"""Local preflight regression tests; standard library, Python 3.9+."""
import contextlib
import copy
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

SYSTEM = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validate_job", SYSTEM / "tools/validate_job.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class TestValidateJob(unittest.TestCase):
    def setUp(self):
        self.draft = json.loads((SYSTEM / "integrationen/BEISPIEL_JOB.json").read_text(encoding="utf-8"))

    def publication_job(self, state):
        job = copy.deepcopy(self.draft)
        job["status"] = state
        job["approval"].update(content_approved=True, execution_authorized=True, revision_sha256="a" * 64)
        job["assets"] = [{"sha256": "b" * 64, "rights_status": "cleared"}]
        job["scheduled_at"] = "2026-10-28T12:00:00+01:00"
        if state == "published":
            job["external_post_id"] = "fictional-post-001"
        return job

    def validate(self, job, expected_error=None):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "job.json"
            path.write_text(json.dumps(job), encoding="utf-8")
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                code = validator.main(path)
        result = json.loads(output.getvalue())
        self.assertEqual(code, 0 if expected_error is None else 2)
        self.assertEqual(result["ok_local"], expected_error is None)
        # Each negative case isolates one defect, rather than passing due to an unrelated error.
        self.assertEqual(result["errors"], [] if expected_error is None else [expected_error])

    def test_example_draft_needs_no_publication_approval(self):
        self.validate(self.draft)

    def test_valid_publication_states(self):
        for state in sorted(validator.PUBLISH_STATES):
            with self.subTest(state=state):
                self.validate(self.publication_job(state))

    def test_publication_requires_both_approvals(self):
        for state in sorted(validator.PUBLISH_STATES):
            for field, error in (("content_approved", "publication state without content approval"),
                                 ("execution_authorized", "publication state without execution authorization")):
                for value in (False, None):
                    with self.subTest(state=state, field=field, value=value):
                        job = self.publication_job(state)
                        if value is None:
                            del job["approval"][field]
                        else:
                            job["approval"][field] = value
                        self.validate(job, error)

    def test_publication_requires_revision(self):
        for state in sorted(validator.PUBLISH_STATES):
            with self.subTest(state=state):
                job = self.publication_job(state)
                del job["approval"]["revision_sha256"]
                self.validate(job, "publication state without revision fingerprint")

    def test_publication_requires_cleared_asset_rights(self):
        for state in sorted(validator.PUBLISH_STATES):
            for rights in (None, "pending"):
                with self.subTest(state=state, rights=rights):
                    job = self.publication_job(state)
                    if rights is None:
                        del job["assets"][0]["rights_status"]
                    else:
                        job["assets"][0]["rights_status"] = rights
                    self.validate(job, "asset 0 rights not cleared")

    def test_published_requires_platform_id(self):
        job = self.publication_job("published")
        del job["external_post_id"]
        self.validate(job, "published without remote platform post id")

    def test_schedule_requires_timezone(self):
        job = self.publication_job("scheduled")
        job["scheduled_at"] = "2026-10-28T12:00:00"
        self.validate(job, "scheduled_at lacks timezone")

    def test_schedule_accepts_utc_and_offsets(self):
        for timestamp in ("2026-10-28T12:00:00Z", "2026-10-28T12:00:00+01:00", "2026-10-28T12:00:00-04:00"):
            with self.subTest(timestamp=timestamp):
                job = self.publication_job("scheduled")
                job["scheduled_at"] = timestamp
                self.validate(job)

    def test_invalid_schedule(self):
        job = self.publication_job("scheduled")
        job["scheduled_at"] = "invalid"
        self.validate(job, "invalid scheduled_at")


if __name__ == "__main__":
    unittest.main()

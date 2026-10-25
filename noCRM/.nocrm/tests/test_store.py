import importlib.util
from pathlib import Path
import tempfile
import unittest
spec=importlib.util.spec_from_file_location('store',Path(__file__).parents[1]/'tools'/'contact_store.py')
store=importlib.util.module_from_spec(spec);spec.loader.exec_module(store)
class StoreTests(unittest.TestCase):
    def test_init_creates_only_on_request(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertFalse((Path(d)/'kontakte').exists())
            store.init(d)
            self.assertTrue((Path(d)/'kontakte/contacts.csv').exists())
    def test_add_keeps_one_contact(self):
        with tempfile.TemporaryDirectory() as d:
            store.init(d);store.add(d,'A-1','Test Beispiel')
            lines=(Path(d)/'kontakte/contacts.csv').read_text().splitlines()
            self.assertEqual(len(lines),2)
            with self.assertRaises(ValueError):store.add(d,'A-1','Doppelt')
    def test_no_auto_initialize_on_add(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):store.add(d,'A-1','Test')
if __name__=='__main__':unittest.main()

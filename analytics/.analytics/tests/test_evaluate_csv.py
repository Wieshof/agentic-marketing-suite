import csv
import importlib.util
import pathlib
import tempfile
import unittest

SCRIPT=pathlib.Path(__file__).resolve().parents[1]/'tools'/'evaluate_csv.py'
spec=importlib.util.spec_from_file_location('eval_csv', SCRIPT)
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path=pathlib.Path(self.tmp.name)/'data.csv'
        self.a=m.window('2026-01-01:2026-01-07'); self.b=m.window('2026-01-08:2026-01-14')
    def save(self, rows, columns=('date','n','d','segment')):
        with self.path.open('w',encoding='utf-8',newline='') as f:
            w=csv.DictWriter(f,fieldnames=columns)
            w.writeheader();w.writerows(rows)
    def rows(self):
        return [{'date':f'2026-01-{day:02d}','n':'10' if day<8 else '20','d':'100','segment':'x'} for day in range(1,15)]
    def test_sum(self):
        self.save(self.rows())
        r=m.analyze(self.path,'date','n',None,self.a,self.b)
        self.assertEqual(r['period_a']['value'],70.0)
        self.assertEqual(r['period_b']['value'],140.0)
        self.assertEqual(r['relative_change'],1.0)
        self.assertEqual(r['evidence_level'],'descriptive')
    def test_weighted_rate(self):
        self.save(self.rows())
        r=m.analyze(self.path,'date','n','d',self.a,self.b)
        self.assertAlmostEqual(r['period_a']['value'],.1)
        self.assertAlmostEqual(r['period_b']['value'],.2)
    def test_missing(self):
        self.save(self.rows())
        with self.assertRaisesRegex(ValueError,'Fehlende Spalten'): m.analyze(self.path,'date','missing',None,self.a,self.b)
    def test_duplicate_key(self):
        self.save(self.rows()+[self.rows()[0]])
        with self.assertRaisesRegex(ValueError,'doppeltes'): m.analyze(self.path,'date','n',None,self.a,self.b)
    def test_negative_number(self):
        rows=self.rows();rows[1]['n']='-5'; self.save(rows)
        with self.assertRaisesRegex(ValueError,'nichtnegativ'):m.analyze(self.path,'date','n',None,self.a,self.b)
    def test_nonnumeric(self):
        rows=self.rows();rows[0]['n']='NaN';self.save(rows)
        with self.assertRaisesRegex(ValueError,'nichtnegativ'):m.analyze(self.path,'date','n',None,self.a,self.b)
    def test_zero_denominator(self):
        rows=self.rows();[r.update(d='0') for r in rows if int(r['date'][-2:])>=8];self.save(rows)
        r=m.analyze(self.path,'date','n','d',self.a,self.b)
        self.assertIsNone(r['difference']);self.assertEqual(r['direction'],'not_computable')
    def test_no_period_rows(self):
        self.save(self.rows()[:7])
        with self.assertRaisesRegex(ValueError,'keine Messzeilen'):m.analyze(self.path,'date','n',None,self.a,self.b)
    def test_segment_filter(self):
        rows=self.rows()+[{'date':f'2026-01-{day:02d}','n':'9999','d':'10000','segment':'y'} for day in range(1,15)]
        self.save(rows)
        r=m.analyze(self.path,'date','n',None,self.a,self.b,'segment','x')
        self.assertEqual(r['period_a']['value'],70)
    def test_overlap_error(self):
        self.save(self.rows())
        with self.assertRaisesRegex(ValueError,'überschneiden'):m.analyze(self.path,'date','n',None,self.a,m.window('2026-01-05:2026-01-14'))
    def test_invalid_date(self):
        rows=self.rows();rows[0]['date']='05/01/2026';self.save(rows)
        with self.assertRaisesRegex(ValueError,'Datum'):m.analyze(self.path,'date','n',None,self.a,self.b)
    def test_first_baseline_zero(self):
        rows=self.rows();[r.update(n='0') for r in rows if int(r['date'][-2:])<8];self.save(rows)
        r=m.analyze(self.path,'date','n',None,self.a,self.b)
        self.assertIsNone(r['relative_change'])
        self.assertTrue(any('Null-Baseline' in w for w in r['warnings']))

if __name__=='__main__': unittest.main()

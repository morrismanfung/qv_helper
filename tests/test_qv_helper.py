import sys
import unittest
import pandas as pd
from io import StringIO
import sys
from qv_helper.qv_helper import qv_groups, qv_scatter, qv_2cat, qv_count, qv_dist

test_data = pd.DataFrame(
    {
        'group_homo':[0, 0, 0, 0, 0, 0],
        'groupA':[0, 1, 0, 1, 0, 1],
        'groupB':[8, 8, 8, 8, 9, 9],
        'groupC': [1, 1, 2, 2, 3, 3],
        'num_homo':[12, 12, 12, 12, 12, 12],
        'numA': [ 1, 1, 2, 3, 4, 5], # One group is with 0 variance
        'numB': [ 1, 2, 3, 4, 5, 6]
    }
)

test_empty = pd.DataFrame(
    {
        'A': [],
        'B': []
    }
)

class TestCaseForqv_groups(unittest.TestCase):
    def test_empty_data(self):
        with self.assertRaises(Exception):
            qv_groups('A', 'B', test_empty)

    def test_1_group_only(self):
        with self.assertRaises(Exception):
            qv_groups('numA', 'group_homo', test_data)

    def test_0_variance(self):
        with self.assertRaises(Exception):
            qv_groups('num_homo', 'groupA', test_data)
    
    def test_0_within_group_variance(self):
        with self.assertRaises(Exception):
            qv_groups('numA', 'groupC', test_data)

    def test_t_test(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        qv_groups('numA', 'groupA', test_data)
        self.assertEqual( captured_output.getvalue().strip().replace(' ', '')[:6], 'Testtp')
    
    def test_F_test(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        qv_groups('numB', 'groupC', test_data)
        self.assertEqual( captured_output.getvalue().strip().replace(' ', '')[:6], 'TestFp')

class TestCaseForqv_scatter(unittest.TestCase):
    def test_r_test(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        qv_scatter('numA', 'numB', test_data)
        self.assertEqual( captured_output.getvalue().strip().replace(' ', '')[:6], 'Testrp')

class TestCaseForqv_2cat(unittest.TestCase):
    def test_2x2(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        qv_2cat('groupA', 'groupB', test_data)
        self.assertEqual( captured_output.getvalue().strip().replace(' ', '')[:6], 'TestTe')
    
    def test_chi2_only(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        qv_2cat('groupA', 'groupC', test_data)
        self.assertEqual( captured_output.getvalue().strip().replace(' ', '')[:6], 'TestTe')

class TestCaseForqv_count(unittest.TestCase):
    def test_count(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        qv_count('groupC', test_data)
        self.assertEqual( captured_output.getvalue().strip().replace(' ', '')[:6], 'GroupC')

class TestCaseForqv_dist(unittest.TestCase):
    def test_count(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        qv_dist('numA', test_data)
        self.assertEqual( captured_output.getvalue().strip().replace(' ', '')[:6], 'Statis')

if __name__ == '__main__':
    unittest.main()
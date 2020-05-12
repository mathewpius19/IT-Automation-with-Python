from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase="Mathew, Pius"
        expected="Pius, Mathew"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)
    
    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M., Hopper"
        self.assertEqual(rearrange_name(testcase), expected)
    
    def test_one_name(self):
        testcase = "Mathew"
        expected = "Mathew"
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()
import unittest
from Range import Range

class TestRange(unittest.TestCase):
    def setUp(self):
        self.rngObj = Range(3, 8)
    
    def test_contains(self):
        self.assertTrue(self.rngObj.contains(4))
        self.assertTrue(self.rngObj.contains(7))
        self.assertFalse(self.rngObj.contains(-1))
        self.assertFalse(self.rngObj.contains(12))
    
    def test_overlaps(self):
        self.assertTrue(self.rngObj.overlaps(Range(1, 4)))
        self.assertTrue(self.rngObj.overlaps(Range(5)))
        self.assertFalse(self.rngObj.overlaps(Range(-4, 2)))
        self.assertFalse(self.rngObj.overlaps(Range(8, 10)))
    
    def test_sub_range(self):
        self.assertTrue(self.rngObj.is_sub_range(Range(2, 9)))
        self.assertTrue(self.rngObj.is_sub_range(Range(-4, 12)))
        self.assertFalse(self.rngObj.is_sub_range(Range(1, 6)))
        self.assertFalse(self.rngObj.is_sub_range(Range(2, 4)))

    def test_disjoint(self):
        self.assertTrue(self.rngObj.is_disjoint(Range(-4, 2)))
        self.assertTrue(self.rngObj.is_disjoint(Range(8, 10)))
        self.assertFalse(self.rngObj.is_disjoint(Range(1, 4)))
        self.assertFalse(self.rngObj.is_disjoint(Range(5)))
    
    def test_touching(self):
        self.assertTrue(self.rngObj.is_touching(Range(3)))
        self.assertTrue(self.rngObj.is_touching(Range(8, 12)))
        self.assertFalse(self.rngObj.is_touching(Range(6)))
        self.assertFalse(self.rngObj.is_touching(Range(5, 10)))

    def test_combine_true(self):
        rObj = Range(5, 12)
        combined_obj = self.rngObj.combine(rObj)
        expected_op = Range(3, 12)
        self.assertTrue(combined_obj.is_equal_to(expected_op))
    
    def test_combine_disjoint_ranges(self):
        rObj = Range(-5, 1)
        combined_obj = self.rngObj.combine(rObj)
        expected_op = Range(0, 0)
        self.assertTrue(combined_obj.is_equal_to(expected_op))
    
    def test_is_equal_to(self):
        self.assertTrue(self.rngObj.is_equal_to(Range(3, 8)))
        self.assertFalse(self.rngObj.is_equal_to(Range(3, 7)))

    def test_is_less_than(self):
        self.assertTrue(self.rngObj.is_less_than(Range(4, 12)))
        self.assertTrue(self.rngObj.is_less_than(Range(3, 10)))
        self.assertFalse(self.rngObj.is_less_than(Range(3, 6)))
        self.assertFalse(self.rngObj.is_less_than(Range(2, 4)))

    def test_is_more_than(self):
        self.assertTrue(self.rngObj.is_more_than(Range(3, 6)))
        self.assertTrue(self.rngObj.is_more_than(Range(2, 6)))
        self.assertFalse(self.rngObj.is_more_than(Range(3, 12)))
        self.assertFalse(self.rngObj.is_more_than(Range(3, 10)))
    
    def test_length(self):
        self.assertEqual(self.rngObj.length(), 5)
        self.assertEqual(Range(-2, 5).length(), 7)
        self.assertEqual(Range(3, 9).length(), 6)

if __name__ == '__main__':
    unittest.main()
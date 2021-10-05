#!/usr/bin/python3
"""
Unittest
"""


import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def test(self):
        self.assertEqual(max_integer([5,9]), 9)

    def test_fail(self):
        with self.assertRaises(TypeError):
            max_integer(['aa', 3])
    
    def test_string(self):
        self.assertEqual(max_integer('why'), 'a')

    def test_max_at_end(self):
        self.assertEqual(max_integer([7, 4, 9]), 9)

    def testMaxAtBeginning(self):
        self.assertEqual(max_integer([8, 1, 6]), 8)

    def test_negative(self):
        self.assertEqual(max_integer([-8, 0]), 0)

    def testTwoNegative(self):
        self.assertEqual(max_integer([-1, -4]), -1)

    def testMaxMiddle(self):
        self.assertEqual(max_integer([1,3,2]), 3)

    def test_one_num(self):
        self.assertEqual(max_integer([5]), 5)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

if __name__ == "__main__":
    unittest.main()

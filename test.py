from add import *
import unittest

class TestAdd(unittest.TestCase):

    def testEmptyString(self):
        self.assertEqual(Add(""),0)

    def testSingleNumber(self):
        self.assertEqual(Add("2"), 2)

    def testTwoNumbers(self):
        self.assertEqual(Add("2,3"),5)

    def testOnlyComa(self):
        with self.assertRaises(ValueError):
            Add(",")
    
    def testNotFullExpression(self):
        with self.assertRaises(ValueError):
            Add("2,")

    def testMultipleNumbers(self):
        self.assertEqual(Add("2,3,1,4,5"), 15)
    
    def testIncludeNewLineBetween(self):
        self.assertEqual(Add("1\n2,3"), 6)

    def testBadNewLineAtEnd(self):
        with self.assertRaises(ValueError):
            Add("1,\n")
        with self.assertRaises(ValueError):
            Add("1\n\n2")
        with self.assertRaises(ValueError):
            Add("1,\n3")
        with self.assertRaises(ValueError):
            Add("\n2,")
        with self.assertRaises(ValueError):
            Add("\n3")
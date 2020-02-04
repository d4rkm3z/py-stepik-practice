#!/usr/bin/env python

import unittest
from declention_words import hello

class TestStringMethods(unittest.TestCase):
    def testHello(self):
        self.assertEqual(hello(1), '1 программист')
        self.assertEqual(hello(11), '11 программистов')
        self.assertEqual(hello(111), '111 программистов')
        self.assertEqual(hello(12), '12 программистов')
        self.assertEqual(hello(13), '13 программистов')
        self.assertEqual(hello(14), '14 программистов')
        self.assertEqual(hello(16), '16 программистов')
        self.assertEqual(hello(20), '20 программистов')
        self.assertEqual(hello(21), '21 программист')
        self.assertEqual(hello(60), '60 программистов')
        self.assertEqual(hello(92), '92 программиста')
        self.assertEqual(hello(100), '100 программистов')
        self.assertEqual(hello(700), '700 программистов')
        self.assertEqual(hello(101), '101 программист')
        self.assertEqual(hello(999), '999 программистов')
        self.assertEqual(hello(2), '2 программиста')
        self.assertEqual(hello(21), '21 программист')
        self.assertEqual(hello(44), '44 программиста')
        self.assertEqual(hello(5), '5 программистов')
        self.assertEqual(hello(1000), '1000 программистов')
        self.assertEqual(hello(0), '0 программистов')
        self.assertEqual(hello(9), '9 программистов')
        self.assertEqual(hello(754), '754 программиста')
        self.assertEqual(hello(689), '689 программистов')


unittest.main()

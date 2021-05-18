#!/usr/bin/env python

import unittest
import wrapping

class WrappingTest(unittest.TestCase):
    def test_one(self):
        line = '2x3x4'
        box = wrapping.Box(line)
        got = box.paper()
        want = 58
        self.assertEqual(got, want)

    def test_two(self):
        line = '1x1x10'
        box = wrapping.Box(line)
        got = box.paper()
        want = 43
        self.assertEqual(got, want)

    def test_ribbon_one(self):
        line = '2x3x4'
        box = wrapping.Box(line)
        got = box.ribbon()
        want = 34
        self.assertEqual(got, want)

    def test_ribbon_two(self):
        line = '1x1x10'
        box = wrapping.Box(line)
        got = box.ribbon()
        want = 14
        self.assertEqual(got, want)

if __name__ == "__main__":
    unittest.main()

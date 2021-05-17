#!/usr/bin/env python3

import floors
import unittest

class FloorsTest(unittest.TestCase):
    def test_simple_balanced_case(self):
        data = "()()"
        got = floors.floor(data)
        want = 0
        self.assertEqual(got, want)

    def test_simple_ascent(self):
        data = "((("
        got = floors.floor(data)
        want = 3
        self.assertEqual(got, want)


if __name__ == "__main__":
    unittest.main()

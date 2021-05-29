#!/usr/bin/env python3

import nicestring
import unittest

class TestNiceString(unittest.TestCase):
    def test_short_nice_string(self):
        candidate = 'aaa'
        want = True
        got = nicestring.check(candidate)
        self.assertEqual(got, want)

    def test_long_nice_string(self):
        candidate = 'ugknbfddgicrmopn'
        want = True
        got = nicestring.check(candidate)
        self.assertEqual(got, want)

if __name__ == "__main__":
    unittest.main()

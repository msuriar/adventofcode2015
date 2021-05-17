#!/usr/bin/env python3

import basement
import unittest

class BasementTest(unittest.TestCase):
    def test_base_case(self):
        data = ")"
        got = basement.position(data)
        want = 1
        self.assertEqual(got, want)

    def test_longer_thing(self):
        data = "()())"
        got = basement.position(data)
        want = 5
        self.assertEqual(got, want)

    def test_suffix(self):
        data = ")("
        got = basement.position(data)
        want = 1
        self.assertEqual(got, want)

if __name__ == "__main__":
    unittest.main()

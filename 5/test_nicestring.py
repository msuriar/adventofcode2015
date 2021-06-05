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

    def test_it_requires_double_letter(self):
        candidate = 'jchzalrnumimnmhp'
        want = False
        got = nicestring.check(candidate)
        self.assertEqual(got, want)

    def test_it_rejects_bad_strings(self):
        candidate = 'haegwjzuvuyypxyu'
        want = False
        got = nicestring.check(candidate)
        self.assertEqual(got, want)

    def test_it_requires_three_vowels(self):
        candidate = 'dvszwmarrgswjxmb'
        want = False
        got = nicestring.check(candidate)
        self.assertEqual(got, want)

class TestNiceString2(unittest.TestCase):
    def test_short_nice_string(self):
        candidate = 'xxyxx'
        want = True
        got = nicestring.check2(candidate)
        self.assertEqual(got, want)

    def test_long_nice_string(self):
        candidate = 'qjhvhtzxzqqjkmpb'
        want = True
        got = nicestring.check2(candidate)
        self.assertEqual(got, want)

    def test_it_needs_repeat_with_single_letter_between(self):
        candidate = 'uurcxstgmygtbstg'
        want = False
        got = nicestring.check2(candidate)
        self.assertEqual(got, want)

    def test_it_needs_duplicate_pairs(self):
        candidate = 'ieodomkazucvgmuy'
        want = False
        got = nicestring.check2(candidate)
        self.assertEqual(got, want)

if __name__ == "__main__":
    unittest.main()

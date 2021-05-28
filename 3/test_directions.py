#!/usr/bin/env python3

import directions
import unittest

class TestDirections(unittest.TestCase):
    def test_empty_string(self):
        course = ''
        want = 1

        houses = directions.traverse(course)
        got = houses.have_presents()
        self.assertEqual(got, want)

    def test_double_move(self):
        course = '^>'
        want = 3

        houses = directions.traverse(course)
        got = houses.have_presents()
        self.assertEqual(got, want)

    def test_backtrack(self):
        course = '^v'
        want = 2

        houses = directions.traverse(course)
        got = houses.have_presents()
        self.assertEqual(got, want)

    def test_present_count_filter(self):
        course = '<>'
        want = 1

        houses = directions.traverse(course)
        got = houses.have_presents(min_count=2)
        self.assertEqual(got, want)


if __name__ == "__main__":
    unittest.main()

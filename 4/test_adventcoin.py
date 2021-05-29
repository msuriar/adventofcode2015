#!/usr/bin/env python3

import adventcoin

import unittest

class TestAdventCoin(unittest.TestCase):
    def test_first(self):
        seed = 'abcdef'
        got = adventcoin.solve(seed)
        want = 609043
        self.assertEqual(got, want)

    def test_second(self):
        seed = 'pqrstuv'
        got = adventcoin.solve(seed)
        want = 1048970
        self.assertEqual(got, want)

if __name__ == "__main__":
    unittest.main()

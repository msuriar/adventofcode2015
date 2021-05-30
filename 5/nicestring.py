#!/usr/bin/env python3

def check(s):
    if not check_double_letter(s):
        return False
    if not check_bad_strings(s):
        return False
    return True

def check_double_letter(s):
    return 1 in [len(set(x)) for x in zip(s, s[1:])]

def check_bad_strings(s):
    bad_strings = set(['ab', 'cd', 'pq', 'xy'])
    pairs = set([''.join(p) for p in zip(s, s[1:])])
    return pairs.isdisjoint(bad_strings)

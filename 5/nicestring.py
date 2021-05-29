#!/usr/bin/env python3

def check(s):
    if not check_double_letter(s):
        return False
    return True

def check_double_letter(s):
    return 1 in [len(set(x)) for x in zip(s, s[1:])]

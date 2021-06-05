#!/usr/bin/env python3

from collections import Counter

def main():
    with open('input.conf') as f:
        print(sum([1 for l in f if check2(l)]))

def check(s):
    if not check_double_letter(s):
        return False
    if not check_bad_strings(s):
        return False
    if not check_vowels(s):
        return False
    return True

def check2(s):
    if not check_repeats_separated_by_one(s):
        return False
    if not check_duplicate_pairs(s):
        return False
    return True

def check_duplicate_pairs(s):
    for i in range(len(s) - 2):
        pair = s[i:i+2]
        rest = s[i+2:]
        pairs = set(''.join(p) for p in zip(rest, rest[1:]))
        if pair in pairs:
            return True
    return False

def check_double_letter(s):
    return 1 in [len(set(x)) for x in zip(s, s[1:])]

def check_repeats_separated_by_one(s):
    pairs = zip(s, s[2:])
    return 1 in [len(set(x)) for x in zip(s, s[2:])]

def check_bad_strings(s):
    bad_strings = set(['ab', 'cd', 'pq', 'xy'])
    pairs = set([''.join(p) for p in zip(s, s[1:])])
    return pairs.isdisjoint(bad_strings)

def check_vowels(s):
    vowels = set('aeiou')
    num_vowels = sum((1 for c in s if c in vowels))
    return num_vowels >= 3

if __name__ == "__main__":
    main()

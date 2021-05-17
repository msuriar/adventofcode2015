#!/usr/bin/env python3

from collections import Counter

def main():
    with open('input.conf') as f:
        floorstring = f.read()
    print(floor(floorstring))

def floor(floors):
    c = Counter(floors)
    return c["("] - c[")"]

if __name__ == "__main__":
    main()

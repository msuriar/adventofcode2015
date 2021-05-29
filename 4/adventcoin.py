#!/usr/bin/env python3

import hashlib

def main():
    incoming = 'bgvyzdsv'
    target = '0'*6
    print(solve(incoming, target))

def solve(seed, target):
    counter = 1
    while True:
        candidate = str.encode(seed+str(counter))
        solution = hashlib.md5(candidate).hexdigest()
        if solution.startswith(target):
            return counter
        counter += 1

if __name__ == "__main__":
    main()

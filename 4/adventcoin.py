#!/usr/bin/env python3

import hashlib

def main():
    incoming = 'bgvyzdsv'
    print(solve(incoming))

def solve(seed):
    counter = 1
    while True:
        candidate = str.encode(seed+str(counter))
        prefix = hashlib.md5(candidate).hexdigest()[:5]
        if prefix == '00000':
            return counter
        counter += 1

if __name__ == "__main__":
    main()

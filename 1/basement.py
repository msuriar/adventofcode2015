#!/usr/bin/env python3

def main():
    with open('input.conf') as f:
        floorstring = f.read()
    print(position(floorstring))

def position(floorstring):
    floor = 0
    position = 1
    for c in floorstring:
        if c == ")":
            floor -= 1
        elif c == "(":
            floor += 1
        if floor == -1:
            return position
        else:
            position += 1

if __name__ == "__main__":
    main()

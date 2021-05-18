#!/usr/bin/env python3

from functools import reduce
from itertools import combinations
from operator import mul

def parse_line(line):
    return tuple([int(c) for c in line.split('x')])

class Box():
    def __init__(self, line):
        self.dimensions = parse_line(line)

    def paper(self):
        return self.area() + self.slack()

    def ribbon(self):
        return min(self.perimeters()) + self.volume()

    def perimeters(self):
        pairs = combinations(self.dimensions, 2)
        return tuple([2*(x+y) for x,y in pairs])

    def volume(self):
        return reduce(mul, self.dimensions)

    def area(self):
        return 2*sum(self.faces())

    def slack(self):
        return min(self.faces())

    def faces(self):
        pairs = combinations(self.dimensions, 2)
        return tuple([x*y for x,y in pairs])

def main():
    total = 0
    with open('input.conf') as f:
        for line in f:
            total += Box(line).ribbon()

    print(total)

if __name__ == "__main__":
    main()

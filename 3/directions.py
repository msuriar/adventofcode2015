#!/usr/bin/env python

from collections import defaultdict

def main():
    with open('input.conf') as f:
        course = f.read()
        santa = course[::2]
        robosanta = course[1::2]
        t1 = traverse(santa)
        t2 = traverse(robosanta)
        all_locations = set(t1.locations.keys() + t2.locations.keys())
        print(len(all_locations))

def traverse(course):
    return Houses(course)

class Houses():
    def __init__(self, course):
        self.course = course
        self._travel()

    def _travel(self):
        x,y = 0,0
        self.locations = defaultdict(int)
        self.locations[(x, y)] += 1
        for c in self.course:
            if c == '^':
                y += 1
            elif c == 'v':
                y -= 1
            elif c == '>':
                x += 1
            elif c == '<':
                x -= 1
            self.locations[(x,y)] += 1

    def have_presents(self, min_count=1):
        c = 0
        for _, v in self.locations.items():
            if v >= min_count:
                c += 1
        return c

if __name__ == "__main__":
    main()

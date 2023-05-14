#!/usr/bin/env python3

from fakeio import PMIO

if __name__ == '__main__':
    # coprocessor
    pmio = PMIO()
    pmio.OUT(6, 7)
    pmio.OUT(7, 2)
    # add
    pmio.OUT(8, 0)
    print(pmio.IN(9))
    # sub
    pmio.OUT(8, 1)
    print(pmio.IN(9))
    # mul
    pmio.OUT(8, 2)
    print(pmio.IN(9))
    # div
    pmio.OUT(8, 3)
    print(pmio.IN(9))
    # entropy
    print(pmio.IN(1))
    # printer
    pmio.OUT(0, 65)
    # tape
    pmio.OUT(4, 4)
    pmio.OUT(5, 0)
    print(pmio.IN(2))
    pmio.OUT(5, 5)
    pmio.OUT(3, 888888)

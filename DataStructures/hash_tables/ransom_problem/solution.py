#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter


def checkMagazine(magazine, note):
    magazine_hash = Counter(magazine)
    note_hash = Counter(note)
    difference = note_hash - magazine_hash
    if difference:
        print("No")
        return
    print("Yes")


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

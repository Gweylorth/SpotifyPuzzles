#!/usr/bin/python
""" A short script to reverse numbers in binary
By Gwenegan Hudin
29/05/2013
gwenegan.hudin@insa-rennes.fr

"""

import sys

input = sys.stdin

print int(str(bin(int(input.readline())))[:1:-1], 2)
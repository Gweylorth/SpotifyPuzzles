#!/usr/bin/python
""" 'Cat vs. Dog' reality show tool
By Gwenegan Hudin
29/05/2013
gwenegan.hudin@insa-rennes.fr
Puzzle : https://www.spotify.com/us/jobs/tech/catvsdog/

"""

import sys

input = sys.stdin

cases = int(input.readline())
results = ''
i = 0
while i < cases:
    k = 0
    c, d, v = [int(x) for x in input.readline().split()]
    votes = dict()
    for j in range(0, c+d+1):
        if j < c:
            votes['C' + str(j+1)] = 1
        else:
            votes['D' + str(j-c+1)] = 1
    while k < v:
        v1, v2 = [x for x in input.readline().split()]
        votes[v1] += 1
        votes[v2] -= 1
        k += 1

    maxvotes = max([v for v in votes.itervalues()])
    minvotes = min([v for v in votes.itervalues()])
    print "Maxvotes : " + str(maxvotes)
    if minvotes < 0:
        minvotes = 0
    print "Minvotes : " + str(minvotes)
    happy = maxvotes - minvotes
    if happy == 0:
        happy = 1
    results += str(happy) + "\n"
    i += 1

print results
input.close()
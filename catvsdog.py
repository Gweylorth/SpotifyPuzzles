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
    votes = dict()  # Will store how many upvotes a pet got
    # Create all dictionary keys
    for j in range(0, c+d):
        if j < c:
            votes['C' + str(j+1)] = 0
        else:
            votes['D' + str(j-c+1)] = 0
    scores = votes.copy()  # Will store how much a pet is liked (up - down)

    # For each vote, update the dictionaries
    while k < v:
        v1, v2 = [x for x in input.readline().split()]
        votes[v1] += 1
        scores[v1] += 1
        scores[v2] -= 1
        k += 1

    # How many votes got the pet with the best score?
    max_score_pet = max(scores, key=scores.get)
    max_vote = votes[max_score_pet]

    # Update the results with the current session
    results += str(max_vote) + "\n"
    i += 1

print results.rstrip()
input.close()
#!/usr/bin/python
""" A short script to sort songs according to their quality
By Gwenegan Hudin
16/01/2013
gwenegan.hudin@insa-rennes.fr
Puzzle : https://www.spotify.com/us/jobs/tech/zipfsong/

"""

from operator import itemgetter
import sys

f = sys.stdin

#Get number of songs in the album, and how many to pick
m, n = [int(x) for x in f.readline().split()]
        
# Generate an array of tuples (quality, rank, songname)
# rank will help to order songs with same quality by order of appearance

songlist = []
for i in range(1, m+1) :
    song = f.readline().split()
    count = long(song[0])
    name = song[1]
    quality = count*i
    songlist.append((quality, m-i, name))

f.close()

# Sort the song list according to quality, then to rank
songlist.sort(key = itemgetter(0,1))
songlist.reverse()

# Prints n songs
for i in range(n) :
    print songlist[i][2]

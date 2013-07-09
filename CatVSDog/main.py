#!/usr/bin/python
""" 'Cat vs. Dog' reality show tool
By Gwenegan Hudin
09/07/2013
gwenegan.hudin@insa-rennes.fr
Puzzle : https://www.spotify.com/us/jobs/tech/catvsdog/

Done thanks to Alonso Vidales tips and code :
http://alonso-vidales.blogspot.fr/2013/03/new-spotify-puzzles-reversed-binary.html

"""

import sys
from bipartite_match import bipartiteMatch

# Set this to false before sending solution, true to use the test file
debug = False

input = open('test', 'r') if debug else sys.stdin

cases = int(input.readline())
i = 0

while i < cases:
	k = 0
	# We're only interested in the number of voters
	_, _, v = [int(x) for x in input.readline().split()]
	
	# All of cat lovers votes
	catLovers = []
	# Who did dog lovers vote for ?
	dogLoversUpvote = {}
	# Who did dog lovers vote against ?
	dogLoversDownvote = {}
	# Final bipartite graph, conflicting cat lovers' votes (up and down) against dog lovers'
	bipartite = {}
	
	while k < v:
		v1, v2 = input.readline().split()
		# We keep the 'k' index to be sure to differenciate each and every vote, even if the votes
		# are similar
		vote = "{} {} {}".format(v1, v2, k)
		
		# If dog lover...
		if v1.startswith("D"):
			# Add this vote to the set of a dog's upvotes, or create a new set
			if v1 in dogLoversUpvote:
				dogLoversUpvote[v1].add(vote)
			else:
				dogLoversUpvote[v1] = set([vote])
			
			# Add this vote to the set of a cat's downvotes, or create a new set
			if v2 in dogLoversDownvote:
				dogLoversDownvote[v2].add(vote)
			else:
				dogLoversDownvote[v2] = set([vote])
				
		# Else cat lover...
		else:
			catLovers.append(vote)
		
		k += 1
	
	# Populate the bipartite graph with problematic edges, eg conflicting votes 
	# (DogLovers downvotes vs CatLover upvote UNION DogLovers upvotes vs CatLover downvote)
	for vote in catLovers:
		upvote, downvote, _ = vote.split()
		bipartite[vote] = dogLoversUpvote.get(downvote, set()).union(dogLoversDownvote.get(upvote, set()))
		
	# Let's use Hopcroft-Karp algorithm to compute the maximum cardinality of the bipartite graph
	# we created : minimum number of conflicting voters
	maxMatching = bipartiteMatch(bipartite)[0]
	
	if debug:
		print ("Votes: {}".format(bipartite))
		print ("Max matching {}".format(maxMatching))
		print ("Dog love: {}".format(dogLoversUpvote))
		print ("Dog hate: {}".format(dogLoversDownvote))
		
	i += 1
	
	# Final result
	print(str(v - len(maxMatching)))
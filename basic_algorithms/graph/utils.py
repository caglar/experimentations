import random as rnd
import numpy as np


#n is number of nodes
#a is the number of edges
def gen_random_graph(n, a):
	G = np.zeros((n,n))	
	for i in xrange(a-1):
		start_node = rnd.randint(0, n-1)
		end_node = rnd.randint(0, n-1)
		while start_node == end_node and G[start_node, end_node] != 0:
			start_node = rnd.randint(0, n-1)
			end_node = rnd.randint(0, n-1)
		G[start_node, end_node] = rnd.randint(20, 80)
		G[end_node, start_node] = G[start_node, end_node]
	return G



import random as rnd
import numpy as np

def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

#n is number of nodes
#a is the number of edges
def gen_random_graph(n, a):
	G = np.zeros((n,n))	
	max_edges = choose(n, 2) 
	if a > max_edges:
		print "Maximum number of edges that you can use is, ", max_edges
		a = max_edges
	print a
	for i in xrange(a):
		(start_node, end_node) = rnd.sample(xrange(n), 2)

		while G[start_node, end_node] != 0:
			(start_node, end_node) = rnd.sample(xrange(n), 2)
		print start_node, end_node
		G[start_node, end_node] = rnd.randint(20, 80)
		G[end_node, start_node] = G[start_node, end_node]
	return G



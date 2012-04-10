import numpy as np
from basic_algorithms.graph.utils import *

#X is an mxn matrix
def get_cov_mat(X):
	(nrows, ncols) = X.shape
	mu = X.mean(axis=0)
	cov = np.zeros((nrows, nrows))
	for i in xrange(nrows):
		for j in xrange(i, nrows):
			a = (X[i] - mu)
			b = (X[j] - mu)
			cov[i,j] = a.dot(b) / nrows	
	return cov + cov.T

if __name__=="__main__":
	G = gen_random_graph(10, 20)
	cov = get_cov_mat(G)
	print cov

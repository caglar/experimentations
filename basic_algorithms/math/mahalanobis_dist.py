import numpy as np
from basic_algorithms.graph.utils import *
from basic_algorithms.math.cov_mat import *

#X is a 1xd vector
#M is a dxn matrix
def get_mah_dist(x, M):
	(nrows, ncols) = M.shape
	sigma = np.matrix(get_cov_mat(M))
	sigma_inv = np.array(sigma.I)
	mu = M.mean(axis=0)
	a = x - mu
	return np.sqrt(a.T.dot(sigma_inv).dot(a))

if __name__=="__main__":
	M = gen_random_graph(5, 20)
	x = np.array([1, 2, 3, 5, 0])
	mah_dist = get_mah_dist(x, M)
	print mah_dist


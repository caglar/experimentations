import sys
import copy
import pprint as pp

def floyd_warshall_(w, n):
	d = {0: w}
	for k in range(n):
		if k!=0:
			d[k] = copy.copy(d[k-1])
		for i in range(n):
			for j in range(n):
				d[k][i][j] = min(d[k][i][j], d[k][i][k] + d[k][k][j])
		if k == 0 or k == n-2:
			pp.pprint(d[k])
	return d


def floyd_warshall(w, n):
	d = {0: w}
	for k in range(1,n+1):
		d[k] = {}
		for i in range(1,n+1):
			for j in range(1,n+1):
				d[k][i][j] = min(d[k-1][i][j],
						d[k-1][i][k] + d[k-1][k][j])
				return d[n]

#"""Test1
n = 10
inf = sys.maxint

g= [[0, 5, inf, inf, inf, inf, 1, inf, inf, inf],
		[15, 0, inf, inf, inf, inf, inf, inf, 1, 13],
		[inf, inf, 0, 7, inf, inf, inf,inf, inf, inf],
		[inf, inf, inf, 0, inf, inf, inf, inf, 6, inf],
		[inf, inf, inf, inf, 0, inf, inf, 17, inf, 1],
		[13, 18, inf, inf, 1, 0, inf, inf, inf, inf],
		[inf, 2, inf, inf, inf, inf, 0, inf, inf, inf],
		[inf, inf, inf, 8, inf, 1, inf, 0, inf, inf],
		[inf, inf, 5, 3, inf, inf, inf, 1, 0, inf],
		[2, inf, inf, inf, inf, inf, inf, 10, inf, 0]]

d = floyd_warshall_(g, n)
#"""

"""
inf = sys.maxint

n = 4
g = [[0, 5, inf, inf],
	[50, 0, 15, 5],
	[30, inf, 0, 15],
	[15, inf, 5, 0]]
d = floyd_warshall_(g, n)
"""

#!/usr/bin/env python


def comb(n, k):
	if k == 0 or k == n:
		return 1
	else: 
		return comb(n-1, k-1) + comb(n-1, k)

print comb(10, 2)


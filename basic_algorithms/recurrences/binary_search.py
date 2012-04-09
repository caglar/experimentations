from __future__ import division
import random as rnd
from linear_search import *
import math

def bin_search_iter(num, lst, low, high):
	while (high >= low):
		mid = int(math.floor((low + high) / 2))
		if lst[mid] == num:
			return mid
		if lst[mid] > num:
			high = mid - 1
		if lst[mid] < num:
			low = mid + 1
	return -1

def bin_search_rec(num, lst, low, high):
	mid = int(math.floor((low + high) / 2))
	if num == lst[mid]:
		return mid
	elif (num < lst[mid]) and (mid > low):
		return bin_search_rec(num, lst, low, mid - 1)
	elif (num > lst[mid]) and (mid < high):
		return bin_search_rec(num, lst, mid+1, high)
	return -1

def bin_search_hybrid(num, lst, low, high):
	mid = int(math.floor((low + high) / 2))
	if num == lst[mid]:
		return mid
	elif (num < lst[mid]) and (mid > low):
		return bin_search_iter(num, lst, low, mid - 1)
	elif (num > lst[mid]) and (mid < high):
		return bin_search_rec(num, lst, mid+1, high)
	return -1


if __name__=="__main__":
	arr = [rnd.randint(0, 80) for i in xrange(100)]
	arr.sort()
	num = 21
	
	idx = bin_search_rec(num, arr, 0, 99)
	idx_iter = bin_search_iter(num, arr, 0, 99)
	idx_hybrid = bin_search_hybrid(num, arr, 0, 99)

	print "bin search rec index: %d"%idx
	print "bin search iter index: %d"%idx_iter
	print "bin search hybrid index: %d"%idx_hybrid
	print "linear search index %d" % linear_search(num, arr)

	if idx != -1:
		assert arr[idx] == num
		print arr[idx]
	assert bin_search_rec(num, arr, 0, 99) == linear_search(num, arr)

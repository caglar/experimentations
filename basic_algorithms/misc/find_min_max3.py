from __future__ import division
import math

def find_min_max(arr):
	sz = len(arr)
	mid = int(math.floor(sz / 2))
	minval = arr[0]
	maxval = arr[0]
	for i in xrange(0, mid+1):
		diff = arr[i] - arr[mid+i]
		if diff > 0:
			if arr[i] > maxval:
				maxval = arr[i]
			elif arr[mid+i] < minval:
				minval = arr[mid+i]
		else:
			if arr[i] < minval:
				minval = arr[i]
			elif arr[mid+i] > maxval:
				maxval = arr[mid+i]
	return (minval, maxval)

arr = [2, 9, 1, 124, 44, 23, 22, 123, 88, 3, 11, 4, 12412, 124, 123, 4938381, 0]
print find_min_max(arr)

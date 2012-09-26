from __future__ import division
import math

def find_min_max(arr):
	sz = len(arr)
	mid = int(math.floor(sz / 2))

	minval = arr[0]
	maxval = arr[sz-1]

	if minval > maxval:
			minval, maxval = maxval, minval

	print "Pairs %d, %d\n" % (0, sz-1)

	for i in xrange(1, mid-1):
		diff = arr[i] - arr[mid+i]
		print "%d, %d" % (i, mid+i)
		if diff > 0:
			if arr[i] > maxval:
				maxval = arr[i]
			if arr[mid+i] < minval:
				minval = arr[mid+i]
		else:
			if arr[i] < minval:
				minval = arr[i]
			if arr[mid+i] > maxval:
				maxval = arr[mid+i]
	return (minval, maxval)

arr = [2, 9, 1, 124, 19123123123123, 3, 44, 23, 22, 123, 88, 3, 11, 4, 5, 12412, 124, 123, 0]
print len(arr)
print find_min_max(arr)

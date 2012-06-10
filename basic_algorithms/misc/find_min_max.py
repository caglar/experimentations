def find_min_max(arr):
	sz = len(arr)
	minval = arr[0]
	maxval = arr[sz - 1]
	for i in xrange(0, sz):
		if arr[i] < minval:
			minval = arr[i]
		elif arr[i] > maxval:
			maxval = arr[i]
	return (minval, maxval)

arr = [2, 9, 1, 124, 44, 23, 22, 123, 88, 0, 11, 4, 12412, 124]
print find_min_max(arr)

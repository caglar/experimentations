
def max_dc(A, hi, lo):

	if hi - lo == 0:
		return -123123

	if hi - lo == 1:
		return A[lo]

	mid = (hi + lo)/2
	max1 = max_dc(A, mid, lo)
	max2 = max_dc(A, hi, mid)
	return max(max1, max2)

A = [ 3, 1231, 412, 4, 5, 623, 2, 911, -1, 23]
print max_dc(A, 8, 0)


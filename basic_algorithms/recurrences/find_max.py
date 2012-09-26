
def get_max(a, off, maxi):
	if off >= len(a):
		return maxi
	if a[off] > maxi:
		maxi = a[off]
	return get_max(a, off + 1,  maxi)

maxi = 0
print get_max([1, 2, 41, 23, 49, 123, 9181, 23], 0, 0)

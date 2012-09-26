
def get_min(a, off, mini):
	if off >= len(a):
		return mini
	if a[off] < mini:
		mini = a[off]
	return get_min(a, off + 1,  mini)

mini = 1231231
print get_min([1, 2, 41, 23, 49, 123, 9181, 23], 0, mini)

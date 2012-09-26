
def insertion_sort(a):
	for i in xrange(1, len(a)):
		j = i -1
		while (j >= 0 and a[j] >= a[j+1]):
			t = a[j]
			a[j] = a[j+1]
			a[j+1] = t
			j -=1
	return a

a = [3, 2, 1, 9, 91, 12, 87, 12, 873, 7162, 1231]

print insertion_sort(a)

#Implementation of linear search just implemented this to test correctness of other algorithms.
def linear_search(num, lst):
	for i, n in enumerate(lst):
		if n == num:
			return i
	return -1

if __name__=="__main__":
	import random as rnd
	arr = [rnd.randint(0, 800) for i in xrange(1000)]
	arr.sort()
	num = 321
	idx = linear_search(num, arr)
	print arr[idx]
	print idx

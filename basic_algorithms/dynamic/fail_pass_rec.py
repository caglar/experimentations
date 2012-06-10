def P(i, j):
	if i==0:
		return 1
	elif j==0:
		return 0
	else:
		return 0.8*P(i-1, j) + 0.2 * P(i, j-1)

print P(4, 4)

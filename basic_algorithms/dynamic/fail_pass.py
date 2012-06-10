import pprint as pp

def fail_pass(n,p):
	P = [[0.0 for i in xrange(n+1)] for j in xrange(n+1)]
	q = 0.2
	P[0][0] = 0 #impossible	
	#Fill from top-left to main diagonal

	for i in xrange(1, n+1):
		P[0][i] = 1
		P[i][0] = 0
		for j in xrange(1, i):
			print "%s, %s: (%s %s), (%s %s)" % (j, i-j, j-1, i-j, j, i-j-1)
			P[j][i-j] = p*P[j-1][i-j] + q*P[j][i-j-1]

	pp.pprint(P)	
	#Fill from below main diagonal to bottom right
	for i in xrange(1, n+1):
		for j in xrange(0, n-i+1):
			print "%s, %s: (%s %s), (%s %s)" % (i+j, n-j, i+j-1, n-j, i+j, n-j-1)
			P[i+j][n-j] = p * P[i+j-1][n-j] + q * P[i+j][n-j-1]
	pp.pprint(P)
	return P[n][n]

print fail_pass(4, 0.8)

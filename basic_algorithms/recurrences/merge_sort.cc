#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>

int* 
merge(int *a, int *b, int alen, int blen)
{
	int acount = 0;
	int bcount = 0;
	int *sorted = new int[alen + blen];

	while (acount <= alen && bcount <= blen) {
		if (a[acount] >= b[bcount]) {
			if (bcount < blen) {
				sorted[acount + bcount] = b[bcount];
				bcount++;
			} else {
				b[bcount] = INT_MAX;
				sorted[acount + bcount] = a[acount];
				acount++;
			}
		} else {
			if (acount < alen) {
				sorted[acount + bcount] = a[acount];
				acount++;
			} else {
				a[acount] = INT_MAX;
				sorted[acount + bcount] = b[bcount];
				bcount++;
			}
		}
	}
	return sorted;
}

int *
merge_sort(int *vals, int len)
{
	if (len == 1)
		return vals;
	int mid = (int)(len/2);
	int *left = new int[mid];
	int *right = new  int[len-mid];

	//Create the left and right sub-arrays
	for (int i = 0; i < len; i++) {
		if (i < mid) {
			left[i] = vals[i];
		}
		else right[i-mid] = vals[i];
	}

	//Recursively split the arrays:	
	left = merge_sort(left, mid);
	right = merge_sort(right, len-mid);
	return merge(left, right, mid, len-mid);
}

int
main()
{
	int len = 13;
	int unsorted[]= {93, 12, 23, 45, 12, 1, 0, 18, 3, 33, -2, 56, 73};	
	int *sorted = new int[len];
	sorted = merge_sort(unsorted, len);
	for(int i = 0; i < len; i++) {
		printf("%d ", sorted[i]);
	}
	printf("\n");
	return EXIT_SUCCESS;
}


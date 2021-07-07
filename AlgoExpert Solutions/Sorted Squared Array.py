# Time O(N log N)
# Space O(1)

def sortedSquaredArray(array):
    # Write your code here.
	for i in range(len(array)):
		array[i] = array[i]**2
	array.sort()
	return array



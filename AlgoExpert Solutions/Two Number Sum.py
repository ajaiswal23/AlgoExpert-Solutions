
def twoNumberSum(array, target):
    # Write your code here.
	dic = {}
	for i in range(len(array)):
		if dic.get(array[i]):
			return [dic[array[i]], array[i]]
		else:
			dic[target - array[i]] = array[i]
			
	return []
    

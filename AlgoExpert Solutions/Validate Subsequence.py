def isValidSubsequence(array, sequence):
    # Write your code here.
	seqItr = 0
	for i in array:
		if seqItr != len(sequence) and sequence[seqItr] == i:
			seqItr += 1
			
	return seqItr == len(sequence)

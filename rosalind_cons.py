def findProfileMatrix(dnaM):

	#Defining the profile matrix
	pMatrix = [[0]*len(dnaM[0]), [0]*len(dnaM[0]), [0]*len(dnaM[0]), [0]*len(dnaM[0])]

	#Counting ocurrences of a nt in dnaM and populating pMatrix
	for j in range(len(dnaM)):
		for i in range(len(dnaM[0])):
			if dnaM[j][i] == 'A':
				pMatrix[0][i] += 1
			elif dnaM[j][i] == 'C':
				pMatrix[1][i] += 1
			elif dnaM[j][i] == 'G':
				pMatrix[2][i] += 1
			elif dnaM[j][i] == 'T':
				pMatrix[3][i] += 1 

	return pMatrix

def findConsensusSequence(pMatrix):

	cSeq = []

	#Determining the highest value in every column of pMatrix using nested conditionals. There's probably an easier way to do this.
	for i in range(len(pMatrix[0])):
		if pMatrix[0][i] > pMatrix[1][i]:
			if pMatrix[0][i] > pMatrix[2][i]:
				if pMatrix[0][i] > pMatrix[3][i]:
					cSeq.append('A')
				else:
					cSeq.append('T')
			elif pMatrix[2][i] > pMatrix [3][i]:
				cSeq.append('G')
			else:
				cSeq.append('T')
		elif pMatrix[1][i] > pMatrix [2][i]:
			if pMatrix[1][i] > pMatrix [3][i]:
				cSeq.append('C')
			else:
				cSeq.append('T')
		elif pMatrix[2][i] > pMatrix [3][i]:
			cSeq.append('G')
		else:
			cSeq.append('T')

	return cSeq


i = open('rosalind_cons.txt', 'r')
o = open('rosalind_cons_out.txt', 'w')


#Collecting the DNA sequences in a matrix
x = 1
dnaMatrix = []

#For this to work, I had to remove all mid-sequence line breaks on the input file. 
for s in i:
    if x % 2 == 0:
    	dnaMatrix.append(s.strip('\n'))
    x += 1

A = findProfileMatrix(dnaMatrix)

o.write(''.join(findConsensusSequence(A))+'\n')
o.write('A:' + ' '.join(['{:2}'.format(item) for item in A[0]])
		+ '\nC:' + ' '.join(['{:2}'.format(item) for item in A[1]])
		+ '\nG:' + ' '.join(['{:2}'.format(item) for item in A[2]])
		+ '\nT:' + ' '.join(['{:2}'.format(item) for item in A[3]]))
 

i.close()
o.close() 

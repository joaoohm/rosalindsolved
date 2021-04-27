def findProfileMatrix(dna):

	for j in range(len(dna)):
		for i in range(len(dna[0])):
			if dna[j][i] == 'A':
				conA[i] += 1
			elif dna[j][i] == 'C':
				conC[i] += 1
			elif dna[j][i] == 'G':
				conG[i] += 1
			elif dna[j][i] == 'T':
				conT[i] += 1 

	conA = map(str, conA)
	conC = map(str, conC)
	conG = map(str, conG)
	conT = map(str, conT)

	return 'A: ' + ' '.join(conA) + '\n' + 'C: ' + ' '.join(conC) + '\n' + 'G: ' + ' '.join(conG) + '\n' + 'T: ' + ' '.join(conT)


i = open('rosalind_cons.txt', 'r')
o = open('rosalind_cons_out.txt', 'w')

x = 1
stringsDNA = []

for s in i:
    if x % 2 == 0:
    	stringsDNA.append(s.strip('\n'))
    x += 1

conA = [0]*len(stringsDNA[0])
conC = [0]*len(stringsDNA[0])
conG = [0]*len(stringsDNA[0])
conT = [0]*len(stringsDNA[0])


o.write(str(findProfileMatrix(stringsDNA)))

       
i.close()
o.close() 

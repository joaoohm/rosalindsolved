def findIEV(num):
	prob = [1, 1, 1, 0.75, 0.5, 0]
	sum = 0
	for i in range(len(num)):
		sum +=(num[i]*prob[i])
	return sum*2


i = open('rosalind_iev.txt', 'r')
o = open('rosalind_iev_out.txt', 'w')

pop = i.read().split(' ')
pop = map(float,pop)

o.write(str(findIEV(pop)))

       
i.close()
o.close() 

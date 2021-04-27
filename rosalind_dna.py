i = open('rosalind_dna.txt', 'r')
o = open('rosalind_dna_out.txt', 'w')

a = 0
c = 0
g = 0
t = 0

for line in i:
    for char in line:
        if char == 'A':
            a += 1
        elif char == 'C':
            c += 1
        elif char == 'G':
            g += 1
        elif char == 'T':
            t += 1

o.write(str(a) + ' ' + str(c) + ' ' + str(g) + ' ' + str(t))
    
       
i.close()
o.close()

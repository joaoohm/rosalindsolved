i = open('rosalind_rna.txt', 'r')
o = open('rosalind_rna_out.txt', 'w')

s = i.readline()

t = s.replace('T', 'U')

o.write(t)
        
i.close()
o.close()

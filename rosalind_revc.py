i = open('rosalind_revc.txt', 'r')
o = open('rosalind_revc_out.txt', 'w')

s = i.readline()
t = ""
u = ""

for x in range(len(s)):
    t += s[len(s) - 1 - x]
    if t[x] == 'A':
        u += 'T'
    elif t[x] == 'C':
        u += 'G'
    elif t[x] == 'G':
        u += 'C'
    elif t[x] == 'T':
        u += 'A'

o.write(u)
        
i.close()
o.close()

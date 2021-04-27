def findGC(s):
    s = s[s.find('\n')+1:].replace('\n', '')
    x = 0.0
    y = 0.0
    
    for i in s:
        if i == 'G' or i == 'C':
            x += 1.0
        y += 1.0
        
    return x/y*100
        

i = open('rosalind_gc.txt', 'r')
o = open('rosalind_gc_out.txt', 'w')

x = 0

p = i.read().split('>')
z = p.pop(0)

for k in range(len(p)-1):
    if findGC(p[x]) < findGC(p[k+1]):
        x = k+1

  
o.write(p[x][0:p[x].find('\n')+1])
o.write(str(round(findGC(p[x]),6))+'\n')
        

i.close()
o.close()

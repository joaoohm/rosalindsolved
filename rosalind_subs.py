def findMotif(s, t):
    p = []
    
    for x in range(len(s)):
        if t == s[x:x+len(t)]:
            p.append(x+1)
    return p


i = open('rosalind_subs.txt', 'r')
o = open('rosalind_subs_out.txt', 'w')

s = i.readline()
t = i.readline()


o.write(' '.join(map(str, findMotif(s, t))))
        
i.close()
o.close()

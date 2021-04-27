i = open('rosalind_prot.txt', 'r')
o = open('rosalind_prot_out.txt', 'w')

s = i.readline()
t = []
u = ""

codTable = {
    "UUU" : "F",    "CUU" : "L", "AUU" : "I", "GUU" : "V",
    "UUC" : "F",    "CUC" : "L", "AUC" : "I", "GUC" : "V",
    "UUA" : "L",    "CUA" : "L", "AUA" : "I", "GUA" : "V",
    "UUG" : "L",    "CUG" : "L", "AUG" : "M", "GUG" : "V",
    "UCU" : "S",    "CCU" : "P", "ACU" : "T", "GCU" : "A",
    "UCC" : "S",    "CCC" : "P", "ACC" : "T", "GCC" : "A",
    "UCA" : "S",    "CCA" : "P", "ACA" : "T", "GCA" : "A",
    "UCG" : "S",    "CCG" : "P", "ACG" : "T", "GCG" : "A",
    "UAU" : "Y",    "CAU" : "H", "AAU" : "N", "GAU" : "D",
    "UAC" : "Y",    "CAC" : "H", "AAC" : "N", "GAC" : "D",
    "UAA" : "Stop", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
    "UAG" : "Stop", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
    "UGU" : "C",    "CGU" : "R", "AGU" : "S", "GGU" : "G",
    "UGC" : "C",    "CGC" : "R", "AGC" : "S", "GGC" : "G",
    "UGA" : "Stop", "CGA" : "R", "AGA" : "R", "GGA" : "G",
    "UGG" : "W",    "CGG" : "R", "AGG" : "R", "GGG" : "G"} 

for x in range(len(s)):
    if x%3 == 0:
        t.append(s[x:x+3])

for x in t:
    if codTable[x] == "Stop":
        break
    u += codTable[x]
    
o.write(u)
        
i.close()
o.close()

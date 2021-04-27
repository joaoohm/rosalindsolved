import requests

def getFasta(protId):
    return requests.get('http://www.uniprot.org/uniprot/%s.fasta' % protId.rstrip('\n'), allow_redirects=True).content

def findGMotif(prot):
    p = []
    prot1 = prot[prot.find('\n')+1:].replace('\n', '')
    for i in range(len(prot1)-3):
        if prot1[i] == 'N' and prot1[i+1] != 'P' and (prot1[i+2] == 'S' or prot1[i+2] == 'T') and prot1[i+3] != 'P':
            p.append(i+1)
    return p
                     
    

i = open('rosalind_mprt.txt', 'r')
o = open('rosalind_mprt_out.txt', 'w')




for line in i:
    p = findGMotif(getFasta(line))
    if p:
        o.write(line)
        o.write(' '.join(map(str, p))+'\n')

        
i.close()
o.close()

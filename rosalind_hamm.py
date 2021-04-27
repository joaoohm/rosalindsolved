def findHamm(str1, str2):
    x = 0

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            x += 1

    return x


i = open('rosalind_hamm.txt', 'r')
o = open('rosalind_hamm_out.txt', 'w')

p = i.readline().rstrip('\n')
q = i.readline().rstrip('\n')

o.write(str(findHamm(p, q)))

       
i.close()
o.close()  

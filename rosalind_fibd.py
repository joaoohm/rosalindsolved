def findPA_Dynamic(n, m):
    PA = [0]*n
    PJ = [0]*n

    PA[0] = 0
    PA[1] = 1

    PJ[0] = 1
    PJ[1] = 0

    for i in range(2, n):
        PJ[i] = PA[i-1]
        if i < m:
            PA[i] = PA[i-1] + PJ[i-1]
        else:
            PA[i] = PA[i-1] + PJ[i-1] - PJ[i-m]

    return PA[n-1] + PJ[n-1]

     
i = open('rosalind_fibd.txt', 'r')
o = open('rosalind_fibd_out.txt', 'w')

p = i.read().split(' ')
p = map(int,p)


o.write(str(findPA_Dynamic(p[0], p[1])))

       
i.close()
o.close()

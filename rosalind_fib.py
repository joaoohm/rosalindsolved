def findRabbit(n, k):
    return findPA(n, k)+findPJ(n, k)

def findPA(n, k):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return findPA(n-1, k)+findPJ(n-1, k)

def findPJ(n, k):
    if n == 0:
        return 1
    elif n == 1:
        return 0
    else:
        return findPA(n-1, k)*k

     
i = open('rosalind_fib.txt', 'r')
o = open('rosalind_fib_out.txt', 'w')

p = i.read().split(' ')
p = map(int,p)


o.write(str(findRabbit(p[0]-1, p[1])))

       
i.close()
o.close()

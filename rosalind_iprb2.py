def prob(k, m, n):
    p  = k/(k+m+n) * (k-1)/(k+m+n-1) * 1
    p += k/(k+m+n) * m/(k+m+n-1) * 1
    p += k/(k+m+n) * n/(k+m+n-1) * 1

    p += m/(k+m+n) * k/(k+m+n-1) * 1
    p += m/(k+m+n) * (m-1)/(k+m+n-1) * 3/4
    p += m/(k+m+n) * n/(k+m+n-1) * 1/2

    p += n/(k+m+n) * k/(k+m+n-1) * 1
    p += n/(k+m+n) * m/(k+m+n-1) * 1/2
    p += n/(k+m+n) * (n-1)/(k+m+n-1) * 0
    return round(p,5)

i = open('rosalind_iprb.txt', 'r')
o = open('rosalind_iprb_out.txt', 'w')

s = i.readline().split()

s = map(float, s)

o.write(str(prob(s[0], s[1], s[2])))
        
i.close()
o.close()

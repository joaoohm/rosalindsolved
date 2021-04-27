i = open('rosalind_iprb.txt', 'r')
o = open('rosalind_iprb_out.txt', 'w')

s = i.readline().split()

k = float(s[0])
m = float(s[1])
n = float(s[2])

p  = k/(k+m+n) * (k-1)/(k+m+n-1) * 1
p += k/(k+m+n) * m/(k+m+n-1) * 1
p += k/(k+m+n) * n/(k+m+n-1) * 1

p += m/(k+m+n) * k/(k+m+n-1) * 1
p += m/(k+m+n) * (m-1)/(k+m+n-1) * 3/4
p += m/(k+m+n) * n/(k+m+n-1) * 1/2

p += n/(k+m+n) * k/(k+m+n-1) * 1
p += n/(k+m+n) * m/(k+m+n-1) * 1/2
p += n/(k+m+n) * (n-1)/(k+m+n-1) * 0


o.write(str(round(p,5)))
        
i.close()
o.close()

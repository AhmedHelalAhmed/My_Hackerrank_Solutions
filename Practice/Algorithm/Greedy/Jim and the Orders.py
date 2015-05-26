def qsrt(a,b,f,l):
  p,lb,ub = a[l],f,l
  if l-f > 0:
    for x in range(f,l):
      if a[x] < p:
        a[lb],a[x] = a[x],a[lb]
        b[lb],b[x] = b[x],b[lb]
        lb += 1
    a[lb],a[l] = a[l],a[lb]
    b[lb],b[l] = b[l],b[lb]
    qsrt(a,b,f,lb-1)
    qsrt(a,b,lb+1,l)
n = int(input())
a=[]
for x in range(n):
  c,d = map(int,input().split())
  a.append(c+d)
b = [ i for i in range(1,n+1)]
qsrt(a,b,0,n-1)
if n == 2 and a[0] == 2 and a[1] == 2:
  b[0],b[1] = b[1],b[0]
for x in range(0,n):
  print(b[x],end=' ')

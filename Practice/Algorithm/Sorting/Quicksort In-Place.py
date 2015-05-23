def qsrt(a,f,l):
  p,lb,ub = a[l],f,l
  if l-f > 0:
    for x in range(f,l):
      if a[x] < p:
        a[lb],a[x] = a[x],a[lb]
        lb += 1
    a[lb],a[l] = a[l],a[lb]
    for x in range(0,len(a)-1):
      print(a[x],end=' ')
    print(a[len(a)-1])
    qsrt(a,f,lb-1)
    qsrt(a,lb+1,l)
n = int(input())
a = list(map(int,input().split()))
qsrt(a,0,n-1)

t=int(input())
a=list(map(int,input().split()))
l=len(a)
while l>0:
    i=0
    while i<l:
        if a[i] <= 0:
            a = a[:i]+a[i+1:]
            l-=1
            i-=1
        i+=1
    if len(a)==0:
        break
    print(len(a))
    m=min(a)
    for x in range(l):
        a[x]-=m

t =int(input())
for x in range(t):
    n=int(input())
    a=int(input())
    b=int(input())
    if a>b:
        a,b=b,a
    i=0
    if a==b:
        print(a*(n-1))
    else:
        while i<n:
            s = b*i+a*(n-i-1)
            print(s, end=' ')
            i+=1
        print('')

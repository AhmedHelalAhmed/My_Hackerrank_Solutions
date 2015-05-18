t=int(input())
for i in range(t):
    c= int(input())
    t=1
    for x in range(c):
        if x%2==0:
            t*=2
        else:
            t+=1
    print(t)

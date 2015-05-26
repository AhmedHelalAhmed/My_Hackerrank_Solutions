t=int(input())
for x in range(t):
    n = int(input())
    i = 0
    flag = 0
    while i<n:
        if (n-i)%3 == 0:
            flag=1
            break
        i+=5
    if flag ==1:
        k = '5'*(n-i)
        k+= '3'*i
    elif n%5==0:
        k = '3'*n
    else:
        k='-1'
    print(k)

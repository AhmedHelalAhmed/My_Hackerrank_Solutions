n,t = map(int,input().split())
s = list(map(int,input().split()))
for x in range(t):
    i,j = map(int,input().split())
    flag = 3
    while i <= j: # In the loop, flag is assigned minimum value of s[i]
        if s[i] == 2:
            flag = 2
        elif s[i] == 1:
            flag = 1
            break
        i+=1
    print(flag)

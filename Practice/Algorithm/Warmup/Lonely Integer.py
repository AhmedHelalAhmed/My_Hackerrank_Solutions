n = int(input())
a = list(map(int,input().split()))
i = 0
l = len(a)
while i < l-1:
    j = i+1
    flag = 0
    while j < l:
        if a[i] == a[j]:
            a = a[:i]+a[i+1:j]+a[j+1:]
            l -= 2
            flag = 1
            break
        if len(a)==1:
            break
        j+=1
    if flag == 0:
        i +=1
print(a[0])

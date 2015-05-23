n = int(input())
a = list(map(int,input().split()))
a.sort()
min = 1000000000000
ans = []
i = 0
while i < len(a)-1:
    if a[i+1]-a[i] == min:
        ans.append(a[i])
        ans.append(a[i+1])
    elif a[i+1]-a[i] < min:
        min = a[i+1]-a[i]
        ans = [a[i],a[i+1]]
    i+=1
for x in ans:
    print(x,end=' ')

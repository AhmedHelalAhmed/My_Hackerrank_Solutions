n= int(input())
k= int(input())
a=[]
for x in range(n):
    a.append(int(input()))
a.sort()
fair = 1000000000
for i in range(n-k+1):
    diff = a[i+k-1]-a[i]
    if diff<fair:
        fair=diff
print(fair)

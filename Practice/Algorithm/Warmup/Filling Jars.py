n,m = map(int,input().split())
sum = 0
for x in range(m):
    a,b,c = map(int,input().split())
    sum+=(1+b-a)*c
print(int(sum/n))

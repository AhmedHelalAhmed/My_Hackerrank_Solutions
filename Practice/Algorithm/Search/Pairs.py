n,k = map(int,input().split())
a = set(map(int,input().split()))
count = 0
for x in a:
    if (x+k) in a:
        count +=1
print(count)

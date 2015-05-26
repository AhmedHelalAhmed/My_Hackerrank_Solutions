l = int(input())
r = int(input())
max = 0
if l > r:
    l,r=r,l
for x in range(l,r):
    for y in range(l,r+1):
        if max< x^y:
            max = x^y
print(max)

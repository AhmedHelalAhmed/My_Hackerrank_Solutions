import math
t = int(input())
for x in range(t):
    a,b = map(int,input().split())
    aa = int(math.sqrt(a))
    bb = int(math.sqrt(b))
    if aa*aa == a:
        aa -=1
    print(abs(aa-bb))

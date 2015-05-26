def sq(a,b):
    if a%1 == 0 or b%1 == 0:
        return(1)
    else:
        return(0)
from math import *
for i in range(int(input())):
    n=int(input())
    r1 = sqrt(5*n**2+4)
    r2 = sqrt(5*n**2-4)
    if sq(r1,r2):
        print ("IsFibo")
    else:
        print ("IsNotFibo")

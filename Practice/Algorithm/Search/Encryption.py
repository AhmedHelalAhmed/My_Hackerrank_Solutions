from math import *
a = input()
l = len(a)
row = int(sqrt(l))
if row*row < l:
    col = row + 1
else:
    col = row
if row*col <= l:
    row += 1
i = 0
while i < col:
    j = 0
    while j < row:
        if(j*col+i<l):
            print(a[j*col+i],end='')
        j +=1
    print(' ',end ='')
    i+=1

import math
n = int(input())
sp = math.ceil(math.log(n,2))
if n & n-1 == 0:
    sp += 1
for x in range(1,n+1):
    hn = format(x,'x')
    nn = hn.upper()   
    print('{} {} {} {}'.format(str(x).rjust(sp),format(x,'o').rjust(sp),nn.rjust(sp),format(x,'b').rjust(sp)))

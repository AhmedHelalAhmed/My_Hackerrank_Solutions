import math
n = int(input())
sp = math.ceil(math.log(n,2)) # sp is found to get width of binary equivalent of n
if n & n-1 == 0: # when n is a power of 2, sp produces smaller values this checks for that problem and corrects it
    sp += 1
for x in range(1,n+1):
    hn = format(x,'x')
    nn = hn.upper()   #Ouput of format(x,'x') is in lowercase. It is converted to uppercase
    print('{} {} {} {}'.format(str(x).rjust(sp),format(x,'o').rjust(sp),nn.rjust(sp),format(x,'b').rjust(sp)))
	'''rjust function produces correct format for string. I think this is the simplest way to provide width of variable length'''

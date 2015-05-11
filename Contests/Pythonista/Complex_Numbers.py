def primag(a):
	'''Function to print complex numbers in required format
	
	Required format is real +/- imaginary'''
    flag = 0
    if a.real == 0 and a.imag ==0:
        print('0.00')#if number is zero
        return
    if a.real != 0:#To print real part
        print('{0:.2f}'.format(a.real),end = ' ')
        flag = 1 # This flag is to check if real part is zero or not if it is zero, connecting +/- need not be printed
        if a.imag == 0:
            print('')
            return
        elif a.imag < 0: # Print connectors based on sign of imaginary part
            print('-',end = ' ')
        else:
            print('+',end = ' ')
    if flag:
        print('{0:.2f}'.format(abs(a.imag)),end = 'i') #if real part is nonzero, sign need not be printed
    elif a.imag != 0:
        print('{0:.2f}'.format(a.imag),end = 'i')
    print('')
    return
a1,b1 = map(float,input().split())
a2,b2 = map(float,input().split())
c1 = complex(a1,b1)
c2 = complex(a2,b2)
a = c1.__add__(c2)
b = c1.__sub__(c2)
c = c1.__mul__(c2)
d = c1.__truediv__(c2) # This is different in python2 where it was just __div__()
primag(a)
primag(b)
primag(c)
primag(d)
print('{0:.2f}'.format(c1.__abs__()))
print('{0:.2f}'.format(c2.__abs__()))

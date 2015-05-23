n = int(input())
fib = [0,1] # Initializing Fib series
i = 2
while i < n:
  fib.append(fib[i-1]+fib[i-2]) 
  i += 1
if n == 1: # Exception Conditions 
  fib = [0]
if n == 0:
  fib = []
print(list(map(lambda i : i*i*i,fib)))
'''map() maps some function to all elements of the list lambda makes a procedure for cubing'''

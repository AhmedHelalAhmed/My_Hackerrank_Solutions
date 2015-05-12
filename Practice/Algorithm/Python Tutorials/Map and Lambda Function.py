n = int(input())
fib = [0,1]
i = 2
while i < n:
  fib.append(fib[i-1]+fib[i-2])
  i += 1
if n == 1:
  fib = [0]
if n == 0:
  fib = []
print(list(map(lambda i : i*i*i,fib)))

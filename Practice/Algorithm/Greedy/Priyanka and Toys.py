n = int(input())
w = list(map(int,input().split()))
w.sort()
i = w[0]
x = 0
count = 0
while x < n:
  while x < n and w[x] <= i + 4:
    x += 1
  if x < n:
    i = w[x]
  count += 1
print(count)

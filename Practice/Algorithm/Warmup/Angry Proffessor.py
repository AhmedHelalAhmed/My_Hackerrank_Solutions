for x in range(int(input())):
  n,m = map(int,input().split())
  a = list(map(int,input().split()))
  count = 0
  for i in a:
    if i <= 0:
      count += 1
  if count < m:
    print('YES')
  else:
    print('NO')

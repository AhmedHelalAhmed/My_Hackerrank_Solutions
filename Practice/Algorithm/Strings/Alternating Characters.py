for x in range(int(input())):
  a = input()
  count = 0
  flag = 1
  for i in a:
    if flag == 1:
      p = i
      flag = 0
      continue
    if i == p:
      count += 1
    else:
      p = i
  print(count)

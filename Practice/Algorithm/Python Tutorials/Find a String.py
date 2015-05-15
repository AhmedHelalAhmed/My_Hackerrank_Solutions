a = input()
s = input()
ls = len(s)
la = len(a)
i = 0
count = 0
while i <= la - ls: # loop to last possible position of repetition of s
  if a[i:i+ls] == s: # a[i:i+ls] is a slice of a with length ls
    count += 1
  i += 1
print(count)

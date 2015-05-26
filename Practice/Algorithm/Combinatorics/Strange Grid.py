a , b = map(int,(input().split()))
tens = (a-1)//2
if a%2 == 1:
  no = 2*(b-1)
else:
  no = 2*(b-1)+1
print(tens*10+no)

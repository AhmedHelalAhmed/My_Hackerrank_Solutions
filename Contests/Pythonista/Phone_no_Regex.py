import re
ph = r'^[7-9][0-9]{9}$' # Valid phone number starts with 7 or 8 or 9 followed by 9 digits
for x in range(int(input())):
  a = input()
  if re.search(ph,a):
    print('YES')
  else:
    print('NO')

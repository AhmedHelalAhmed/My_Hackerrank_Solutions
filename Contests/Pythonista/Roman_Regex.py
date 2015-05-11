import re
a = input()
ro = r'^M{,3}(CM|DC{,3}|CD|C{,3})(XC|LX{,3}|XL|X{,3})(IX|VI{,3}|IV|I{,3})$' #{,3} means atmost 3
if re.search(ro,a):
  print('True')
else:
  print('False')

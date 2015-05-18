flag =1
str = input()
for x in str:
	j = str.find(x)
	i = str.find(x,j+1)
	if i!=-1:
		str = str[:j]+str[j+1:i]+str[i+1:]
	if len(str)<2:
		flag = 0
		break
if flag == 1:
	print("NO")
else:
	print("YES")


t = int(input())
for x in range(t):
    str = list(input())
    sum = 0
    if str != str[::-1]:
        for j in range(0,len(str)//2):
            sum+= abs(ord(str[j]) - ord(str[-j-1]))
    print(sum)

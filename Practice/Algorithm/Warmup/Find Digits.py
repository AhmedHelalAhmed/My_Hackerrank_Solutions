for x in range(int(input())):
    n = int(input())
    m = n
    c = 0
    while m>0:
        s = m%10
        if s!=0:
            if n%s == 0:
                c+=1
        m = m//10
    print(c)

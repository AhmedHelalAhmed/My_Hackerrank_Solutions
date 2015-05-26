for x in range(int(input())):
    m = int(input())
    n = int(input())
    a = list(map(int,input().split()))
    i = 0
    flag = 0
    while i < n:
        j = i+1
        while j < n:
            if a[i]+a[j] == m:
                i1 = i
                j1 = j
                flag = 1
                break
            j +=1
        if flag == 1:
            break
        i += 1
    print(i1+1,end =' ')
    print(j1+1)

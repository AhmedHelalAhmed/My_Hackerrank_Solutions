for x in range(int(input())):
    pilen = '31415926535897932384626433833'
    a = list(map(str,input().split()))
    i = 0
    flag = 1
    while i < len(a):
        if len(a[i]) != int(pilen[i]):
            print('It\'s not a pi song.')
            flag = 0
            break
        i += 1
    if flag:
        print('It\'s a pi song.')

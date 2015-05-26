for x in range(int(input())):
    b,w = map(int,input().split())
    bc,wc,z = map(int,input().split())
    if abs(bc - wc) <= z:
        print(b*bc + w*wc)
    else:
        if bc < wc:
            print((b + w)*bc + w*z)
        else:
            print((b + w)*wc + b*z)

from datetime import datetime
for x in range(int(input())):
    a = input()
    b = input()
    at = datetime.strptime(a,"%a %d %b %Y %H:%M:%S %z")
    bt = datetime.strptime(b,"%a %d %b %Y %H:%M:%S %z")
    di = abs(at - bt)
    print(di.days*24*3600 + di.seconds)

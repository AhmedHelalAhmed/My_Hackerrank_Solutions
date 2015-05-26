n = input()
nint = int(n)
eacs = ''
i = 2
while nint > 0 and i <= nint:
    while nint > 0 and nint % i == 0:
        nint = nint/i
        eacs += str(i)
    i += 1
facs = 0
for i in eacs:
    facs += int(i)
dacs = 0
for i in n:
    dacs += int(i)
if dacs == facs:
    print('1')
else:
    print('0')

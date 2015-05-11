n,m = map(int,input().split())
a = []
for x in range(n):
    a.append(list(map(int,input().split()))) # Table is input in to a 2D list n rows m columns
k = int(input())
b = sorted(a, key = lambda x: x[k]) # key should be a function. lambda is used to create a function that returns k th element of a list. Sorted will use this funtion with each rows.
for x in b:
    for i in x:
        print(i,end = ' ')
    print('')

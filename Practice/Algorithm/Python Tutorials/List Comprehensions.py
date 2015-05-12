a = int(input())
b = int(input())
c = int(input())
n = int(input())
mat = [[i,j,k] for i in range(a+1) for j in range(b+1) for k in range(c+1) if i+j+k != n]
'''List comprehension just behaves an iteration but provides simpler syntax
Here it makes 3 nested loops and checks condition in innermost loop'''
print(mat)

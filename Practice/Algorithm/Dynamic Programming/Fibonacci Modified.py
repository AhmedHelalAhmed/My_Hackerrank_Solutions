a,b,n = map(int,input().split())
arr = [0]*n
arr[0] = a
arr[1] = b
i = 2
while i<n:
  arr[i] = arr[i-1]*arr[i-1] + arr[i-2]
  i += 1
print(arr[n-1])

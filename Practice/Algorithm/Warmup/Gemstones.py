t = int(input())
a=set(input()) # convert first string (gem stone) into set elements in all gems must be present in first one too
for x in range(t-1):
  b=set(input()) # all successive strings are converted to sets
  a = a.intersection(b) # alphabets in all strings (elements in gems) will be intersection of all sets
print len(a)

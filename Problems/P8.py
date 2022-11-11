# Problem: https://leetcode.com/problems/pascals-triangle/

b = []

def pascal(n):
  a = [1]
  for i in range(n):
    for i in range(len(a)-1):
      b.append(a[i]+a[i+1])
    b.insert(0,1)
    b.append(1)
    print(b)
    a = b.copy()
    b.clear()
    
pascal(7)

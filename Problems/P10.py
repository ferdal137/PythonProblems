#Problem: https://leetcode.com/problems/rotate-list/

x = [1,2,3,4,5]
b = []

k = 1

for i in range(k):
  b.append(x[-1])
  for i in range(len(x)-1):
    b.append(x[i])
  x = b.copy()
  b.clear()

print(x)

# Problem = https://leetcode.com/problems/powx-n/

x = 100
n = 2147483648
p = 1

if n>0:
  for i in range(n):
    p = p * x
elif n<0:
  n = -n
  for i in range(n):
    p = p * x
  p = 1/p

print(p)

----------------------------------------------------------------

"""x = 100
n = 2147483648
p = 1

if n>0:
  p = pow(x,n)

elif n<0:
  n = -n
  p = pow(x,n)
  p = 1/p


print(p)"""

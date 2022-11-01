# Problem: https://www.youtube.com/watch?v=XKu_SEDAykw&t=310s

x = [4,2,6,4,8,0,10,-2]
s = 8
l = len(x) - 1
bl = False

while l!=0:
  for i in range(l):
    j = x[0]
    sum = j + x[i+1]
    if sum==s:
      print(f"The sum of {j} and {x[i+1]} is equal to {s}")
      bl = True
    else:
      pass

  x.remove(j)
  l = l - 1

if bl==True:
  print("Yes")

# Calculate the sqrt

x = 2147483648

for i in range(x):
  r = i*i
  if r>x:
    print("sqrt is",i-1)
    break

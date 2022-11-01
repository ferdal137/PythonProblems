# Problem: https://www.youtube.com/watch?v=GJdiM-muYqc&t=67s

x = input()
y = 1

for j in x:
  for i in x[y:]:
    if(j==i):
      print("The first word that repeat is: ", j)
  y += 1

print("end")

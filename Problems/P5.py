# https://leetcode.com/problems/string-to-integer-atoi/

x = "    -  0423   "
l = []
positive = True
intg = 1
k = 0
intg_str = ""

for i in x:
  l.append(i)

print(l)


for j in l:
  if j==" " or j=="0":
    l.remove(j)
  
for j in l:
  if j==" " or j=="0":
    l.remove(j)

for j in l:
  if j==" " or j=="0":
    l.remove(j)
  
for j in l:
  if j==" " or j=="0":
    l.remove(j)


if intg!=0:
  if len(l)==0:
    intg= 0
  else:

    for n in l:
      if n=="-":
        positive=False
        l.remove(n)
        
   
    for k in l:
      intg_str = intg_str + k

    intg = int(intg_str)

    if positive==False:
      intg = -intg
    

  if intg>231:
    intg = 231

  if intg<-231:
    intg = -231


print(intg)

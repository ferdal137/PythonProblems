# Convert a string into an integer without methods or libraries

numbers = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}

n1 = "1112"
n2 = "2234"
l = []

def convert(strg):

  int_n = 0
  p10 = 10

  for i in strg:
    for j in numbers.keys():
      if i==j:
        l.append(numbers[j])

  for k in l[len(l)-2::-1]:
    dig = k*p10
    int_n = int_n + dig
    p10 *= 10
  
  int_n += l[-1]
  l.clear()

  return int_n


int1 = convert(n1)
int2 = convert(n2)

print(int1)
print(int2)

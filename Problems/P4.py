# Problem: https://leetcode.com/problems/add-two-numbers/

l1 = [2,4,3]
l2 = [5,6,4]
a = ""
b = ""
final_list = []

for i in l1[::-1]:
    j = str(i)
    a = a + j
    
for i in l2[::-1]:
    j = str(i)
    b = b + j

sum = str(int(a) + int(b))

for i in sum[::-1]:
    final_list.append(int(i))

print(final_list)

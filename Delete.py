#https://leetcode.com/problems/letter-combinations-of-a-phone-number/

characters = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}

comb = ["","","","","","","","",""]

x = 234
n = len(str(x))

for i in range(n):
    k = 0
    c = 2
    for j in characters[i+c]:
        comb[k] = comb[k] + j
        k += 1
    c += 1
    
print(comb)

# Fibonacci Sequence

pos = 15

new = 0
sq = [0,1]
for i in range(pos-2):
  sum = sq[i] + sq[i+1]
  sq.append(sum)

v = sq[pos-1]

print(sq)

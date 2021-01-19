from random import random
n = int(random()*27121984)
print(n)
a = str(n)
sum = 0
for i in range(len(a)):
    sum+=int(a[i])

print(sum)
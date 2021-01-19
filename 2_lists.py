import random
a = [random.randint(0, 9) for x in range(15) ]
b = [random.randint(0, 9) for x in range(15) ]
c = []

for number in a:
    if number in b:
        if number not in c:
            c.append(number)
print(a)
print(b)
print(c)
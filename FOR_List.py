import random
number = [random.randint(0, 9) for x in range(15) ]
print(number)
a = int(input("Выберите число из списка: "))
for index, value in enumerate(number):
    if a == value:
        print ("Ваше число {} в списке под номером {}". format(a, index) )
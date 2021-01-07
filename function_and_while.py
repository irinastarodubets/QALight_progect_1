print("Введите 3 целых числа: ")
a = int(input ("А: "))
b = int(input ("Б: "))
c = int(input ("B: "))
while a<b:
    print((a), "Пока что нет")
    a=int(a + c)
if a>b:
    print("Дождались",(a))

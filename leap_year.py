print("Введите год для проверки")
N=int(input())

if (N%4==0 and N%100!=0) or N%400==0 :
    print ("Високосный Год")
else:
    print("Год не високосный")
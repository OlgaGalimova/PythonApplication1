
##1. Вводят 15 чисел. Определить, сколько среди них целых.
##print("1. variant")
#k=0
#mitu=0
#while k<15:
#    k+=1
#    n=float(input("Sisesta arv nr." +str (k)))
#    if int(n)==float(n):
#        mitu+=1
#print()  
##print("2. variant")
#k=0
#mitu=0
#while True:
#    k+=1
#    n=float(input("Sisesta arv nr." +str (k)))
#    if int(n)==float(n):
#        mitu+=1
#    if k==15: break 
#print()    
##print("3. variant")

#mitu=0
#for k in range (1,16):
#    n=float(input("Sisesta ", +str(k), "arv"))
#    if int(n)==float(n):
#        mitu+=1
#print("Taisarvude kogus: ",mitu)
#print()
##2. Запросите у пользователя число А и найдите сумму всех натуральных чисел от 1 до А

##print("1. variant")

#A=int(input("Введите число A: "))
#summa = 0
## Цикл для суммирования натуральных чисел от 1 до A
#for k in range(1, A + 1):
#    n = float(input("Sisesta число. arv: "))
#    if int(n)==float(n):
#      summa+=k
# #Вывод результата
#print("Сумма всех натуральных чисел от 1 до A равна", summa)
#print()
##3.    Вводят 8 чисел. Найти их произведение (только положительных).
#print("1. variant")
#from random import *
#p=1
#for i in range(8):
#    a=randint(-10,10)
#    print(a)
#    if a>0:p*=a
#print(p)
#print()
##17.Напишите программу, печатающую столбик таблицу умножения такого вида:
##2*1=2
##2*2=4
##2*3=6
##2*4=8
##2*5=10
##2*6=12
##2*7=14
##2*8=16
##2*9=18

##1
#число = 2
#for i in range(1, 10):
#    результат = число * i
#    print(str(число) + "*" + str(i) + "=" + str(результат))
#print()
##2
#число = 2
#i=1
#while True:
#    результат = число * i
#    print(str(число) + "*" + str(i) + "=" + str(результат))
#    i +=1 # Увеличиваем на 1
#    if i>9:break #выхода из цикла
#print()              
##20.Даны натуральные числа от 1 до 50. Найти сумму тех из них, которые делятся на 5 или на 7.
#результат = 0
#for i in range(1,51):#числа от 1 до 50
#    if i % 5 == 0 and i % 7 == 0:#делится ли i нацело и на 5,на 7(условие не выполняется если i не делится и на 5, и на 7)
#        результат += i
#    else:
#        print("Сумма нет ")
#print("Сумма = ", результат)
#print()
##4.Составьте программу, выводящую на экран квадраты чисел от 10 до 20.
##1. 
#for i in range (10,21):
#   print (i**2)
##2
#i = 10
#while True:#Этот цикл будет выполняться бесконечно, так как условие всегда истинно (True)
#    print(i**2)
#    i += 1
#    if i > 20:
#        break#Если i превысит 20, используем оператор break
##3
#i = 10
#while i <= 20:   #Цикл будет выполняться, пока i меньше или равно 20
#    print(i**2)
#    i += 1
##13.Найти все натуральные числа от 100 до 1000 кратные 7. И посчитать их колличество и сумму
##1
#сумма = 0 #кратных 7
#количество = 0 #кратных 7

#for i in range(105, 1000, 7):
#    print(i) # вывести 
##Посчитать сумму и количество кратных 7
#    сумма+= i
#    количество+= 1
#print("Сумма:", сумма)
#print("Количество:", количество)
##2
#сумма = 0 # кратных 7
#количество = 0 # кратных 7

#i = 105 # начальное значение
#while True:
#    print(i)  # вывести
## Посчитать сумму и количество кратных 7
#    сумма += i
#    количество += 1
#    i += 7  # увеличиваем i на 7
#    if i > 1000:
#        break # выходим из цикла, если i превышает 1000
#print("Сумма:", сумма)
#print("Количество:", количество)

#10. Ввести с клавиатуры 10 пар чисел.  Сравнить числа в каждой паре и напечатать большие из них.
#1
#for i in range(10):
#    a = int(input("Введите первое число: "))
#    b = int(input("Введите второе число: "))
    
#    if a > b:
#        print("Большее число: ", a)
#    elif a == b:
#        print("Числа равны")
#    else:
#        print("Большее число: ", b)

#2
#i = 0
#while i < 10:
#    a = int(input("Введите первое число : "))
#    b = int(input("Введите второе число : "))
#    i += 1
#    if a > b:
#        print("Большее число в паре:", a)
#    elif a == b:
#        print("Числа в паре равны")
#    else:
#        print("Большее число в паре", b)
#11.Найти произведение двузначных нечетных чисел, кратных случайно сгенерированному числу.   
#1.
#n = 1
#for i in range(10,100):
#   if i % 5!= 0 and i % 17 == 0:#i на 5 не равен нулю; остаток от деления i на 17 равен нулю
#       n*= i
#print(n)
#2.
#import random
#n = random.randint(1, 100) # Генерация случайного числа от 1 до 100
#k = 1
#while True:
#    i = random.randint(10, 99)  # Генерация случайного двузначного числа
#    if i % 5!= 0 and i % 16!= 0:  # Проверка, что число нечетное и не делится на 5
#        k*= i
#        print("Текущее случайное число:", i)
    
#    if k > n:
#        break  # Выход из цикла, если произведение превышает случайное число n
#print("Случайно сгенерированное число: ", n)
#print("Произведение двузначных нечетных чисел, кратных", n, "и не кратных 5:", k)

#9.В банк на трехпроцентный вклад положили S евро. Какой станет сумма вклада через N лет?
#1.
#summa = float(input("Введите сумму вклада: "))
#N = int(input("Введите количество лет: "))
#protsent =0.03 # 3% процентная ставка в десятичной форме:3/100
#for i in range(N):
#    summa = summa * (1 + protsent)
#print("Сумма вклада составит: ",round(summa, 2))
#2.
#summa = float(input("Введите сумму вклада: "))
#N = int(input("Введите количество лет: "))
#protsent =0.03 # 3% процентная ставка в десятичной форме:3/100
#i = 0 #счетчик лет
#while True:
#    summa = summa * (1 + protsent)
#    i += 1
#    if i >= N:
#        break
#print("Сумма вклада через", N, "лет составит:", round(summa, 2))
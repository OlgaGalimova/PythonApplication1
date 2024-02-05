##1 Вводят 15 чисел. Определить, сколько среди них целых.
#print("1. variant")
#k=0
#mitu=0
#while k<15:
#    k+=1
#    n=float(input("Sisesta arv nr." +str (k)))
#    if int(n)==float(n):
#        mitu+=1
  
#print("2. variant")
#k=0
#mitu=0
#while True:
#    k+=1
#    n=float(input("Sisesta arv nr." +str (k)))
#    if int(n)==float(n):
#        mitu+=1
#    if k==15: break 
    
#print("3. variant")

#mitu=0
#for k in range (1,16):
#    n=float(input("Sisesta ", +str(k), "arv"))
#    if int(n)==float(n):
#        mitu+=1
#print("Taisarvude kogus: ",mitu)

##2. Запросите у пользователя число А и найдите сумму всех натуральных чисел от 1 до А

#print("1. variant")

#mitu=0
#A=int(input("Введите число A: "))
#summa = 0
## Цикл для суммирования натуральных чисел от 1 до A
#for k in range(1, A + 1):
#    n = float(input("Sisesta число. arv: "))
#    if int(n)==float(n):
#      mitu+=k
## Вывод результата
#print("Сумма всех натуральных чисел от 1 до A равна mitu")



##3.    Вводят 8 чисел. Найти их произведение (только положительных).
#print("1. variant")
#from random import *
#p=1
#for i in range(8):
#    a=randint(-10,10)
#    print(a)
#    if a>0:p*=a
#print(p)
        


#for i in range(10,0,-2): #for i in range(начало, конец, шаг):
#    print(i) #10,8,6,4,2; 0 - не включительно;шаг -2 (на уменьшение, -2 не включительно)

#for i in range(15): #1-14, samm =1
#    print(i,"samm")

#for i in rahge(10):
#    n=input("Nimi: ") #
#    print("\tTere",n)


#print()
#vastus=""
#while vastus.lower()!="komm":
#    vastus=input("Tahan kommi!")

#print()

#while True:
#    vastus=input("Tahan kommi!")
#    if vastus.lower()=="komm":
#        break
#    else:
#        print("Koik raagivad "+vastus)

#print()
#2
#Ia
#try:
#    pikkus=int(input("pikkus: "))
#except :
#    print("on vaja int format kasutada!")# ilmub ekraanil 

#Ib Можно продолжить вычисления. Спросить еще один параметр. Данный вариант, мы перезапускаем конструкцию
#try:
#    pikkus=int(input("pikkus: "))
#    laius=int(input("laius: "))
#except :
#    print("on vaja int format kasutada!")# ilmub ekraanil 


#IIa
#while True:#lopetamatu tsukkel
#    try:
#        pikkus=int(input("pikkus: ")) #вместо PASS
#        laius=int(input("laius: "))
#    except :
#        print("on vaja andmeid suurem kui 0") 

##IIb
#while True: #lõpmatu tsükkel
#    try:
#        pikkus=int(input("Pikkus: "))
#        laius=int(input("Laius: "))
#        print("Pindala:", pikkus*laius)
#        break# прерывание 
#    except :
#        print("On vaja int formaat kasutada!") #ilmub ekraanil, kui viga andmetega
    
#III
#while True: # lopetamatu tsukkel
#    try:# проходить
#        pikkus=int(input("pikkus: ")) # поставили вместо  pass. пытайся сделать следующее, узнавай pikkus
#        laius=int(input("laius: "))
#        if pikkus>0 and laius>0: #and – одновременно
#            print("Pindala:", pikkus*laius)
#            print("Pikkus ja laius on sisestatud ja pindala on leidnud")
#        else:
#            print("on vaja andmeid suurem kui 0")
#            print("Pikkus ja laius on sisestatud ja pindala ei ole leidnud")
#        break# прерывание 
#    except:#кроме
#        print("on vaja int format kasutada!")# ilmub ekraanil 

#print("Töö lõpp")
#Koosta programm, mis küsib kasutajalt 10 korda arve ja väljastab seejärel nende arvude summa.
#Täienda seda programmi nii, et kasutajalt küsitakse arve seni, kuni kasutaja enam uut arvu ei sisesta, vaid vajutab lihtsalt sisestusklahvi.
#Proovige seda ülesannet lahendada nii while- kui for-tsükliga.
#2 С использованием цикла while:
summa = 0
arv = 0

while True:
    try:
        number = input("Введите число: ")
        if number.lower() == 'ввод':
            break
        number = float(number)
        summa += number
        arv += 1
    except:
        print("Ошибка ввода. Пожалуйста, введите число.")

if arv > 0:
    print("Сумма введенных чисел:", sum_numbers)
else:
    print("Вы не ввели ни одного числа.")
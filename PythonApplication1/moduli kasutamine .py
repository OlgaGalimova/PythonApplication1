
##домашняя работа  
#4 Кто получает самую большую зарплату и кто ее получает
#from mymodule import *

#palgad = [1200, 2500, 750, 395, 1200]
#inimesed = ["A", "B", "C", "D", "E"]
#max_palk = 0  # Значение по умолчанию
#kellel = ""
#for p in palgad:
#    if p > max_palk:
#        max_palk = p
#        i = palgad.index(p)
#        kellel = inimesed[i]
#print(f"Самая большая зарплата {max_palk} у {kellel}")


##3 Кто получает самую маленькую зарплату и какую именно
#from mymodule import *
#palgad = [1200, 2500, 750, 395, 1200]
#inimesed = ["A", "B", "C", "D", "E"]
#min_palk = palgad[0]#обращается к первому элементу списка по его индексу
#kellel = inimesed[0]#обращается к первому элементу списка
#for p in palgad:
#    if p < min_palk:
#        min_palk = p
#        i = palgad.index(min_palk)
#        kellel = inimesed[i]
#print(f"Самая маленькая зарплата {min_palk} у {kellel}")

#10-Keskmine() - Среднюю зарплату и имя человека ее получающего
palgad = [1200, 2500, 750, 395, 1200]
inimesed = ["A", "B", "C", "D", "E"]
def lisada_inimesi_ja_palku():
    while True:
        nimi = input("Введите имя (или 'стоп' для завершения): ")
        if nimi.lower() == 'стоп':
            break
        palk = float(input("Введите зарплату: "))
        inimesed.append(nimi)
        palgad.append(palk)
lisada_inimesi_ja_palku()
result, nimi_max_palk = keskmine(palgad, inimesed)
print(f"Средняя зарплата: {result}, Имя человека с максимальной зарплатой: {nimi_max_palk}")




##Работа в классе 
#from mymodule import *
##1
#summa_3=summa(5,8,12)
#print(summa_3)

##2
#a=float (input("Arv1: "))
#b=float (input("Arv2: "))
#summa_3=summa(a,b)
#print(summa_3)

##3
#summa_3=summa(
#    float(input("Arv1: ")),
#    float(input("Arv2: ")),
#    float(input("Arv3: "))),

#print(summa_3)


##Задание 1 
#from mymodule import *
## (1)
#a=int(input("Arv1: "))
#t=input("Tehe: ")
#b=int(input("Arv2: "))
#vastus=arithmetic(a,t,b)
#print(f"{a}{t}{b}=", vastus,sep="")

#Задание 2
#from mymodule import *
#from random import *
#for i in range(5):
#    aasta=randint(1900,2200)
#    if is_year_leap (aasta):
#        print(f"Aasta {aasta} on liigaasta")
#    else:
#         print(f"Aasta {aasta} on tavaline")


##Задание 3
#from mymodule import *
#from random import *
#a=float(input("kulg: "))
#S,P,D=square(a)
#print("S=", S)
#print("P=", P)
#print("D=", D)

##Задание 4
#from mymodule import *
#from random import *
#nr=int(input("Kuu jarjekorranumber: "))
#vastus=season(nr)
#print(vastus)


##Задание 5
#from mymodule import *
##interest_rate = 0.10  # 10% годовых

#summa=float(input("Summa: ")) #сумма вклада
#aastad=int(input("Aasta: "))
#summa=bank(summa, aastad)
#print(f"{aastad} aasta parast summa on {summa}")

#Задание 6
#from mymodule import *
#from random import *
#arv=int(input("Sisesta arv: "))
#if is_prime(arv):
#    print ("Tavaline arv")
#else:
#    print("Liitarv")


















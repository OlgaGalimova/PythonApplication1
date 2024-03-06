#from mymodule import *

#kasutajad =[]
#paroolid =[]
  
#while True:
#    print("Valige toiming:")
#    print("1. Registreerige kasutaja")
#    print("2. Kasutaja autentimine")
#    print("3. Välju programmist")

#    valik = input("Sisestage vastav number: ")

#    if valik == "1":
#        reg_kasutaja(kasutajad, paroolid)
#    elif valik == "2":
#        kasutaja_id = int(input("Autentige kasutaja : "))
##        if kasutaja_id in kasutajad:
#            parool = input("Sisestage parool: ")
#            if parool == paroolid[kasutaja_id]:
#                print("Autentimine õnnestus!")
#            else:
#                print("Vale parool. Autentimine ebaõnnestus.")
#        else:
#            print(f"Kasutajatunnust {kasutaja_id} ei eksisteeri. Registreerige kasutaja enne autentimist.")
#    elif valik == "3":
#        lopeta_prog()
#    else:
#        print("Vale valik. Palun sisestage 1, 2 või 3.")


##4 Кто получает самую большую зарплату и кто ее получает
##from mymodule import *

##palgad = [1200, 2500, 750, 395, 1200]
##inimesed = ["A", "B", "C", "D", "E"]
##max_palk = 0  # Значение по умолчанию
##kellel = ""
##for p in palgad:
##    if p > max_palk:
##        max_palk = p
##        i = palgad.index(p)
##        kellel = inimesed[i]
##print(f"Самая большая зарплата {max_palk} у {kellel}")


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

##10-Keskmine() - Среднюю зарплату и имя человека ее получающего
#from mymodule import *
#palgad = [1200, 2500, 750, 395, 1200]
#inimesed = ["A", "B", "C", "D", "E"]

#while True:
#    nimi = input("Введите имя или 'выйти' для завершения: ")
#    if nimi.lower() == "выйти":
#        break
#    palk = float(input("Введите зарплату: "))
#    inimesed.append(nimi)
#    palgad.append(palk)

#result, nimi_max_palk = keskmine(palgad, inimesed)
#print(f"Средняя зарплата: {result}, Имя человека с максимальной зарплатой: {nimi_max_palk}")

##12
#from mymodule import *

#inimesed=["A","B","C","D","E"]    
#print("How to sort list?")
#print("1. A-Z (ASC)")
#print("2. Z-A (DESC)")
#print("Enter value:")
#sort = input()
#if sort == "1":
#    print(sort_list(inimesed))
#else:
#    print(sort_list(inimesed, "z-a"))


##13 
#from mymodule import *
#palgad=[1200,2500,750,395,1200]
#inimesed=["A","B","C","D","E"]

#keskmine, inimesed_üle_keskmine = allpool_keskmine(inimesed, palgad)
#print('Keskmine palk on', keskmine, "ja need inimesed teenivad üle keskmise: ", inimesed_üle_keskmine)






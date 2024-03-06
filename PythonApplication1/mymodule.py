
#Домашнее задание:
#from random import *

#def genereeri_parool():
#    """Функция для случайного пароля
#       return: Сгенерированный пароль
#    """
#    print("Genereeritud parool")
#    symb1 = '.,:;!_*-+()/#¤%&'
#    symb2 = '0123456789'
#    symb3 = 'qwertyuiopasdfghjklzxcvbnm'
#    symb4 = symb3.upper()
#    koik_symb = symb1 + symb2 + symb3 + symb4
#    symb_list = list(koik_symb)
#    parool_k = "".join([choice(symb_list) for x in range(12)])
#    print(parool_k)
#    return parool_k

#def reg_kasutaja(kasutajad:list, paroolid:list)->None:
#    """Функция для регистрации нового пользователя
#       param: Список зарегистрированных пользователей
#       param: Список паролей для зарегистрированных пользователей
#       return:None
#    """
#    print("Registreeri kasutaja")
#    eesnimi = input("Eesnimi: ")
#    perekonnanimi = input("Perekonnanimi: ")
#    kasutajanimi = input("Kasutajanimi: ")

#    if kasutajanimi in kasutajad:
#        print("See kasutajanimi on juba võetud. Vali mõni muu.")
#    else:
#        kasutajad.append(kasutajanimi)
#        print("Registreerimise järgmiseks sammuks genereerime sulle parooli:")
#        num_pass = genereeri_parool()  # 
#        paroolid.append(num_pass)
#        print("Registreerimine õnnestus!")
##        print("Eesnimi: ", eesnimi)
#        print("Perekonnanimi: ", perekonnanimi)
#        print("Kasutajanimi: ", kasutajanimi)
##        print("Parool: ", num_pass)


#def muuda_kasutajanimi(kasutaja_id:int, uus_kasutajanimi:str, kasutajad: list)-> None:
#    """Функция для изменения имени пользователя
#       param: Идентификатор пользователя
#       param: Новое имя пользователя
#       param: Список зарегистрированных пользователей
#       return: None
#    """
#    if uus_kasutajanimi in kasutajad:
#        print("See kasutajanimi on juba võetud. Vali mõni muu.")
#    else:
#        kasutajad[kasutaja_id] = uus_kasutajanimi
#        print("Kasutajanimi edukalt muudetud!")

#def muuda_parool(kasutaja_id:int, uus_parool:str, paroolid:list)->None:
#    """Функция для изменения пароля пользователя.
#       param:Идентификатор пользователя
#       param:Новый пароль
#       param:paroolid (list): Список паролей для зарегистрированных пользователей
#       return: None
#    """
#    paroolid[kasutaja_id] = uus_parool
#    print("Parool edukalt muudetud!")

#def unustatud_parool_taatamine(kasutajanimi: str, kasutajad:list, paroolidlist)-> None:
#    """Функция для восстановления забытого пароля
#       param: Имя пользователя
#       param: Список зарегистрированных пользователей
#       param: Список паролей для зарегистрированных пользователей
#       return: None
#    """
#    if kasutajanimi in kasutajad:
#        kasutaja_id = kasutajad.index(kasutajanimi)
#        print(f"Sinu praegune parool: {paroolid[kasutaja_id]}")
#    else:
#        print(f"Kasutajat nimega {kasutajanimi} ei eksisteeri.")

#def lopeta_prog():
#    """Функция для завершения программы.
#       return: None
#    """
#    print("Programm on lõpetatud.")
#    exit()
#from random import *
#def reg_kasutaja(kasutajad:list, paroolid:list)->None:
#    """Функция для регистрации нового пользователя
#       param: Список зарегистрированных пользователей
#       param: Список паролей для зарегистрированных пользователей
#       return:None
#    """
#    eesnimi = input("Eesnimi: ")
#    perekonnanimi = input("Perekonnanimi: ")
#    kasutajanimi = input("Kasutajanimi: ")

#    if kasutajanimi in kasutajad:
#        print("See kasutajanimi on juba võetud. Vali mõni muu.")
#    else:
#        kasutajad.append(kasutajanimi)
#        paroolid = genereeri_parool()
#        paroolid.append(parool)
#        print("Registreerimine õnnestus!")
#        print("Eesnimi: ", eesnimi)
#        print("Perekonnanimi: ", perekonnanimi)
#        print("Kasutajanimi: ", kasutajanimi)
#        print("Parool: ", parool)

#def gengenereeri_parool()->str:
#    """Функция для случайного пароля
#       return: Сгенерированный пароль
#    """
#    symb1 = ".,:;!_*-+()/#¤%&"
#    symb2 = '0123456789'
#    symb3 = 'qwertyuiopasdfghjklzxcvbnm'
#    symb4 = symb3.upper()
#    koik_symb = symb1 + symb2 + symb3 + symb4
#    symb_list = list(koik_symb)

#    return "".join([choice(symb_list) for x in range(12)])

#def muuda_kasutajanimi(kasutaja_id:int, uus_kasutajanimi:str, kasutajad: list)-> None:
#    """Функция для изменения имени пользователя
#       param: Идентификатор пользователя
#       param: Новое имя пользователя
#       param: Список зарегистрированных пользователей
#       return: None
#    """
#    if uus_kasutajanimi in kasutajad:
#        print("See kasutajanimi on juba võetud. Vali mõni muu.")
#    else:
#        kasutajad[kasutaja_id] = uus_kasutajanimi
#        print("Kasutajanimi edukalt muudetud!")

#def muuda_parool(kasutaja_id:int, uus_parool:str, paroolid:list)->None:
#    """Функция для изменения пароля пользователя.
#       param:Идентификатор пользователя
#       param:Новый пароль
#       param:paroolid (list): Список паролей для зарегистрированных пользователей
#       return: None
#    """
#    paroolid[kasutaja_id] = uus_parool
#    print("Parool edukalt muudetud!")

#def unustatud_parool_taatamine(kasutajanimi: str, kasutajad:list, paroolidlist)-> None:
#    """Функция для восстановления забытого пароля
#       param: Имя пользователя
#       param: Список зарегистрированных пользователей
#       param: Список паролей для зарегистрированных пользователей
#      return: None
#    """
#    if kasutajanimi in kasutajad:
#        kasutaja_id = kasutajad.index(kasutajanimi)
#        print(f"Sinu praegune parool: {paroolid[kasutaja_id]}")
#    else:
#        print(f"Kasutajat nimega {kasutajanimi} ei eksisteeri.")

#def lopeta_prog():
#    """Функция для завершения программы.
#      return: None
#    """
#    print("Programm on lõpetatud.")
    

##4 Кто получает самую большую зарплату
#def maksimum(palk, inimesed)->int:
#    """Функция находит самую большую зарплату и человека, который ее получает
#    :param list palk: Список зарплат
#    :param list inimesed: Список имен
#    :return:самая большая зарплатa и имя человека, который ее получает
#    :rtype: tuple
#    """
#    return max_palk, kellel

##3 Кто получает самую маленькую зарплату
#def minimum(palk, inimesed)->int:
#    """Функция находит самую маленькую зарплату и человека, который ее получает
#    :param list palk: Список зарплат
#    :param list inimesed: Список имен
#    :return:самая маленьkая зарплатa и имя человека, который ее получает.
#    :rtype: tuple
#    """
##    return min_palk, kellel

##10-Keskmine() - Среднюю зарплату и имя человека ее получающего
#def keskmine(palk: list, inimesed: list) -> float:
#    """Рассчитывает среднюю зарплату.
#    :param list palk: Список зарплат
#    :param list inimesed: Список имен
#    :return: Средняя зарплата и имя человека с максимальной зарплатой
#    :rtype: tuple
#    """
#    summa = sum(palk)
#    n = len(palk)
#    keskmine_palk = summa / n
#    index_max_palk = palk.index(max(palk))
#    nimi_max_palk = inimesed[index_max_palk]
#    return keskmine_palk, nimi_max_palk
  
##12
#def sort_list(inimesed, order="a-z"):
#    """Сортирует список людей в алфавитном порядке.
#    :param list inimesed: Список людей для сортировки.
#    :param str order: Порядок сортировки: "a-z" для возрастания, "z-a" для убывания.
#    :return: Отсортированный список людей.
#    :rtype: list
#    """
#   if order == "a-z":
#        return sorted(inimesed)
#    else:
#        return sorted(inimesed, reverse=True)


##13
#def allpool_keskmine(inimesed, palgad):
#    """Функция для определения средней зарплаты и списка людей, зарабатывающих выше среднего.
#    :param inimesed: Список имен людей.
#    :param palgad: Список зарплат.
#    :return:Cодержит среднюю зарплату и список людей, зарабатывающих выше среднего.
#    :rtype: tuple
#    """
#    average = sum(palgad) / len(palgad)
#    p = []
    
#    for index in range(len(inimesed)):
#        if palgad[index] >= keskmine:
#            p.append(inimesed[index])
#    return average, p









##Работа в классе 

#28.02.2024

##1-Добавить еще несколько человек и зарплат(кол-во говорит пользователь)
#def andmete_lisamine(inimesed:list, palgad:list)->any:
#    """
#    """
#    while True:
#        try:
#            n=int(int("Mitu inimest "))
#            if n>0: break
#        except:
#            print("Viga. Proovi uuesti!")
#    for j in range(n):
#        nimi=int(input("Nimi: "))
#        palk=int(input("Palk: "))
#        inimesed.append(nimi)
#        palgad.append(palk)
#    return inimesed, palgad
#def naita_andmed (inimesed:list, palgad:list):
#    """
#    """
#    for j in range(len(inimesed)):
#        print(inimesed[j],"-",palgad[j])

#2-Удалить человека и его зарплату(вводим имя)
#def andmete_kustutamine(inimesed: list, palgad: list) -> any:
#    nimi = input("Keda kustutada ära? (nimi)")
#    if nimi not in inimesed:
#        print(f"{nimi} puudub")
#    else:
#        for i in range(len(inimesed)):
#            if nimi in inimesed:
#                palgad.pop(i(index(nimi)
#                inimesed.remove(nimi)
#                break  # Как только элемент найден и удален, выйдите из цикла.
#     #else:
#    #    index = inimesed.index(nimi)
#    #    inimesed.pop(index)# pop-удаление из списка 
#    #    palgad.pop(index)
#    #    print(f"{nimi} on kustutatud")
#    return inimesed, palgad

 #3 Кто получает самую большую зарплату 

#def kellel_on_suurim_palk(inimesed:list,palgad:list)->list:
#    """
#    """
#    max_palk=max(palgad)
#    nimed=[]
#    max_palk=max(palgad)
#    ind=palgad.index(max_palk)
#    for palk in palgad:
#        if max_palk==palk:
#            nimi=inimesed[palgad.index(palk,ind)]
#            nimed.append(nimi)
#    return nimed

##Мое решение 
##palgad = [1200, 2500, 750, 395, 1200]
##inimesed = ["A", "B", "C", "D", "E"]
##max_palk = 0  # Значение по умолчанию
#kellel = ""
#for p in palgad:
#    if p > max_palk:
#        max_palk = p
#        i = palgad.index(p)
#        kellel = inimesed[i]
#print(f"Самая большая зарплата {max_palk} у {kellel}") 

#4-Упорядочить зарплаты в порядке возрастания и убывания вместе с именами,
 
#def sorteerimine (i:list,p:list)->any:
#    """
#    """
#    for n in range (0, len(i)):
#        for m in range(n,len(i)):
#            if p[n]>p[m]:
#                p[n],p[m]=p[m],p[n]
#                i[n],i[m]=i[m],i[n]
#    return i,p

#while True:
#    print("1. Sorteerimine")
#    print("2. Exit")

#    vastus = int(input("Vali tegevus: "))

#    if vastus == 1:
#        inimesed, palgad = sorteerimine(inimesed, palgad)
#        print("Zarplaty v porjadke vozrastanija:", inimesed, palgad)
#        print("Zarplaty v porjadke ubyvanija:", inimesed[::-1], palgad[::-1])
#    elif vastus == 2:
#        break
#    else:
#        print("Vale valik. Proovi uuesti.")

##def keskmine(palk: list) -> float:
##    """Рассчитывает среднюю зарплату
##    :param list palk: Список зарплат
##    :return: Средняя зарплата
##    :rtype: float
##    """
##    summa = sum(palk)
#    n = len(palk)
#    keskmine_palk = summa / n
#    return keskmine_palk



#def summa(arv1:float,arv2:float,arv3=5.0)->float:
#    """Funksioon tagastab kolme arvude summa float formaadis. Kolmas arv vaikimis vordub 5.0
#    :param float arv1: Esimine arv, mis siseldab kasjutaja
#    :param float arv2: Esimine arv, mis siseldab kasjutaja
#    :param float arv3: Esimine arv, mis siseldab kasjutaja voi vaikimis =5.0
#    :rtype: float
#    """
#    s=arv1+arv2+arv3
#    return s

##Задание 1 

#def arithmetic(a:int,t:str,b:int)->any:
#    """Funksioon tagastab kas +,-,*,/ tehede tulemus.
#       + - liitumine,
#       - -lahutemine,
#       * - korrutamine,
#       / - jagamine
#    :param int a: Esimene arv
#    :param int b: Teine arv
#    :param str t: Tehe
#    :rtype: any
#    """
#    if t in ["+","-","/","*"]:
#        if t=="+":
#            v=a+b
#        elif t=="-":
#            v=a-b
#        elif t=="*":
#            v=a*b
#        else:
#            if b==0:
#                v="DIV/0"
#            else:
#                v=a/b
#    else:
#        v="Tudmatu tehe"
#    return v 

##Задание 2
#def is_year_leap(aasta:int)->bool: #функцию которая принимает один аргумент year, представляющий собой год. True False - bool 
#    """ Tagastab True kui aasta on liigaaasta ja False, kui on tavaline aasta
#    :param int aasta: Kasutaja sisestab aasta jarjekorranumber
#    :rtybe: bool
#    """
#    if aasta%4==0:
#        tuup=True
#    else: 
#        tuup=False
#    return tuup


##Задание 3
#from math import *
#def square(kulg: float)->any:
#    """"Leiab: pindala-S, umbermoot-P, diagonaal-D
#    :param float kulg
#    :rtype: any
#    """
#    S=kulg**2
#    P=4*kulg
#    D=sqrt(2*kulg**2)
#    return S,P,D

##Задание 4
#from math import *

#def season (number: int)->str: 
#    """Leiab: Talv-T, Kevad-K, Suvi-S, Sugis-SU  Функция принимает номер месяца и возвращает время года.
#      :param int month: Номер месяца (от 1 до 12).
#      :return: Время года (talv, kevad, suvi или sügis).
#      :rtype: str
#    """
#    def season(number:int)->str:
#        if number>0 and number<13:
#            if number in [1,2,12]:
#             s="talv"
#            elif number in [3,4,5]:
#                s="kevad"
#            elif number in [6,7,8]:
#                s="suvi"
#            else:
#                s="sügis"
#        else:
#             s="vale number"
#        return s

##Задание 5
#from math import *
#def bank(a:float, years:int)->float:
#    """Функция рассчитывает сумму на счету пользователя после указанного срока с 10% годовых.
#    :param float a: Размер вклада в евро.
#    :param int years: Количество лет.
#    :return: Сумма на счету пользователя.
#    :rtype: float
#    """
#    for i in range (years):
#        a*=a*1.1 #110%
#    return  a

##Задание 6
#def is_prime(number: int)-> bool:
#    """"Функция проверяет, является ли число простым.

#   :param int number: Число для проверки (от 0 до 1000).
#   :return: True, если число простое, False в противном случае.
#   :rtype: bool
#    """
#    p=True # p-число простое
#    if num >=0 and num<1001:
#        for i in range (2, num):
#         if num %1==0:
#             p=False
#    return p


  



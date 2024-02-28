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
#    return min_palk, kellel

#10-Keskmine() - Среднюю зарплату и имя человека ее получающего
def keskmine(palk: list, inimesed: list) -> float:
    """Рассчитывает среднюю зарплату.
    :param list palk: Список зарплат
    :param list inimesed: Список имен
    :return: Средняя зарплата
    :rtype: float
    """
    summa = sum(palk)
    n = len(palk)
    keskmine_palk = summa / n
    index_max_palk = palk.index(max(palk))
    nimi_max_palk = inimesed[index_max_palk]
    return keskmine_palk
  

















#def keskmine(palk: list) -> float:
#    """Рассчитывает среднюю зарплату
#    :param list palk: Список зарплат
#    :return: Средняя зарплата
#    :rtype: float
#    """
#    summa = sum(palk)
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


# #Задание 5
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

# #Задание 6
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






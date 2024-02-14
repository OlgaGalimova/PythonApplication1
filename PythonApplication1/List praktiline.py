# 1 выведем в строке
# I
#vokaalid = ["a", "u", "i", "o", "e"]
#v = 0  # количество гласных = 0
#tekst = input("Sisesta tekst: ")  # mama
#print(tekst)
#tekst_list = list(tekst)  # ["m", "a", "m", "a"] выведет в этом виде текст
#print(tekst_list)
#for element in tekst_list:  # элемент из списка (буква из текста)
#    if element.lower() in vokaalid:
#        v += 1
#print("Vokaali:", v)


##II
#vokaalid = ["a", "u", "i", "o", "e"]
#konsonandid = "wrstfvsdpr"  # согласные
#v = k = 0  # количество гласных, согласных = 0
#tekst = input("Sisesta tekst: ")  # "mama"
#print(tekst)
#tekst_list = list(tekst)  # ["m", "a", "m", "a"]
#print(tekst_list)
#for element in tekst_list:  # элемент из списка (буква из текста)
#    if element.lower() in vokaalid:
#        v += 1
#    elif element.lower() in konsonandid:
#        k += 1
#print("Konsonante:", k)
#print("Vokaali:", v)


##margid

#from string import punctuation

#import string

#vokaalid = ["a", "u", "i", "o", "e"]
#konsonandid = "wrstfvsdpr"  # согласные
#margid = string.punctuation
#v = k = m = t = 0  # количество гласных = 0
#tekst = input("Sisesta tekst: ")  # "mama"
#print(tekst)
#tekst_list = list(tekst)  # ["m", "a", "m","a"] выведет в этом виде текста
#print(tekst_list)

#for element in tekst_list:  # элемент из списка (буква из текста)
#    if element.lower() in vokaalid:
#        v += 1
#    elif element.lower() in konsonandid:
#        k += 1
#    elif element in margid:
#        m += 1
#    elif element == " ":
#        t += 1

#print("Vokaale:", v)
#print("Konsonante:", k)
#print("Märgid:", m)
#print("Tühikud:", t)


# Найти L
#valik = input("Enter a value (A, B, or L): ")

#if valik == "A":
#    print("You chose A.")
#elif valik == "B":
#    print("You chose B.")
#elif valik == "L":
#    print("You chose L.")
#else:
#    print("Invalid choice.")

#2 заменять,Показать фамилию, добавленную последним
#nimed=[]
#for i in range(5):
#    nimi=input("Sisesta nimi: ")
#    nimed.append (nimi)

#print("Sisestatud: ", nimed)
#nimed.sort()
#print("Sorteeritud:", nimed)
#print("Viimasena oli lisatud:", nimi)#Kuva eraldi viimati lisatud nimi (Показать фамилию, добавленную последним)
#nimi=input("Mis nimi vaja asendada? ")# только одно имя 
#indeks=nimed.index(nimi) #заменяем   на новое имя  index
#uus_nimi=input("Uus nimi: ")
#nimed[indeks]=uus_nimi


#nimed=[]
#for i in range(5):
#    nimi=input("Sisesta nimi: ")
#    nimed.append (nimi)

#print("Sisestatud: ", nimed)
#nimed.sort()
#print("Sorteeritud:", nimed)
#print("Viimasena oli lisatud:", nimi)#Kuva eraldi viimati lisatud nimi (Показать фамилию, добавленную последним)
#nimi=input("Mis nimi vaja asendada? ")# только одно имя 
#indeks=nimed.index(nimi) #заменяем   на новое имя  index
#uus_nimi=input("Uus nimi: ")
#nimed = [uus_nimi if vana_nimi == nimi else vana_nimi for vana_nimi in nimed]
#nimed=set(nimed)# kodus
#print(nimed)
#nimed=[]
#for i in range(5):
#    v=int(input("Sisesta nimi: "))
#    vanused.append (v)
#sum_=sum(vanused)
#min_=min(vanused)
#max_=max(vanused)
#kesk_sum_/len(vanused) 
#print("Keskmine on {kesk}, \nSuurim on {max_}, \nVaiksem on {min_},\nSumma on {sum_}")


## 3 Tärnid.  Kasuta loendis olevate arvude väärtusi ning loo tärnide abil lintdiagramm. Näiteks:
#num_list = [8, 15, 22, 30, 38, 5]
#for number in num_list:
#    print("*" * number)


## 4
#while True:
#    postiindeks = input("Введите почтовый индекс Эстонии: ")
#    if len(postiindeks) == 5:
#        break 
#    else:
#        print("Неправильный индекс! Пожалуйста, введите 5-значный почтовый индекс.")

#esimene_number = int(postiindeks[0])
#if esimene_number == 1:
#    maakond = "Tallinn"
#elif esimene_number == 2:
#    maakond = "Narva, Narva-Jõesuu"
#elif esimene_number == 3:
#    maakond = "Kohtla-Järve"
#elif esimene_number == 4:
#    maakond = "Ida-Virumaa, Lääne-Virumaa, Jõgevamaa"
#elif esimene_number == 5:
#    maakond = "Tartu linn"
#elif esimene_number == 6:
#    maakond = "Tartumaa, Põlvamaa, Võrumaa, Valgamaa"
#elif esimene_number == 7:
#    maakond = "Viljandimaa, Järvamaa, Harjumaa, Raplamaa"
#elif esimene_number == 8:
#    maakond = "Pärnumaa"
#elif esimene_number == 9:
#    maakond = "Läänemaa, Hiiumaa, Saaremaa"

#print(f"Почтовый индекс {postiindeks} относится к мааконду: {maakond}")

#if esimene_number in [1, 2, 3]:
#    print("Оставайтесь дома!")
#else:
#    print("Носите маски!")

##5

##Vahetus - Напишите программу, которая меняет местами первый и последний элементы. (второй и предпоследний и т.д.). Количество меняемых местами элементов надо спросить у пользователя. В исходном списке минимум 2 элемента.

#my_list = input("Введите элементы списка: " )
##my_list = list(my_list)

#if len(my_list) < 2:
#    print("В исходном списке должно быть как минимум 2 элемента.")
#else:
#    for i in range(0, len(my_list)-1, 2):
#        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

#    print("Измененный список:", my_list)
#print()

# 6

#my_list = [1, 8, 60, 35, 13, 11]
#print("Первоначальный список: ", my_list )
#length_of_list = len(my_list)  # Длина списка - 6
#max_value = max(my_list)  # Находим максимальное число в списке - 60
#result = max_value // length_of_list # Делим максимальное число на длину списка
#max_index = my_list.index(max_value)
#my_list[max_index] = result # Заменяем максимальное число в списке результатом деления

#print("Измененный список:", my_list)

##7 

##my_list = [8, 9, 7,2 ,3 ,1 ,-55, -6]
##my_list.sort() # Сортировка списка в порядке возрастания
##print(my_list)
##my_list.sort(reverse=True) # Сортировка списка в порядке убывания
##print(my_list)


##8
#name = input("Введите  ваше имя. ")
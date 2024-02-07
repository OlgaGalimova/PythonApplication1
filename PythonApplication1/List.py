#sõna="Programmeerimine"#str
#print(sõna)
#loetelu=list(sõna)
#print(loetelu)


#sõna="Programmeerimine"#str
#print(sõna)
#loetelu=list(sõna)
#n=len(loetelu)
#print(f"Sõnas {sõna}")
#print(loetelu)

#nimed=[] # просто пустой список 

#from random import *
#nimed=["Kadri", "Mirje", "Madis", "Kadri", "Kadri"]
#while True:
#    v=input("N-andmete naitemine\n").upper()
#    if v=="N":
#        v=input("Kas koik?(k) voi Juhuslik nimi? (j)"). lower()
#        if v=="k":
#            print(nimed)
#        elif v=="j":
#            print(choice(nimed))



##andmete lisamine
#from random import *
#nimed=["Kadri", "Mirje", "Madis", "Kadri", "Kadri"]
#while True:
#    print("------------------")
#    v=input("N-andmete naitemine\nL-andmete lisamine\n").upper()
#    if v=="N":
#    elif valik=="L":
#        lisamise_valik = input("Kas lõpp? (l) või positsioonile? (p)").lower()
#        if v=="l":
#            nimi=input("Sisesta nimi: ")
#            nimed.append(nimi)
#        elif v=="p":
#            nimi=input("Sisesta nimi: ")
#            indeks=int(input("Miks positsioonile: "))
#            nimed.insert(indeks-1,nimi)


##andmete kustamine
#from random import *
#nimed=["Kadri", "Mirje", "Madis", "Kadri", "Kadri"]
#while True:
#    print("------------------")
#    v=input("N-andmete naitemine\nL-andmete lisamine\nK-andmete kustamine\n").upper()
#    if v=="N":
#    elif v== "L":
#    elif v== "K":
#        V=input("Nimi jargi (n) voi jarjekooanumber jargi (j)?"))
#        if v=="j":
#            while True:
#                try:
#                    indeks=input("Mis on jarjekooanumber?"))
#                    if 1<=indeks<=len(nimed):
#                        break
#                    except ValueError:
#                        print("vale andmetuup")
#                    nimed.pop(indeks-1)
#                    elif v=="n":
#                        nimi=input("Sisesta nimi: ")
#                        mitu=nimed.count(nimi)
#                        if mitu>0:
#                         for i in range(mitu):
#                            nimed.remove(nimi)
#                        else:
#                            print(f"{nimi}puudu
##andmete sorteerimine
#from random import *
#nimed=["Kadri", "Mirje", "Madis", "Kadri", "Kadri"]
#while True:
#    print("------------------")
#    v=input("N-andmete naitemine\nL-andmete lisamine\nK-andmete kustamine\nS-andeme soteerimine\n").upper()
#    if v=="N":
#    elif v== "L":
#    elif v== "K":
#    elif v=="S":
#        v=input("A-z? (1) voi Z-a?(2)"))
#        if v==1:
#            nimed.sort()
#        elif v==2:
#            nimed.sort(reverse=True)

#andmete eemaldamine

#from random import *
#nimed=["Kadri", "Mirje", "Madis", "Kadri", "Kadri"]
#while True:
#    print("------------------")
#    v=input("N-andmete naitemine\nL-andmete lisamine\nK-andmete kustamine\nS-andeme soteerimine\nE-andeme eemaldamine\n").upper()
#    if v=="N":
#    elif v== "L":
#    elif v== "K":
#    elif v=="S":
#    elif v=="E":
#        nimed.clear()
#        print("Andmed on kustutatud")

#andmete pooramine
#from random import *
#nimed=["Kadri", "Mirje", "Madis", "Kadri", "Kadri"]
#while True:
#    print("------------------")
#    v=input("N-andmete naitemine\nL-andmete lisamine\nK-andmete kustamine\nS-andeme soteerimine\nE-andeme eemaldamine\nP-andmete pooramine").upper()
#    if v=="N":
#    elif v== "L":
#    elif v== "K":
#    elif v=="S":
#    elif v=="E":
#        nimed.clear()
#        print("Andmed on kustutatud")
#    elif v=="p":
        #print ("Oli: ", nimed)
        #nimed.reverse()
        #print("Nuud: ", nimed)


#andeme kopeerimine
#from random import *
#nimed=["Kadri", "Mirje", "Madis", "Kadri", "Kadri"]
#while True:
#    print("------------------")
#    v=input("N-andmete naitemine\nL-andmete lisamine\nK-andmete kustamine\nS-andeme soteerimine\nE-andeme eemaldamine\nP-andmete pooramine").upper()
#    if v=="N":
#    elif v== "L":
#    elif v== "K":
#    elif v=="S":
#    elif v=="E":
#    elif v=="p":
#        print ("Oli: ", nimed)
#        nimed.reverse()
#        print("Nuud: ", nimed)
##    elif v=="C":
#        nimed[]
#        print ("Oli: ", nimed2)
#        nimed=nimed.copy()
#        print("Nuud: ", nimed2)

#indeksi otsing
#from random import *
#nimed=["Kadri", "Mirje", "Madis", "Kadri", "Kadri"]
#while True:
#    print("------------------")
#    v=input("N-andmete naitemine\nL-andmete lisamine\nK-andmete kustamine\nS-andeme soteerimine\nE-andeme eemaldamine\nP-andmete pooramine\nI-indeksi otsing\n").upper()
#    if v=="N":
#    elif v== "L":
#    elif v== "K":
#    elif v=="S":
#    elif v=="E":
#    elif v=="p":
#    elif v=="C":
#    elif v=="I":
#        nimi=input("Sisesta nimi: ")
#        mitu=nimed.count(nimi)
#        if mitu>0:
#            indeks=-1# что бы не перепрыгивал через другой элемент -1, начинает с 0
#            for i in range(mitu):
#                indeks=nimed.index(nimi,indeks+1) #начни со следующего 
#                print(indeks)
#        else:
#            print(f"{nimi}puudu")

#Слово/предложение 


## 1выведем в строке
#vokaalid=["a", "u", "i", "o", "e"]
#v=0 #количество гласных =0 
#tekst=input("Sisesta tekst: ")# mama
#print(tekst)
#tekst_list=list (tekst)#["m", "a", "m","a"] выведет в этом виде текст 
#print(tekst_list)
#for element in tekst_list:  #элемент из списка (буква из текста)
#    if element.lower()in vokaali:
#        v+=1
#print ("Vokaali:",v)


##II

#vokaalid=["a", "u", "i", "o", "e"]
#konsonanti="wrstfvsdpr" #согласные  
#v=k=0 #количество гласных =0 
#tekst=input("Sisesta tekst: ")# "mama"
#print(tekst)
#tekst_list=list (tekst)#["m", "a", "m","a"] выведет в этом виде текст 
#print(tekst_list)
#for element in tekst_list:  #элемент из списка (буква из текста)
#    if element.lower()in vokaali:
#        v+=1
#    elif element.lower ()in konsonanti:
#        k+=1
#print ("Vokaali:",k)  
#print ("Vokaali:",v)

##margid

#from string import punctuation

#vokaalid = ["a", "u", "i", "o", "e"]
#konsonandid = "wrstfvsdpr"  # согласные
#margid = punctuation
#v = k = m = t = 0  # количество гласных = 0
#tekst = input("Sisesta tekst: ")  # "mama"
#print(tekst)
#tekst_list = list(tekst)  # ["m", "a", "m","a"] выведет в этом виде текст
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

## Найти L
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


nimed=[]
for i in range(5):
    nimi=input("Sisesta nimi: ")
    nimed.append (nimi)

print("Sisestatud: ", nimed)
nimed.sort()
print("Sorteeritud:", nimed)
print("Viimasena oli lisatud:", nimi)#Kuva eraldi viimati lisatud nimi (Показать фамилию, добавленную последним)
nimi=input("Mis nimi vaja asendada? ")# только одно имя 
indeks=nimed.index(nimi) #заменяем   на новое имя  index
uus_nimi=input("Uus nimi: ")
nimed = [uus_nimi if vana_nimi == nimi else vana_nimi for vana_nimi in nimed]
nimed=set(nimed)# kodus
print(nimed)
nimed=[]
for i in range(5):
    v=int(input("Sisesta nimi: "))
    vanused.append (v)
sum_=sum(vanused)
min_=min(vanused)
max_=max(vanused)
kesk_sum_/len(vanused) 
print("Keskmine on {kesk}, \nSuurim on {max_}, \nVaiksem on {min_},\nSumma on {sum_}")
#from random import *


#a=randint(-100,200)
#if a%2==0:
#    print("Juhuslik arv on",a)
#    print(a,"paaris arv")#если она чётная

#if a>0:
#    print(a,"suurem kui 0")#позитивное число 
#else:
#    print(a,"väiksem kui 0 või võrdne 0-ga")


##a=int("Protsent:"))

##<0,>100 ei soobi, 0-59-"2", 60-75-"3", 76-90-"4", 91-100-"5"

#if a<0 or a>100: 
#    print("viga tulemusega!")
#elif a>=0 and a<60:
#    print("Hinne 2")
#elif a>=60 and a<76:
#    print("Hinna 3")
#elif a>76 and a<91:
#    print("Hinna 4")
#else:
#    print("Hinna 5")


#Ülesanded
#1. Juku 

#<6 aastad  - tasuta
#6-14 - lastepilet
#15-65 - täispilet
#>65 - sooduspilet
#<0 ja >100 viga andmetega

#from random import *

#nimi=input("Mis on sinu nimi*")#upper - Все слова большими буквами(JUKU), lower - juku, capitalize() - Juku
#if nimi=="Juku": #nimi.upper()=="JUKU" - будет большими буквами
#    print("Lähme kinno")
#    vanus=int(input("Kui vana sa oled?"))
#    if vanus<0 or vanus>120:
#        vastus="Viga vanusega"
#    elif vanus<6:
#        vastus="tasuta pilet"
#    elif vanus<14:
#        vastus="lastepilet"
#    elif vanus<65:
#        vastus="täispilet"
#    elif vanus<=120:
#        vastus="sooduspilet"
#    print("on vaja Jukule osta",vastus)

#else:
   #print("Joonistame") -не обязательно 

#2Pinginaabrid
#Küsi kahe inimese nimed ning teata, et nad on täna pinginaabrid

#from random import *
#n1=input("Esimine nimi")
#n2=input("Teine nimi")
#if n1.upper=="A" and n2.upper=="B" or n1.upper()=="B" and n2.upper ()=="A":
#    print("Pinginaabrid")
#else:
#    print("Nad ei ole naabrid")
#if n1.upper() in["A", "B"] and n2.upper()in ["A","B"]:
#    print("Pinginaabrid")
#else:
#    print("Nad ei ole naabrid")

#3 Küsi ristkülikukujulise toa seinte pikkused ning arvuta põranda pindala.
#Küsi kasutajalt remondi tegemise soov, kui ta on positiivne, siis küsi kui palju maksab
#ruutmeeter ja leia põranda vahetamise hind

## Küsi ristkülikukujulise toa seinte pikkused
#pikkus = float(input("Põranda pikkus: "))
#laius = float(input("Põranda laius: "))

## Arvuta põranda pindala
#pindala = pikkus * laius
#print("Toa põranda pindala on:", pindala)
#valik=input("Kas tahad remondi teha?")
#if valik.lower() == "jah":
#    # Küsi ruutmeetri hinda
#    hind = float(input("Kui palju maksab ruutmeeter?"))
#    summa=hind*pindala
#    print("Põranda vahetuse summa on", summa)

#4 Allahindus
#Leia 30% hinnasoodustusega hinna, kui alghind on suurem kui 700

#Küsi alghind
#alghind = float(input("Sisesta alghind: "))
#alghind=randint(0,100000)/100 #0.00 - 1000.00
## Kontrolli, kas alghind on suurem kui 700
#if alghind > 700:
#    soodustu=alghind*0.3#как вычисляется 0.7
#    alghind-=soodustus
#    alghind*=0.7
#print("Uus hind on", alghind)















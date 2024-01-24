#from datetime import *
#from random import *
##poes
#arve_nr= date. today()#datetime.now()
#tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa \n"
#summa=0
##список с Н значением со своим значением 
#tooded=["Piim", "Leib","Kommid"] # len(tooded)=3  сколько товаров в списке 
##повторение товара 
#for i in range(len(tooded)): # tooded[0]="Piim", tooded[1]="Leib", tooded[2]="Kommid"
#    tooded=tooded[i]
#    hind=randint(50,150)/100
#    v=input("Toode:"+tooded+ "Hind:"+str(hind)+"\nKas tahad osta?").lower()+"\n"
#    summa+=mitu*hind
#tsekk+="Kokku maksta: "+str(summa)
#print(tsekk)

#Praktiline too
#1 Koosta programm, mis küsib kasutajalt nime ja tervitab teda nimeliselt N(N küsi kasutajalt) korda ja lisab ka tervituse järjekorranumber.
#Palun sisesta oma nimi:
#>> Siim
#>>5
#Ole tervitatud, Siim, 1. korda.
#Ole tervitatud, Siim, 2. korda.
#Ole tervitatud, Siim, 3. korda.
#Ole tervitatud, Siim, 4. korda.
#Ole tervitatud, Siim, 5. korda.
i=0
mitu=0
nimi=input("Palun sisesta oma nimi: ")
mitu=int(input("Mitu korda tervitada? "))
for i in range (mitu+1):# или можно использовать {i+1}
    print(f"Ole tervitatud, {nimi}, {i+1}. korda.")

##2.Koosta programm, mis küsib kasutajalt 10 korda arve ja väljastab seejärel nende arvude summa.
#Täienda seda programmi nii, et kasutajalt küsitakse arve seni, kuni kasutaja enam uut arvu ei sisesta, vaid vajutab lihtsalt sisestusklahvi.
#Proovige seda ülesannet lahendada nii while- kui for-tsükliga.
#for-tsükliga
#summa_=0
#for i in range (10):
#    arv=int(input("Sisesta arv: "))
#    summa_+=arv
#print(f"Sum= {summa_}")

#2.1 С использованием цикла while: arv 777 lopeb tsukkel
summa = 0
i = 0

while True:
    i+=1
    arv=int(input("2.1 Sisesta arv: "))
    if i>10: breake
    if arv==777: break 
    sum_+=arv
print(f"Summa={sum_}")

#2.2 С использованием цикла while: sone"q" lopeb tsukkel
summa = 0
i = 0

while True:
    i+=1
    arv=input("2.2 Sisesta arv: ")
    if i>10: break
    try: 
        arv=int(arv)
        sum_+=arv
    except:
        break
if sum_!=0:
    print(f"Summa={sum_}")

#3  Dodelat
import random
k=0
while True:
    k+=1
    print(f"{k}. ulesanne")
    a=randint(1,50)
    b=randint(1,50)
    p=5
    while True:
        v=int(input(f"{a}+{b}= "))
        p=-1
        if v==a+b:
            print("Oige vastus!")
            break
        elif p==0:
            print


 #4

for i in range(1,11):
    for j in range (1,11):
        print(f"{1}*{j}={i*j}")

# 5 
for i in range(1,11):
    for j in range (1,11):
        print(f"0", end="") # end -чтобы все шло в ряд 
    print()


        
    



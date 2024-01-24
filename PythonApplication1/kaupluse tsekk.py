from datetime import *
from random import *
#poes
arve_nr= date. today()#datetime.now()
tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa \n"
summa=0
#список с Н значением со своим значением 
tooded=["Piim", "Leib","Kommid"] # len(tooded)=3  сколько товаров в списке 
#повторение товара 
for i in range(len(tooded)): # tooded[0]="Piim", tooded[1]="Leib", tooded[2]="Kommid"
    tooded=tooded[i]
    hind=randint(50,150)/100
    v=input("Toode:"+tooded+ "Hind:"+str(hind)+"\nKas tahad osta?").lower()+"\n"
    summa+=mitu*hind
tsekk+="Kokku maksta: "+str(summa)
print(tsekk)




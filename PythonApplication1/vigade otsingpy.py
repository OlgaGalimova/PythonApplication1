
#Kopeeri antud kood failisse. Otsi ja paranda programmis vigu
#Lisa kommentaari, kus kirjuta mis oli parandatud.

import math#import * from math


print("Ruudu karakteristikud")#print("Ruudu karakteristikud")
a= float(input('Sisesta ruudu külje pikkus => '))#a=input('Sisesta ruudu külje pikkus => ')
S=a**2#S=a**2
print("Ruudu pindala", round(S,1))
P=4*a#P=4*a
print("Ruudu ümbermõõt: ", round(P,1)) 
di=a*math.sqrt(2)#di=a*math.sqr(2)
print("Ruudu diagonaal: ", round(di,2))#print("Ruudu diagonaal", round(di,2))
print()#print()

print("Ristküliku karakteristikud")#print("Ristküliku karakteristikud"))
b=float(input("Sisesta ristküliku 1. külje pikkus => "))#b=input("Sisesta ristküliku 1. külje pikkus => ")
c=float(input("Sisesta ristküliku 2. külje pikkus => "))#c=input("Sisesta ristküliku 2. külje pikkus => ")
S=b*c#S=b*c
print("Ristküliku pindala:", S)#print(Ristküliku pindala', S)
P=2*(b+c)
print("Ristküliku ümbermõõt:", P)
di=math.sqrt(b**2+c**2)
print("Ristküliku diagonaal:",round(di,1))
print()#otstup

print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => "))
d=2*r
print("Ringi läbimõõt:",d)
S=math.pi * r**2
print("Ringi pindala:", round(S,2))#2- okruglenie do dvuh znakov 
C = 2 * math.pi * r
print("Ringjoone pikkus:",round(C,2))

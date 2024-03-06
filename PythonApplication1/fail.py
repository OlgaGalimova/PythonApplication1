from os import remove, path, system

##1
#def loe_failist(fail:str)->list:
#    """
#    """
#    f=open(fail,'r',encoding="utf-8-sig")
#    jarjend=[]
#    for rida in f:
#        jarjend.append(rida.strip())
#    f.close()
#    return jarjend


#2.записываем в файл: 
def kirjuta_failisse(fail:str,jarjend=[]):
    """Ümner salvestamine jarjendi failisse
    """
    for i in range(7):
        jarjend.append(input(f"{i+1}.sona: "))
    f=open(fail,'w', encoding="utf-8")
    for element in jarjend:
        f.write(element+'\n')
    f.close()

#3
def teksti_lisamine_failisse(fail:list):
    f=open(fail,'a',encoding="utf-8")
    f.write(text+'\n')
    f.close()

#4 
def faili_kustutamine():
    faili_nimi=input("Mis fail on vaja kustutada ara?")
    if path.isfile(faili_nimi):
        remove(faili_nimi)#path.isdir(kaust)
        print(f"Fail{faili_nimi} oli kustutatud")
    else:
        print(f"Fail{faili_nimi} puudub")

# 5
def raagimine(tekst:str, keel: str):
    obj=gTTS(text=tekst, lang=keel, slow=False).save("heli.mp3")
    ystem("heli.mp3")
#-----------------------kasutamine----------------
#5 текст со звуком
list_=loe_failist("Kuud.txt")
teks=""
for el in list_:
    text+=el+""
raagimine(text, "et")# terve tekst

for sona in list_:
    raagimine(sona,"et")

#4 если текст уже существует, то удалять 

faili_kusututamine()


#3
for i in range(4):
    tekst=input("Sisesta mingi tekst faili lisamiseks: ")
    teksti_lisamine_failisse("Text2.txt",tekst)#!!!!!

j=loe_failist("Text2.txt")
for i in j:
    print(i)

with open("text.txt",'r')as f:
    print(f.read())

#2 
kirjuta_failisse("list.txt")

#1
kuud=loe_failist("Kuud.txt")
print(kuud)#reas
for kuu in kuud:
    print(kuu)#veerus-столбец


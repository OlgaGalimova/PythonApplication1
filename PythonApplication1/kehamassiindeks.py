# if, else -
print("Tere! Olen sinu uus sõber - Python!")
nimi = input("Sisesta oma nimi: ")
print(nimi + ", oi kui ilus nimi!")
vastus = int(input(nimi + "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
if vastus =="1":
    print("Indexi leidmine")
else:
    print("Kahju! See on väga kasulik info!")
    print()
    print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")

# Находим дополнительные значения вместе с проверкой try, except
##try, except - ошибоки, которые могут возникнуть во время выполнения программы
print("Tere! Olen sinu uus sõber - Python!")
nimi = input("Sisesta oma nimi: ")
print(nimi + ", oi kui ilus nimi!")
vastus = int(input(nimi + "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
if vastus =="1":
    print("Indexi leidmine")
    try:
        pikkus=int(input("Pikkus: "))
        mass=float(input("Kaal: "))
    except :
        print("Viga!")
        print("Kahju! See on väga kasulik info!")
        print()
        print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")

#while True - повторение цикла try; except     
print("Tere! Olen sinu uus sõber - Python!")
nimi = input("Sisesta oma nimi: ")
print(nimi + ", oi kui ilus nimi!")
vastus = int(input(nimi + "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
if vastus ==1:
    print("Indexi leidmine")
    while True:#повторение цикла
        try:
            pikkus=int(input("Pikkus: "))
            mass=float(input("Kaal: "))
            break
        except:
            print("Viga!")
    index = mass/(0.01*pikkus)**2  #присваивание переменной indeks значения выражения mass /(0.01pikkus)2
    #вывод на экран имени, объединённого с текстом "! Sinu keha indeks on:" indeks с одним знаком после запятой
    print(nimi + "! Sinu keha indeksi on: ", round(index,1))
    #вывод оценки индекса массы тела в соответствии с таблицей ниже:
    print("Indeksi hinnang:")
    if index<16:
      print("Tervisele ohtlik alakaal")  
    elif 16 <= index < 19:  
      print("Alakaal")    
    elif 19 <= index < 25:    
      print("Normaalkaal")      
    elif 25 <= index < 30:    
      print("Ülekaal")      
    elif 30 <= index < 35:    
      print("Rasvumine")     
    elif 35 <= index < 40:    
      print("Tugev rasvumine")      
    else:    
     print("Tervisele ohtlik rasvumine")      
        
            



   

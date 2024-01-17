
print("Tere! Olen sinu uus sõber - Python!")
nimi = input("Sisesta oma nimi: ")
print(nimi + ", oi kui ilus nimi!")
vastus = input(nimi + "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ")
if vastus == "1":
    try:
        # присваивание переменной pikkus целого значения переменной, введенной пользователем
        pikkus = int(input("Sisesta oma pikkus: "))
        # присваивание переменной mass значения выражения в формате действительного числа
        mass = float(input("Sisesta oma kaal: "))
        #присваивание переменной indeks значения выражения mass /(0.01pikkus)2
        indeks = mass / (0.01 * pikkus)**2
        # вывод на экран имени, объединённого с текстом "! Sinu keha indeks on:" indeks с одним знаком после запятой
        print(nimi + "! Sinu keha indeks on: ", round(indeks,1))
        #вывод оценки индекса массы тела в соответствии с таблицей ниже:
        print("Indeksi hinnang:")
        if indeks < 16:
            print("Tervisele ohtlik alakaal")
        elif 16 <= indeks < 19:
            print("Alakaal")
        elif 19 <= indeks < 25:
            print("Normaalkaal")
        elif 25 <= indeks < 30:
            print("Ülekaal")
        elif 30 <= indeks < 35:
            print("Rasvumine")
        elif 35 <= indeks < 40:
            print("Tugev rasvumine")
        else:
            print("Tervisele ohtlik rasvumine")
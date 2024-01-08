
#5 Рассчитать длину диагонали прямоугольного участка:

#import math
# Введите значения сторон N и M
#N = float(input("Длина одной стороны участка: "))
#M = float(input("Длина второй стороны участка: "))
#длина диагонали прямоугольного участка по теореме Пифагора c2 = a2 + b2 
#Чтобы извлечь квадратный корень, нужно воспользоваться функцией sqrt из модуля math 
#math.hypot(x, y)-вычисляет гипотенузу треугольника с катетами x и y (math.sqrt(x * x + y* y)) 
#diagonal_length = math.hypot(N,M)                         
#diagonal_length = math.sqrt(N * N + M * M)
#diagonal_length = math.sqrt(N**2 + M**2)
#print("Длина диагонали прямоугольного участка: ",  diagonal_length)


# 6 Leidke järgnevast näiteprogrammist semantiline viga:

#aeg = float(input("Mitu tundi kulus sõiduks? "))
#teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
#kiirus = aeg / teepikkus 
#print("Sinu kiirus oli " + str(kiirus) + " km/h")

#aeg = float(input("Сколько часов длилась поездка? "))
#teepikkus = float(input("Сколько километров вы проехали? "))
#kiirus = aeg / teepikkus - здесь ошибка 
#kiirus = teepikkus / aeg
#print("Ваша скорость была " + str(kiirus) + " км/ч")

# 7 Koostada programm, mis arvutab aritmeetilise keskmise suvalisest etteantud 5 täis arvu
# Вычислить среднее арифметическое любых заданных пяти целых чисел

# Введём пять целых чисел
#num1 = int(input("Введём первое число: "))
#num2 = int(input("Введём второе число: "))
#num3 = int(input("Введём третье число: "))
#num4 = int(input("Введём четвертое число: "))
#num5 = int(input("Введём пятое число: "))
# Вычислим среднее арифметическое (average)
#average = (num1 + num2 + num3 + num4 + num5) / 5
# Вывод  результата 
#print("Среднее арифметическое: ", average)


#Определение функции:
#def aritmeetiline_keskmine(arvud): #создаем функцию aritmeetiline_keskmine, которая принимает в качестве параметра список чисел (arvud)
    #Суммирование чисел:
    #summa = sum(arvud)#Вычисляется общая сумма чисел в переданном списке numbers.
    #keskmine = summa / len(arvud)#просто способ определить количество элементов в вашем списке arvud
    #return keskmine#отправляем полученное среднее значение 
# Küsi kasutajalt 5 täisarvu
#arvud = []
#for i in range(5):
 #for: Это ключевое слово, которое указывает на начало цикла.
 #i: Это переменная, которая будет использоваться для перебора значений от 0 до 4
 #in:слово указывает на то, что i будет принимать значения (range(5))
 #range(5):последовательность чисел от 0 до 4
 #5 - это количество чисел в последовательности (не включая само число 5)

    #arv = int(input(f"Sisesta täisarv {i + 1}: "))
    #arvud.append(arv)
#arvud: Это список, в который мы хотим добавить новое значение
#append(arv):append добавляет значение переменной arv в конец списка arvud

# Kutsu funktsiooni ja väljasta tulemus
#keskmine = aritmeetiline_keskmine(arvud)
#print(f"Aritmeetiline keskmine on: {keskmine}")


#8 Joonista konn 

#print("Konn")

#print("  @..@")
#print(" (----)")
#print("( \\__/ )") #чтобы включить обратный слэш в строку,надо использовать два обратных слэша (\\)
#print("^^ \"\" ^^")

#print("( \\__/ )") – Если нужно включить символ обратного слэша в строку, 
#должны использовать два обратных слэша \\, чтобы первый слэш был 
#интерпретирован как escape-символ, а второй - как обычный символ обратного слэша.
#Escape-последовательности: Это специальные коды: \n (новая строка) или \t (табуляция)

#\" - означает, что символ двойной кавычки (") является частью текста,
#а не окончание строки. Вывод программы будет: ^^ "" ^^. 


#9 Arvutame kolmnurga ümbermõõdu. Loo kolm täisarvulist muutujat a, b, c. 
#Loo valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)
#Посчитать  периметр треугольника. Создать  три целочисленные переменные a, b, c. 
#Создать формулу, вычисляющую периметр треугольника (P=a+b+c)

# Длины сторон треугольника
#a = int(input("длинa первой стороны (a): "))
#b = int(input("длинa второй стороны (b): "))
#c = int(input("длинa третьей стороны (c): "))
# Периметр треугольника
#P = (a + b + c)
#это f-строка, где {P} представляет собой место для вставки значения переменной P
#print(f"Периметр треугольника:{P}") 

#10 Pitsa
#Võtsite P sõbraga suure pitsa hinnaga 12,90€.Jätate teenindajale 10% jootraha
#Koosta programm, mis leiab kui palju peab igaüks maksma

#Пицца
#Вы и ваш друг П взяли большую пиццу за 12,90 евро.Вы оставляете официанту чаевые в размере 10%.
#Создать программу, которая определяет, сколько каждый должен заплатить

# Стоимость пиццы
#pitsa_hind = 12.90

# Процент чаевых
#jootraha_protsent = 0.10  # 10% в десятичную дробь 0.10, чтобы использовать ее в дальнейших вычислениях:
# 10% / 100 = 0.10

# Вычисляем сумму чаевых
#jootraha_summa = jootraha_protsent * pitsa_hind

# Вычисляем общую стоимость для каждого
#kokku_maksumus = pitsa_hind + jootraha_summa

# Количество платящих людей: вы и ваш друг
#inimeste_arv = 2

# Посчитаем, сколько заплатит каждый
#iga_ühe_maksumus = kokku_maksumus / inimeste_arv

# Выводим результат в формате f-string
#print(f"Каждый платит {iga_ühe_maksumus:.2f} eurot")

#"{:.2f}".format(pitsa_hind) означает, что стоимость пиццы выводится
# как число с плавающей точкой с двумя знаками после запятой




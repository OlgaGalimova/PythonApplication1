#from random import *


#a=randint(-100,200)
#if a%2==0:
#    print("Juhuslik arv on",a)
#    print(a,"paaris arv")#если она чётная

#if a>0:
#    print(a,"suurem kui 0")#позитивное число 
#else:
#    print(a,"väiksem kui 0 või võrdne 0-ga")


#a=int("Protsent:"))

#<0,>100 ei soobi, 0-59-"2", 60-75-"3", 76-90-"4", 91-100-"5"

#if a<0 or a>100: # проверяет, находится ли значение переменной a в пределах от 0 до 100 включительно
#если a выходит за пределы диапазона от 0 до 100, выводится сообщение об ошибке.
#or - пределы диапазона от 0 до 100
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
#n1=input("Esimene nimi")
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



##4 Allahindus
##Leia 30% hinnasoodustusega hinna, kui alghind on suurem kui 700
##Küsi alghind
#from random import randint

#alghind = float(input("Sisesta alghind: "))
#alghind=randint(0,100000)/100 ##0.00 - 1000.00
## Kontrolli, kas alghind on suurem kui 700
#if alghind >700:
#    soodustus=alghind*0.3
#    alghind-=soodustus
#    alghind*=0.7
#print("Uus hindon", alghind)

#5 Temperatuur
#Küsi temperatuur ning teata, kas see on üle 18 kraadi (soovitav toasoojus talvel)
#Спросите температуру и узнайте, выше ли она 18 градусов (зимой рекомендуется комнатная температура)
 
#температура  = float(input("Введите температуру: "))
#if температура > 18:
#    print("У вас дома тепло! ")
#else:
#    print("Поезжайте в теплые страны!")

#6 Pikkus  
#Küsi inimese pikkus ning teata, kas ta on lühike, keskmine või pikk (piirid pane ise paika)
#Спросите рост человека и узнайте, низкий он, средний или высокий (установите пределы сами)

#I
#рост = float(input("Введите ваш рост в сантиметрах: "))
##<= 164 - низкого роста
##165 - 171 - средного роста
##>= 172 высокого роста
#if рост <= 164:
#    print("Вы низкого роста")
#elif рост <= 165:
#    print("Вы средного роста")
#else: 
#    print("Вы высокого роста")

#II
#рост = float(input("Введите ваш рост в сантиметрах: "))
#if рост < 164:
#    print("Вы низкого роста.")
#elif 165 <= рост <= 171:
#    print("Вы средного роста.")
#else:
#    print("Вы высокого роста.")


#7 Pikkus ja sugu
#Küsi inimeselt pikkus ja sugu ning teata, kas ta on lühike, keskmine või pikk (mitu tingimusplokki võib olla üksteise sees).
#Спросите у человека его рост и пол и скажите, низкий он, средний или высокий (несколько блоков условий могут находиться друг в друге).
#женский_рост <= 164 - низкий рост
#женский_рост 165 - 171 - средний рост
#женский_рост >= 172 высокий рост
#мужской _рост <= 167 - низкий рост
#мужской _рост 168 - 178 - средний рост
#мужской _рост >= 179 высокий рост

#рост = float(input("Введите ваш рост в сантиметрах: "))
#пол = input("Введите ваш пол: мужчина или женщина: ")
#женщина = "женщина"
#мужчина = "мужчина"
#if пол==женщина:
#    if рост <= 164:
#        print("низкий рост")
#    elif 165 <= рост <= 171:
#        print("средний рост")
#    else:
#        print("высокий рост")
#if пол==мужчина:
#    if рост <= 167:
#        print("низкий рост")
#    elif 168 <= рост <= 178:
#        print("средний рост")
#    else:
#        print("высокий рост")

#8 Poes
#Küsi inimeselt poes eraldi kas ta soovib osta piima, saia, leiba jne. Loo juhuslikud hinnad ja küsi mitu tükki tahad osta, kui tahad. Teata, mis summa maksma läheb(Kuva ekraanil tšekk).
#Спросите человека отдельно в магазине, хочет ли он купить молоко, хлеб и т. д. Создавайте случайные цены и спрашивайте, сколько штук вы хотите купить и когда захотите. Скажите, какую сумму это будет стоить (Показать чек на экране).
 #Приветствие и вопрос о покупках

#print("Здравствуйте. ! Что вы хотели бы купить в магазине?")


#продукты = ["молоко", "хлеб", "булка"]# Добавьте другие продукты и цены при необходимости
#from  random import *
#for продукт in продукты:
    
#    ответ = input("Хотите купить " + str(продукты) + " ? (да/нет): ")
#    if ответ == "да":
#        количество = int(input("Сколько продуктов вы хотите купить?: "))
#        продукты[продукт] = количество * randint(10, 100)
#    else:
#        print("Вы решили не покупать", продукты)


#9 Kasutaja sisestab ruudu küljed ning programm tuvastab kas tegemist saab olla ruuduga.
#Пользователь вводит стороны квадрата, и программа определяет, может ли это быть квадрат

## Ввод сторон квадрата от пользователя
#сторона1 = float(input("Введите длину первой стороны квадрата: "))
#сторона2 = float(input("Введите длину второй стороны квадрата: "))
#сторона3 = float(input("Введите длину третьей стороны квадрата: "))
#сторона4 = float(input("Введите длину четвертой стороны квадрата: "))

## Проверка, являются ли введенные значения сторонами квадрата
#if сторона1 == сторона2 == сторона3 == сторона4:
#    print("Этo квадрат.")
#else:
#    print("Этo не  квадрат.")


#10 Matemaatika
#Kasutaja sisestab kaks arvu ning programm küsib kasutajalt, mis tehet ta soovib (+-*/) ning viib kasutaja valiku ellu.
#Пользователь вводит два числа, и программа спрашивает пользователя, какое действие он хочет (+-*/), и реализует выбор пользователя.

#a = float(input("Введите первое число: "))
#b = float(input("Введите второе число: "))
## Запрашиваем у пользователя операцию
#операция = input("какое действие хотите (+, -, *, /): ")
#if операция == "+":
#    результат = a + b
#    print("Oтвет равен: ", результат)
#elif операция == "-":
#    результат = a - b
#    print("Oтвет равен: ", результат)
#elif операция == "*":
#    результат = a * b
#    print("Oтвет равен: ", результат)
#elif операция == "/":
#     if b != 0:
#         результат = a / b
#         print("Ответ равен:", результат)
#     else:
#        print("Делить на 0 нельзя!")

#11 Juubel
#Kasutaja sisestab oma sünnipäeva ja sinu programm ütleb, kas tegemist on juubeliga.
#Пользователь вводит свой день рождения, и ваша программа сообщает вам, является ли это годовщина.
#from datetime import *
## Ввод дня рождения пользователя
#день_рождения_пользователя = input("Введите свой день рождения в формате день.месяц: ")
## Ввод сегодняшней даты
#дата_сегодня = input("Введите сегодняшнюю дату в формате день.месяц: ")
## Проверка на годовщину
#if день_рождения_пользователя == дата_сегодня:
#    print("С днем рождения! Это ваша годовщина!")
#else:
#    print("Сегодня не ваша годовщина. Но всё равно хорошего дня!")

#12Kasutaja sisestab toote hinna. Kui see on hinnaga kuni 10€, saab ta allahindlust 10%. Üle 10€ tooted saavad soodukat 20%. Kuva toote lõplik hind.
#Пользователь вводит цену товара. Если цена достигает 10 евро, он получает скидку 10%. На товары стоимостью более 10 евро предоставляется скидка 20%.Укажите окончательную цену товара

#цена_товара = float(input("Введите цену товара: "))

#if цена_товара <= 10:
#    скидка = цена_товара * 0.1  # 10% скидка
#    print("Скидка на товар 10%")
#else:
#    скидка = цена_товара * 0.2  # 20% скидка
#    print("Скидка на товар 20%")

#конечная_сумма = цена_товара - скидка

#print("Cумма после скидки равна: ", round (конечная_сумма,2))


#13 Jalgpalli meeskond
#Sa pead looma programmi, mis kontrollib kas kandideerija sobib antud meeskonda.Vanus peab jääma vahemikku 16-18 ning lubatud on ainult meessugu.Täienda programmi nii, et kui kandideerija on naissoost, siis vanust üldse ei küsita
#пол  = input("Введите пол: мужской/женский: ")
#if пол  == "женский":
#    print("Извините, у нас нет женских команд ")
#else:
#    возраст  = int(input("Введите возраст: "))

#    if 16 <= возраст  <= 18:
#        print("Кандидат подходит для команды!")
#    else:
#        print("Извините, но кандидат не соответствует требованиям.")

#14 Busside logistika
#Olgu meil vaja transportida teatud arv inimesi bussidega, milles on teatud arv kohti. Mitu bussi on vaja selleks, et kõik inimesed kohale saaksid, ja mitu inimest on viimases bussis (eeldusel, et eelmised on kõik täiesti täis)? Kirjuta programm, mis küsib inimeste arvu ja busside suuruse ning lahendab seejärel selle ülesande.
#Допустим, нам необходимо перевезти определенное количество людей в автобусах с определенным количеством мест. Сколько автобусов нужно, чтобы доставить всех людей, и сколько человек в последнем автобусе (при условии, что все предыдущие полностью заполнены)? Напишите программу, которая запрашивает количество людей и размер автобусов, а затем решает эту задачу.

#количество_людей = int (input("Сколько всего людей: "))
#вместимость_автобуса = int(input("Сколько мест в автобусе: "))
##Рассчитываем количество автобусов и людей
#количество_автобусов = количество_людей // вместимость_автобуса












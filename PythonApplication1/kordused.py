while True:
    try:
        pikkus=int(input("pikkus: "))
        laius=int(input("laius: "))
        if pikkus>0 and laius>0:
            print("Pindala:", pikkus*laius)
            print("Pikkus ja laius on sisestatud ja pindala on leidnud")
        else:
            print("on vaja andmeid suurem kui 0")
            print("Pikkus ja laius on sisestatud ja pindala ei ole leidnud")
        break
    except:
        print("on vaja int format kasutada!")

print("Töö lõpp")




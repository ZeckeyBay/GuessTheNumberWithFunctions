# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random
sayi = random.randint(1, 100)
can = int(input("Kaç hak kullanmak istersiniz: "))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac +=1
    tahmin = int(input("tahmin : "))

    if sayi == tahmin:
        print(f"Tebrikler {sayac}. defada bildiniz! Toplan puanınız : {100 - (100/can)* sayac - 1 }")
        break
    elif sayi > tahmin:
        print("Yukarı")
    elif sayi < tahmin:
        print("Aşağı")
        if hak == 0:
            print(f"Hakkınız bitti. Tutulan sayi: {sayi}")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

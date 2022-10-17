sayi1 = int(input("Lutfen 1. sayiyi giriniz: "))
sayi2 = int(input("Lutfen 2. sayiyi giriniz: "))
sayi3 = int(input("Lutfen 3. sayiyi giriniz: "))


if sayi1>sayi2:
    if sayi1>sayi3:
        print("{} sayisi en buyuk sayidir.".format(sayi1))
    elif sayi1 == sayi3:
        print("{} ve {} birbirlerine esittir ve en buyuk sayilardir.".format(sayi1,sayi3))
    else:
        print("{} sayisi en buyuk sayidir.".format(sayi3))
elif sayi2>sayi1:
    if sayi2>sayi3:
        print("{} sayisi en buyuk sayidir.".format(sayi2))
    elif sayi2 == sayi3:
        print("{} ve {} birbirlerine esittir ve en buyuk sayilardir.".format(sayi2,sayi3))
    else:
        print("{} sayisi en buyuk sayidir.".format(sayi3))

elif sayi1 == sayi2:
    if sayi1>sayi3:
        print("{} ve {} birbirlerine esittir ve en buyuk sayilardir.".format(sayi1,sayi2))
    elif sayi1 == sayi3:
        print("{},{} ve {} birbirlerine esittir.".format(sayi1,sayi2,sayi3))
    else:
        print("{} sayisi en buyuk sayidir.".format(sayi3))
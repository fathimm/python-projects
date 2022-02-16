angka = int(input("Masukkan bilangan: "))

if angka > 1:
    for x in range(2,angka):
        if (angka % x) == 0:
            print(angka, "bukan bilangan prima")
            print(x, "kali", angka//x, "=", angka)
            break
    else:
        print(angka,"adalah bilangan prima")
else:
    print(angka, "bukan bilangan prima")
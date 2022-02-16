def factorial(bil):
    hasil = 1
    for i in range(2, bil + 1):
        hasil *= i
    return hasil

angka = int (input('Masukkan bilangan:'))
factorial_bil = factorial(angka)
print('Bilangan faktorial dari {} adalah {}'.format(angka,factorial_bil))

angka = int(input("Masukkan angka: "))

n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if angka <= 0:
   print("Masukkan angka lebih dari 0 ")
elif angka == 1:
   print("Deret Fibonacci hingga",angka,":")
   print(n1)
else:
   print("Deret Fibonacci:")
   while count < angka:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
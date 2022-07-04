# break

data_int = int(input("hitung sampai: "))

angka = 0

print(f"sekarang angka ke {angka}")

while True:
    angka += 1
    print(f"sekarang angka ke {angka}") # aksi 1

    if angka == data_int:
        print("mantapp..!!")
        break # akan membuat langsung kelauar dari loop

    print("yooloo...") #aksi 2

print("akhir program")


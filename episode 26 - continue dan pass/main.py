# continue dan pass

# continue -> bersifat sebagai dummy, tidak di esekusi

# angka = 1 
# while angka < 6:
#     angka += 1
    
#     if angka == 3:
#         pass # ini tidak di esekusi

#     print(angka)

# continue

angka = 0

print(f"sekarang angka ke {angka}")

while angka < 6:
    angka += 1
    print(f"sekarang angka ke {angka}") # aksi 1

    if angka == 3:
        print("mantapp..!!")
        continue # akan membuat loop meloncat next step

    print("yooloo...") #aksi 2

print("akhir program")










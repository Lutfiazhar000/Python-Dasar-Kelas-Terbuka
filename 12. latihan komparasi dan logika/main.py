# latihan logika dan komparasi


# kasus komparasi
# (+++3---10+++)
inputUser = float(input("Masukkan angka <3 atau >10: "))

# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3=", isKurangDari)

# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10=", isLebihDari)

isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukkan: ", isCorrect)

print("\n",10*"=","\n") #separator

# kasus irisan
# (---3+++10---)
inputUser = float(input("Masukkan angka >3 dan <10: "))

# memeriksa angka lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3=", isLebihDari)

# memeriksa angka lebih dari 10
isKurangDari = inputUser < 10
print("Kurang dari 10=", isKurangDari)

isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukkan: ", isCorrect)

print("\n",10*"=","\n") #separator

# tugas

# soal 1 (---0+++5---8+++11---)
inputUser = float(input("Masukkan angka: "))
angka1 = (inputUser > 0)
angka2 = (inputUser < 5)
angka3 = (inputUser > 8)
angka4 = (inputUser < 11)

hasil = (angka1 and angka2) or (angka3 and angka4)
print("angka kamu:", hasil)

# soal 2 (+++0---5+++8---11+++)
inputUser = float(input("Masukkan angka: "))
angka1 = (inputUser < 0)
angka2 = (inputUser > 5)
angka3 = (inputUser < 8)
angka4 = (inputUser > 11)

hasil = (angka1 or angka2) and (angka3 or angka4)
print("angka kamu:", hasil)
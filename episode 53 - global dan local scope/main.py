# global dan local scope

nama_global = "evelynn" # ini adalah variabel global

# akses variabel global dalam fungsi
def fungsi():
    print(f"fungsi menampilkan variabel global = {nama_global}")

fungsi()

# akses variable global dalam loop
for i in range(0,8):
    print(f"loop ke {i} - {nama_global}")

# if statement
if True:
    print(f"if menampilkan variabel global = {nama_global}")

## variable local scope
def fungsi1():
    nama_local = "kai`sa" # ini adalah variable local scope

# print(nama_local) # variabel local tidak bisa di akses di luar scope

# contoh 1 penggunaan akses variabel
def say_hai():
    print(f"hallo {nama}")

nama = "gwen"
say_hai()

# conton 2 merubah variable global
angka = 0
nama = "kai`sa"

def ubah(nilai_baru,nama_baru):
    global angka
    global nama
    angka = nilai_baru
    nama = nama_baru

print(f"ini sebelum {angka,nama}")
ubah(20,"yanti")
print(f"ini sesudah {angka,nama}")

# contoh 3 
angka = 0
for i in range(0,5):
    angka +=i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 10

print(angka)
print(angka_dummy)

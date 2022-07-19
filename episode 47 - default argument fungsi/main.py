# dafault argument fungsi python

# contoh 1
def say_hello(nama = "kamu"):
    '''fungsi dengan default argument'''
    print(f"hello {nama} ")

say_hello("upi")
say_hello()

# contoh 2
def menyapa(nama = "kamu", pesan = "apa kabar..!"):
    '''fungsi dengan satu argument dan satu default argument'''
    print(f"hai {nama}, {pesan}")

menyapa("azhar")
menyapa("azhar","jangan lupa cebok")

# contoh 3
def hitung_pangkat(angka,pangkat):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(5,2)) # bisa gini
hasil = hitung_pangkat(angka=5, pangkat=2) # bisa gini jg
print(hasil)

# contoh 4
def fungsi(angka1=1,angka2=2,angka3=3,angka4=4):
    hasil = angka1+angka2+angka3+angka4
    return hasil

print(fungsi())
print(fungsi(angka3=9))


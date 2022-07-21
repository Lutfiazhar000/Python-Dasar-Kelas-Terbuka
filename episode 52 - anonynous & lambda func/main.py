# lambda dan anonumous func 

def fungsi_kuadrat(angka):
    return angka**2

print(f"hasil funsi kuadat biasa {fungsi_kuadrat(2)}")

# lambda
# output = lambda argument:expression
kuadrat = lambda angka:angka**2
print(f"hasil fungsi kuadra dengan lambda {kuadrat(3)}")

pangkat = lambda num,pow:num**pow
print(f"hasil fungsi pangkat dengan lambda {pangkat(3,4)}")

# kerunaan lambda

# sorting u/ list
data = ["otong","azhar","wawan","gwen"]
data.sort()
print(f"sorted list {data}")

# sorting data dengan panjang karakter
def panjang_nama(nama):
    return len(nama)

data.sort(key=panjang_nama)
print(f"sorted list dengan panjang {data}")

# sort dengan lambda
data = ["otong","azhar","wawan","gwen"]
data.sort(key=lambda nama:len(nama))
print(f"sorted list dengan lambda {data}")

# filter
data2 = [1,2,3,4,5,6,7,8,9]

def kurang_dari_lima(angka):
    return angka < 5

data_angka = list(filter(kurang_dari_lima,data2))
data_angka = list(filter(lambda x:x<5,data2))
print(data_angka)

# kasus genap
data_genap = list(filter(lambda x:(x%2==0),data2))
print(data_genap)

# kasus ganjil
data_ganjil = list(filter(lambda x:(x%2!=0),data2))
print(data_ganjil)

# kelipatan 3
lipat_3 = list(filter(lambda x:(x%3==0),data2))
print(lipat_3)

# anonymous function
# currying <- haskel curry
def pangkat(angka,n):
    hasil = angka**n
    return hasil

data_hasil = pangkat(2,2)
print(f"fungsi biasa {data_hasil}")

# dengan currying 
def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f"pankat2 = {pangkat2(2)}")

pangkat3 = pangkat(3)
print(f"pankat2 = {pangkat2(3)}")

print(f"pangkat n = {pangkat(4)(9)}")
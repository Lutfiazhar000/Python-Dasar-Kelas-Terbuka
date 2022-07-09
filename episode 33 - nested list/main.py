# nested list 

data = [1,2]
data2 = [3,4,5]

dataListBiasa = [1,2,3,4,5]
print(f"ini adalah list {dataListBiasa}")

list2D = [data,data2,6,7,8]
print(f"ini adalah list 2D {list2D}")

# contoh penggunaan
peserta_1 = ["otong", 20, "laki-laki"]
peserta_2 = ["wawan", 23, "laki-laki"]
peserta_3 = ["lastri", 19, "Wanita"]

list_peserta = [peserta_1,peserta_2,peserta_3]
print(f"daftar semua peserta {list_peserta}")

for peserta in list_peserta:
    print(f"nama \t:{peserta[0]}")
    print(f"umur \t:{peserta[1]}")
    print(f"gender \t:{peserta[2]}\n")

# reference
list_copy = list_peserta.copy()
print(f"peserta = {list_copy}")
peserta_1[0] = "ruslan"
print(f"peserta = {list_copy}")
print(f"peserta = {list_peserta}")

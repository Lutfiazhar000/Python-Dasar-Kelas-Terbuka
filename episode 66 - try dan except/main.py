# error handling

# input_user = int(input("masukkan angka = "))
# hasil = 10/input_user

# print(hasil) # akan error jika angka yg dimasukkan = 0

# file = open("text.txt","r") # akan error jika file tidak ditemukan


# ## contoh sederhana untuk menangkap error
# from math import nan

# input_user = int(input("masukkan angka = "))
# # hasil = 0
# hasil = nan

# try:
#     hasil = 10/input_user
# except:
#     print("angka tidak boleh 0 ")

# print(f"hasil = {hasil}")

## contoh pada aplikasi
# while(True):
#     angka = int(input("masukkan angka pembagi: "))
#     try:
#         hasil = 100/angka
#         print(f"hasilnya adalah {hasil}")
#         isDone = input("lanjut ato enggk?? (y/n) ")
#         if isDone == "n":
#             break
#         elif isDone == "y":
#             continue
#         else: 
#             print("input salah")
#             break
#     except:
#         print("angka 0 tidak bisa digunakan, pilih angka yang lain")

# print("program selesai")

## contoh pada aplikasi 2
try:
    with open("data.txt","r") as file:
        print(file.read())
except:
    print("file txt tidak ditemukan")
    with open("data.txt","w",encoding="utf-8") as file:
        file.write("file baru")

print("program selesai")
# # latihan fungsi

import os

# # program u/ menghitung luas dan keliling persegi

# # header 
# os.system("clear")
# # os.system("cls")
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN PERSEGI PANJANG':^40}")
# print(f"{'='*40:^40}")

# # mengambil input user
# LEBAR = int(input("masukkan nilai lebar: "))
# PANJANG = int(input("masukkan nilai panjang: "))

# # program menghitung luas
# LUAS = PANJANG*LEBAR
# KELILING = 2*(PANJANG+LEBAR)

# # cetak hasil
# print(f"hasil dari perhitungan luas adalah {LUAS}")
# print(f"hasil dari perhitungan keliling adalah {KELILING}")

# header
def header():
    '''header function'''
    os.system("clear")
    # os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN PERSEGI PANJANG':^40}")
    print(f"{'='*40:^40}")

# input user
def input_user():
    '''input user function'''
    lebar = int(input("masukkan nilai lebar: "))
    panjang = int(input("masukkan nilai panjang: "))

    return lebar,panjang

# hitung luar
def hitung_luas(lebar,panjang):
    '''hitung luas'''
    return lebar*panjang

# hitung keliling
def hitung_keliling(lebar,panjang):
    '''hitung keliling'''
    return 2*(lebar+panjang)

# display
def display(message,value):
    '''display function'''
    print(f"hasil perhitungan {message} adalah {value}")

# main program
while True:
    header()
    LEBAR,PANJANG = input_user()
    LUAS = hitung_luas(LEBAR,PANJANG)
    KELILING = hitung_keliling(LEBAR,PANJANG)
    display("luas", LUAS)
    display("keliling", KELILING)

    is_continue = input("apakah masih lanjut..?? ")
    if is_continue == "n":
        break

print("program selesai, terimakasih.")
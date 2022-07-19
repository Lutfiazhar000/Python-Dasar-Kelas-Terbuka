# laihan 

import datetime
import os

mhs_template = {
    'nama' : 'nama',
    'nim' : 00000000000,
    'sks_lulus' : 0,
    'lahir' : datetime.datetime(111,1,1),
}

data_mhs = {}

# os.system("cls") # untuk windows
os.system("clear") # untuk linux & mac
print(f"{'SELAMAT DATANG':^20}")
print(f"{'DATA MAHASISWA':^20}")
print("="*20)

# mengambil input user
mhs = dict.fromkeys(mhs_template.keys())
# print(mhs) 
mhs['nama'] = input("Nama Mahasiswa: ")
mhs['nim'] = input("NIM Mahasiswa: ")
mhs['sks_lulus'] = int(input("sks_lulus: "))
TAHUN_LAHIR = int(input("Tahun lahir (yyyy): "))
BULAN_LAHIR = int(input("Tahun bulan (1-12): "))
TANGGAL_LAHIR = int(input("Tahun lahir (1-31): "))
mhs['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
print(mhs)

# laihan 

import datetime
import os
import string
import random

mhs_template = {
    'nama' : 'nama',
    'nim' : 00000000000,
    'sks_lulus' : 0,
    'lahir' : datetime.datetime(111,1,1),
}

data_mhs = {}

while True:
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
    
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mhs.update({KEY:mhs})

    print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<11} {'SKS Lulus':^10} {'Tanggal Lahir':^10}")
    print("-"*60)
        

    for mhs in data_mhs:
        KEY =  mhs
        
        NAMA = data_mhs[KEY]['nama']
        NIM = data_mhs[KEY]['nim']
        SKS = data_mhs[KEY]['sks_lulus']
        LAHIR = data_mhs[KEY]['lahir'].strftime("%x")

        print(f"{KEY:<6} {NAMA:<17} {NIM:<11} {SKS:^10} {LAHIR:^10}")

    print("\n")
    is_done = input("Apakah input data sudah selesai (y/n) ?? ")
    if is_done == "y":
        break

print("program selesai, terima kasih.")

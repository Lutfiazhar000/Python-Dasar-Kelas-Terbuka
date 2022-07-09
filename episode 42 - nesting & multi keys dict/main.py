import datetime

mahasiswa = {
    "nama" : "upi azhar",
    "nim" : "12310173035",
    "sks_lulus" : 130,
    "beasiswa" : False,
    "lahir":datetime.datetime(1996,3,21)

}

mahasiswa2 = {
    "nama" : "wawan sudrajat",
    "nim" : "12310173032",
    "sks_lulus" : 130,
    "beasiswa" : True,
    "lahir":datetime.datetime(1997,2,2)

}

mahasiswa3 = {
    "nama" : "nurul cantikk",
    "nim" : "12310173011",
    "sks_lulus" : 130,
    "beasiswa" : False,
    "lahir":datetime.datetime(1996,2,29)

}

data_mhs = {
    'MHS001' : mahasiswa,
    'MHS002' : mahasiswa2,
    'MHS003' : mahasiswa3
}

print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'beasiswa':<9} {'lahir':<10}")
print("-"*50)

for mhs in data_mhs:
    KEY = mhs 
    NAMA = data_mhs[KEY]['nama']
    NIM = data_mhs[KEY]['nim']
    SKS = data_mhs[KEY]['sks_lulus']
    BEASISWA = data_mhs[KEY]['beasiswa']
    LAHIR = data_mhs[KEY]['lahir'].strftime("%x")

    print(f"{KEY:^6} {NAMA:<17} {SKS:^3} {BEASISWA:^9} {LAHIR:^10}")

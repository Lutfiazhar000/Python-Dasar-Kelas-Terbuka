# latihan 

import datetime as dt

print("masukkan tanggal lahir kamu")
tanggal = int(input("tanggal \t: "))
bulan = int(input("bulan \t\t: "))
tahun = int(input("tahun \t\t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print("\n"+f"tanggal_lahir kamu adalah: {tanggal_lahir} \ndan kamu lahir di hari {tanggal_lahir:%A}")

# menghitung umur
hari_ini = dt.date.today()
print(f"hari ini adalah: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
umur_hari_sisa = umur_hari.days % 365

print(f"umur kamu adalah : {umur_tahun} tahun, {umur_bulan_sisa} bulan, {umur_hari_sisa} hari")

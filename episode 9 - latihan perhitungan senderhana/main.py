# latihan konversi satuan temperatur

print("\nPROGRAM KONVERSIN TEMPERATUR\n")

celcius = float(input("Masukan suhu dalam celcius:"))
print("Suhu adalah:", celcius, "Celcuis")

#  reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah", reamur, "Reamur")

#  fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah", fahrenheit, "Fahrenheit")

#  kelvin
kelvin = 32 + celcius
print("Suhu dalam kelvin adalah", kelvin, "Kelvin")

# =====tugas=====

# fahrenheit -> kelvin
hasil = 5/9 * (fahrenheit - 32) + 273.15
print("hasil konversi", fahrenheit, "Fahrenheit ke kelvin adalah",hasil, "Kelvin")

# kelvin -> fahrenheit
hasil2 = 1.8 *(kelvin - 273) + 32
print("hasil konversi", kelvin, "Kelvin ke fahrenheit adalah",hasil2, "Fahrenheit")


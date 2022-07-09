# looping list dan enumetate

## for loop
print("\n==>for loop<==")
kumpulan_angka = [2,3,5,4,2,6,7,8,6,1]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["jojo", "jotaro", "jolin", "jostar"]

for nama in peserta:
    print(f"nama : {nama}")

## for loop dan range
print("\n==>for dan range<==")
kumpulan_angka = [2,3,5,34,22,16,7,38,36,1]
panjang = len(kumpulan_angka)

for nomer in range(panjang):
    print(f"nomer : {kumpulan_angka[nomer]}")

## while
print("\n==>while<==")
kumpulan_angka = [2,3,5,34,22,16,7,38,36,1]
panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

## list comprehension
print("\n==>list comprehension<==")
data = ["ruslan",2,4,5,"sutiyoso"]
[print(f"data = {i}") for i in data]

kumpulan_angka = [2,3,5,34,22,16,7,38,36,1]
angka_kuadrat = [angka**2 for angka in kumpulan_angka]
print(angka_kuadrat)

## enumerate
print("\n==>enumerate<==")
data_list = ["ruslan",2,4,5,"sutiyoso"]
for index, data in enumerate(data_list):
    print(f"index: {index}, data: {data}")


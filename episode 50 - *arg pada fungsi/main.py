'''args'''

def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi badan {tinggi} cm dan berat {berat} kg")

fungsi("wawan",120,40)

def fungsi2(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi badan {tinggi} cm dan berat {berat} kg")

fungsi2(["hadi",130,60])

# arg
def fungsi2(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi badan {tinggi} cm dan berat {berat} kg")

fungsi("danur",120,40)

# study kasus
def jumlah(*data):
    # data tipenya tiple dan bersifat iterable
    output = 0
    for number in data:
        output += number
    
    return output

hasil = jumlah(1,2,3,4,5,6,7)
print(f"hasilnya adalah {hasil}")

hasil = jumlah(37,42,51)
print(f"hasilnya adalah {hasil}")


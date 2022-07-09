# manipulasi pada list


## operasi

# index  0(-3)    1(-2)     2(-1)
data = ["upi", "ruslan", "nomnom"]

# mengambil data list
data_list = data[1]
print (f"data kedua dari data adalah {data_list}")

data_list_terakhir = data[-1] # bisa menggunakan bilangan negatif
print (f"data terakhir dari data adalah {data_list_terakhir}")


# mengambil info data dalam list
data_panjang = len(data)
print (data_panjang)

## manipulasi data list

# menambahkan item pada list
print (f"data sebelum ditambahkan {data}\n")

data.insert(0,"jhon") # .insert (posisi,data)
print (f"data sesudah ditambahkan {data}")

data.append("sulastri") # .append (menambah di akhir list)
print (f"data sesudah ditambahkan {data}")

# menambah list dengan list
data2 = ["august","max","stave"]
data.extend(data2)
print(f"data sesudah di gabung {data}")

# merubah data pada list
data[3] = "bocil"
print(f"data setelah di rubah {data}")

# menghapus data
data.remove("bocil") # sensitive case
print(f"data setelah di hapus {data}")

# menghapus data paling akhir
data.pop()
print(f"data setelah di hapus bagian belakang {data}")



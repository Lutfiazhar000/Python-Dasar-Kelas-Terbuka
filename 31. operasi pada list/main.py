# operasi pada list
data = [1,5,3,6,2,8,9,8,4,6,2,8,6,4,7]

print (f"data angka = \n{data}")

# count
jumlah_data_8 = data.count(8)
jumlah_data_6 = data.count(6)
print (f"angka 8 pada data muncul {jumlah_data_8} kali")
print (f"angka 6 pada data muncul {jumlah_data_6} kali")

# index
data2 = ["upi","azhar","ruslan","mamat","max"]
index_upi = data2.index("upi")
index_ruslan = data2.index("ruslan")

print (f"index upi ada di {index_upi}")
print (f"index ruslan ada di {index_ruslan}")

# sort
print (f"data angka sebelum diurutkan \n{data}")
data.sort()
print (f"data angka setelah diurutkan \n{data}")

print (f"data string sebelum diurutkan \n{data2}")
data2.sort()
print (f"data string setelah diurutkan \n{data2}")

# reverse
data.reverse()
print (f"data angka setelah di reverse \n{data}")
data2.reverse()
print (f"data string setelah di reverse \n{data2}")




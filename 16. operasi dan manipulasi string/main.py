# operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_depan = "upi"
nama_tengah = "D"
nama_belakang = "azhar"

nama_lengkap = nama_depan + " " + nama_tengah + "'" + nama_belakang
print(nama_lengkap)

# 2. menghitung panjang string (length)
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. operator untuk sting

## cek komponen char / string di dalam string
d = "d"
status = d in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + " = " + str(status)) 

D = "D"
status = D in nama_lengkap
print("string " + D + " ada di " + nama_lengkap + " = " + str(status)) 

d = "d"
status = d not in nama_lengkap
print("string " + d + " tidak ada di " + nama_lengkap + " = " + str(status)) 

## pengulangan string
print("wk "*30)
print(15*"hiya ") # bisa di balik

## indexing
print("index ke 6: " + nama_lengkap[6])
print("index ke 4: " + nama_lengkap[4])
print("index ke -4: " + nama_lengkap[-4]) # mengambil dari belakang
print("index ke [4:10]: " + nama_lengkap[4:10]) # mengambil area
print("index ke [2:4:6:8:10]: " + nama_lengkap[2:10:2]) # mengambil secara acak

## item terkecil
print("item terkecil:" + min(nama_lengkap))

## item terbesar
print("item terbesar:" + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah: " + str(ascii_code))
data = 112
print("char untuk ASCII 112 adalah: " + chr(data))

# 4. operator dalam bentuk method
data = "uvuvwevwevwe onyetenvewve ugwemubwem ossas"
jumlah = data.count("e")
print("jumlah e pada " + data + "= " + str(jumlah))





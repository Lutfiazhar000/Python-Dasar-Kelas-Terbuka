# width dan multiline

#  data
data_nama = "upi azhar"
data_umur = 19
data_tinggi = 165
data_nomor_sandal = 40

# string normal
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sandal = {data_nomor_sandal}"
print(5*"="+"data string"+5*"=")
print(data_string)

# string multiline (menggunakan \n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsandal = {data_nomor_sandal}"
print("\n"+5*"="+"string dengan \\n"+5*"=")
print(data_string)

# string multiline (menggunakan triplets)
data_string = f"""nama : {data_nama}
umur : {data_umur}
tinggi : {data_tinggi}
sandal : {data_nomor_sandal}
"""

print("\n"+5*"="+"string dengan triplets"+5*"=")
print(data_string)

# mengatur lebar string
data_string = f"""
nama   = {data_nama:>9}
umur   = {data_umur:>9}
tinggi = {data_tinggi:>9}
sandal = {data_nomor_sandal:>9}
"""
print(5*"="+"mengatur lebar string"+5*"=")
print(data_string)




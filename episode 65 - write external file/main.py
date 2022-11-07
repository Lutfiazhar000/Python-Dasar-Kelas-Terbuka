# write external file

# 1. mode write (bersifat over write / menimpa)
with open("data_satu.txt","w",encoding="utf-8") as file:
    file.write("kotaro minami")

with open("data_satu.txt","w",encoding="utf-8") as file:
    file.write("kento yamazaki")


# 2. mode append (menambahkan)
with open("data_dua.txt","w",encoding="utf-8") as file:
    file.write("kotaro minami\n")

with open("data_dua.txt","a",encoding="utf-8") as file:
    file.write("kento yamazaki\n")

with open("data_dua.txt","a",encoding="utf-8") as file:
    file.write("yono\n")


# 3. mode r+
with open("data_tiga.txt","w",encoding="utf-8") as file:
    file.write("baris - 1\n")

with open("data_tiga.txt","r+",encoding="utf-8") as file:
    file.write("baris - 1\n")
    file.write("baris - 2\n")
    file.write("baris - 3\n")

with open("data_tiga.txt","r+",encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("data_tiga.txt","r+",encoding="utf-8") as file:
    data = file.write("palu arit") # akan menimpa isi text sesuai dgn panjang data
    print(data)

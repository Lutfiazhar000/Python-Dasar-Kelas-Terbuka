# copy & pop dictionary

pedagang = {
    "bak" : "tukang bakso",
    "sot" : "tukang soto",
    "gor": "tukang nasgor",
    "tuk" : "tukang getuk",
    "mar" : "tukang martabak"
}

tukang = pedagang.copy() # ini tidak merubah 
# tukang = pedagang # ini akan berubah keduanya jk salah satu ada yg di rubah

print(f"pedagang : {pedagang}\n")
print(f"tukang : {tukang}\n")

pedagang["mar"] = "tukang martabak dan terbul"
print(f"pedagang : {pedagang}\n")
print(f"tukang : {tukang}\n")

# pop dictionary -> mengambil berdasarkan key
data_soto = tukang.pop("sot")
print(f"data soto: {data_soto}\n")
print(f"tukang: {tukang}\n")

# popitems -> mengambil yang terakhir ajaahh
data_akhir = tukang.popitem()
print(f"data akhir = {data_akhir}\n")
print(f"tukang: {tukang}\n")
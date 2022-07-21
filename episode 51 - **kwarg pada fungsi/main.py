# kwargs pada fungsi


def fungsi(nama,berat,tinggi):
    '''fungsi biasa'''
    print(f"{nama} memepunyai berat {berat} kg dan tinggi badan {tinggi} cm ")

fungsi("Gwen",49,140)

def fungsi(**kwargs):
    '''fungsi degan kwargs'''
    nama =  kwargs["nama"]
    berat = kwargs["berat"]
    tinggi = kwargs["tinggi"]
    print(f"{nama} memepunyai berat {berat} kg dan tinggi badan {tinggi} cm ")

fungsi(nama="Gwen",berat=49,tinggi=140)

# study kasus
def math(*args,**kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output+=angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output*=angka
    else:
        print("operasi tidak ditemukan")
    return output

hasil = math(4,5,6,7,8,9,option="tambah")
print(f"hasil penjumlahan {hasil}")

hasil = math(4,5,6,7,8,9,option="kali")
print(f"hasil perkalian {hasil}")

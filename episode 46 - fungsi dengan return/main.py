# template fungsi dengan kembalian

# def nama_fungsi(argument):
    # badang fungsi
    # return

# fungsi kuadrat
def kuadrat(input_angka):
    '''fungsi kuadrat'''
    hasil_kuadrat = input_angka**2
    return hasil_kuadrat

x = kuadrat(8)
print(x)
print(kuadrat(4))
z = 84 * kuadrat(7)
print(z)

# fungsi tanpa variabel
def kali(angka1,angka2):
    '''return dengan multi input'''
    return angka1 * angka2

a = kali(4,5)
print(a)

# fungsi dengan return value banyak
def operasi_hitung(angka1,angka2):
    penjumlahan = angka1+angka2
    pengurangan = angka1-angka2
    pembagian = angka1/angka2
    perkalian = angka1*angka2

    return penjumlahan,pengurangan,pembagian,perkalian

d,e,f,g = operasi_hitung(54,32)

print(f"hasil penjumlahan {d}")
print(f"hasil pengurangan {e}")
print(f"hasil pembagian {f}")
print(f"hasil perkalian {g}")

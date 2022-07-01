# format string

# contoh generic

## string
nama = "sergio" 
format_str = f"hallo {nama}"

print(format_str)

## boolean
boolean = True
format_bool = f"boolean = {boolean}"

print(format_bool)

## angka
angka = 74938.4
format_angka = f"angka = {angka}"

print(format_angka)

## angka => bilangan bulat
angka = 31
format_angka = f"angka = {angka:d}"

print(format_angka)

## angka => dengan ordo ribuan
angka = 7000
format_angka = f"angka = {angka:,}"

print(format_angka)

## angka => desimal
angka = 7232.1234
format_angka = f"angka = {angka:.2f}" # membatasi jumlah angka belakang koma

print(format_angka)

## angka => leading zero
angka = 7232.1234
format_angka = f"angka = {angka:08.2f}" # nemabah 0 depan koma

print(format_angka)

## angka => menampilkan tanda + dan -
angka_minus = -20
angka_plus = +20.415
format_angka_minus = f"angka_minus = {angka_minus:+d}"
format_angka_plus = f"angka_plus = {angka_plus:+.2f}"

print(format_angka_minus)
print(format_angka_plus)

## angka => persentase
persentase = 0.075
format_persentase = f"persentase {persentase:.2%}"

print(format_persentase)

## angka => melakukan oparasi aritmatika dalam placeholder
harga = 2000
jumlah = 50
format_angka = f"harga total = Rp {harga*jumlah:,}"

print(format_angka)

## angka => bnary, octal, hex
angka = 229
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)


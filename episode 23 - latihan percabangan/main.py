# latihan membuat kalkulator sederhana

print(15*"=")
print("kalkulator sederhana")
print(15*"=" + "\n")

angkaSatu = float(input("masukan anggka pertama: "))
operator = input("masukan operator (+,-,/,*): ")
angkaDua = float(input("masukan anggka kedua: "))

if operator == "+":
    hasil = angkaSatu + angkaDua
    print(f"hasilnya adalah: {hasil}")
elif operator == "-":
    hasil = angkaSatu - angkaDua
    print(f"hasilnya adalah: {hasil}")
elif operator == "/":
    hasil = angkaSatu / angkaDua
    print(f"hasilnya adalah: {hasil}")
elif operator == "*":
    hasil = angkaSatu * angkaDua
    print(f"hasilnya adalah: {hasil}")
else:
    print("gak iso ngitung aku mas, mumet")

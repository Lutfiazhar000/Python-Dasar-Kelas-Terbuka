# latihan list

# mengolah data buku
list_buku = []
while True:
    print("input koleksi baru")
    judul = input("judul\t: ")
    penulis = input("penulis\t: ")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)
    print(list_buku)

    print("\n\n","="*5,"list buku","="*5)
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")
    
    print("\n\n","="*20)
    is_lanjut = input("apakah kamu ingin berhenti? (y/n) ")

    if is_lanjut == "y":
        break

print("input data selesai")


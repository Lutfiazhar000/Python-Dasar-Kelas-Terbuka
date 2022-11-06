# __main__ adalah top level code environmet

# __name__ = akan terjadi jika ada di program utama

## __name__ pada file program utama
print(f"nilai __name pada main.py adalah '{__name__}' ")

## __name__ pada file program eksternal
import fungsi

# contoh penggunaan

# deklarasi

def fungsi_kali(a:int,b:int)->int:
    return a*b

# fungsi utama
if __name__ == "__main__":
    angka_1 = 4
    angka_2 = 8
    hasil = fungsi_kali(angka_1,angka_2)
    print(f"hasil kali = {hasil}")

# import package
import package
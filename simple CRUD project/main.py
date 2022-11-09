# episode 67 - 71

import os
import CRUD as CRUD

if __name__ == "__main__":
    oprating_system = os.name

    match oprating_system:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
    
    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print("="*25)

    # check database ada atau tidak
    CRUD.init_console()

while(True):
    match oprating_system:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print("="*25)

    print(f"1. read data")
    print(f"2. create data")
    print(f"3. update data")
    print(f"4. delete data\n")

    user_option = input("masukkan opsi: ")

    print("\n","="*25,"\n")

    match user_option: 
        case "1": print(f"1. read data")
        case "2": print(f"2. create data")
        case "3": print(f"3. update data")
        case "4": print(f"4. delete data")

    print("\n","="*25,"\n")
    
    is_done = input("apakah sudah selesai?? (y/n): ")
    if is_done == "y" or is_done == "Y":
        break

print("program selesai.")



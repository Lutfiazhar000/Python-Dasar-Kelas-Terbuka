from . import Operasi

DB_NAME = "data.txt"
TEMPLATE = {
    "pk":"xxxxxx",
    "date_add":"yyyy-dd-mm",
    "penulis":255*" ",
    "jadul":255*" ",
    "tahun":"yyyy",
    "ISBN":"xxxxxxxxxxxxxxxxx",
    "kota":255*" "
    }

def init_console():
    try:
        with open(DB_NAME,"r") as file:
            print("Database tersedia, init done! ")
    except:
        print("Database tidak tersedia, silahkan buat database baru")
        Operasi.create_first_data()


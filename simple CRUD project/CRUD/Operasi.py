# import Database
from . import Database
from .Utility import random_string
import time

def create_first_data():
    penulis = input("penulis: ")
    judul = input("judul: ")
    tahun = input("tahun: ")
    ISBN = input("ISBN: ")
    kota = input("kota: ")

    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%d-%m-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = tahun
    data["ISBN"] = ISBN
    data["kota"] = kota + Database.TEMPLATE["kota"][len(kota):]

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]},{data["ISBN"]},{data["kota"]}\n'
    print(data_str)
    try:
        with open(Database.DB_NAME,"w",encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("gagal")
    







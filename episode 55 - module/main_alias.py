# membuat module sederhana

from hitung import tambah as tam # bisa pakai * u/ import semua
from hitung import kali as kal
from hitung import pangkat as pang 

hasil_tambah = tam(2,3,4,5,6)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = kal(2,3,4,5,6)
print(f"hasil kali = {hasil_kali}")

hasil_pangkat = pang(4)
print(f"hasil pangkat 4 = {hasil_pangkat(4)}")

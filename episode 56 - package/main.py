# membuat package sederhana

import sains.hitung
from sains import fisika
from sains.fisika import gaya as force

hasil_1 = sains.hitung.tambah(4,6,3,7,8)
print(f"hasil tambah dari package adalah {hasil_1}")

hasil_gaya = fisika.gaya(90,10)
print(f"hasil gaya adalah {hasil_gaya}")

hasil_gaya2 = force(70,14)
print(f"hasil gaya adalah {hasil_gaya2}")


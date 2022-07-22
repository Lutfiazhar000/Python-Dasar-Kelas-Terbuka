# __init__ pada package

import sains
from sains.matematika import science

hasil_tambah = sains.matematika.tambah(4,7,3,8,2,10,9,3)
print(f"hasil tambah {hasil_tambah}")

hasil_kali = sains.matematika.kali(4,7,3,8,2,10,9,3)
print(f"hasil kali {hasil_kali}")

hasil_pangkat3 = science.pangkat(3)
print(f"hasil panggkat 3 dari 6 adalah {hasil_pangkat3(6)}")

hasil_fisika = sains.fisika.gaya(42,19)
print(f"hasil gaya {hasil_fisika}")

#-------------------------------------- 

# from sains import *

# hasil_tambah = matematika.basic.tambah(4,7,3,8,2,10,9,3)
# print(f"hasil tambah {hasil_tambah}")

# hasil_kali = matematika.basic.kali(4,7,3,8,2,10,9,3)
# print(f"hasil kali {hasil_kali}")

# hasil_fisika = fisika.gaya(42,19)
# print(f"hasil gaya {hasil_fisika}")


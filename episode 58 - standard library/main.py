import datetime

data_waktu = datetime.datetime.now()
print(f" tanggal sekarang {data_waktu}")
print(f"sekarang tahun {data_waktu.year}")
print(f"sekarang hari {data_waktu.strftime('%A')}")

from collections import Counter

data = ["a","d","d","a","b","e","e","c","a","c"]
data_count = Counter(data)

print(f"data counter = {data_count}")
print(f"jumlah a adalah {data_count['a']}")
print(f"jumlah e adalah {data_count['e']}")

# import io
import io
file = io.open("file_text.txt","r")
print(file.read())

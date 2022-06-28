# a = 10 adalah variabel dengan nilai 10

# tipe data: angka satuan yang tidak ada komanya atau integer
data_integer = 13
print("data : ", data_integer)
print("- bertipe :", type(data_integer))

# tipe data: angka dengan koma atau float
data_float = 17.4
print("data : ", data_float)
print("- bertipe :", type(data_float))

# tipe data: kumpulan karakter (string)
data_string = "upi"
print("data : ", data_string)
print("- bertipe :", type(data_string))

# tipe data: biner true or false (boolean)
data_bool = False
print("data : ", data_bool)
print("- bertipe :", type(data_bool))

## tipe data khusus

# bilangan kompleks
data_complex = complex(4,6)
print("data : ", data_complex)
print("- bertipe :", type(data_complex))

# tipe data dari bahasa C
from ctypes import c_double

data_double = c_double(10.4)
print("data : ", data_double)
print("- bertipe :", type(data_double))
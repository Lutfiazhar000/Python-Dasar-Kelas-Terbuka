# deep copy

data = [1,2]
data_2 = [3,4,5]

data2D = [data,data_2,10]
data2D_copy = data2D.copy()

print(f"data 2D = {data2D}")
print(f"data 2D copy = {data2D_copy}\n")

# mengambil data dari nested list
data2 = data2D[0][1]
print(f"data = {data2}")

# melihat address dari list
print(f"address dari list asli {hex(id(data2D))}")
print(f"address dari list copy {hex(id(data2D_copy))}")

print(f"address dari member ke 1")
print(f"address dari list asli {hex(id(data2D[0]))}")
print(f"address dari list copy {hex(id(data2D_copy[0]))}\n")

data2D[1][0] = 9
data2D[2] = 7
print(f"data: {data2D}")
print(f"data copy: {data2D_copy}\n")

# deep copy
from copy import deepcopy

data2D = [data,data_2,10]
data2D_deepcopy = deepcopy(data2D)

print(f"address dari list asli {hex(id(data2D))}")
print(f"address dari list deepcopy {hex(id(data2D_deepcopy))}")

print(f"address dari member ke 1")
print(f"address dari list asli {hex(id(data2D[0]))}")
print(f"address dari list deepcopy {hex(id(data2D_deepcopy[0]))}\n")

data2D[1][0] = 99
print(f"data = {data2D}")
print(f"data copy = {data2D_copy}")
print(f"data deepcopy = {data2D_deepcopy}")
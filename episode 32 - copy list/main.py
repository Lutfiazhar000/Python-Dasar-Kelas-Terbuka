# copy list

## teknik duplikasi list
a = ["upi","azhar","ningrum","qoyun"]
print(f"a = {a}")

b = a
print(f"b = {b}")

## merubah member dari a
a[1] = "viego" # ini akan merubah keduanya
b.sort()
print(f"a = {a}")
print(f"b = {b}") 

# melihat address dari kedua list (a dan b)
print(f"address a adalah {hex(id(a))}")
print(f"address b adalah {hex(id(b))}")

# menduplikat list dengan .copy
print(f"membuat list c dengan a.copy()")
c = a.copy()

print(f"address a adalah {hex(id(a))}")
print(f"address b adalah {hex(id(b))}")
print(f"address c adalah {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}") 
print(f"c = {c}") 

print("merubah data list c")
c[0] = "otong"
print(f"c = {c}") 





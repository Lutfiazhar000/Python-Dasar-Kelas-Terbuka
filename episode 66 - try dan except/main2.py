from numbers import Number

def pangkat(a,b):
    if not isinstance(a,Number) or not isinstance(b,Number):
        raise "input yang dimasukkan harus angka"
    return a**b

print("hasil = ", pangkat(2,5))
print(pangkat(3,"2"))

# angka = 0

# try:
#     hasil = 20/angka
# except Exception as error_message:
#     print(error_message)


# try:
#     hasil = 20/angka
# except  ZeroDivisionError as error_message:
#     print(error_message)
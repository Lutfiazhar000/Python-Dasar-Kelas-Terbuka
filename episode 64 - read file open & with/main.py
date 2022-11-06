# membaca file eksternal

print(3*"=","membaca file txt", 3*"=")
file = open("data.txt",mode="r")
# file = open("data.txt",mode="w")

print(f"status read : {file.readable()}")
print(f"status write : {file.writable()}")

# semua file
print(file.read())

# baca per baris
# print(file.readline(),end="")
# print(file.readline(),end="")

# baca semua line sbg list
# print(file.readlines())

print(f"apakah file sudah ditutup : {file.closed}")

file.close()
print(f"apakah file sudah ditutup : {file.closed}")

# teknik membuka file di python dengan with
print(3*"=","membaca file txt dengan with", 3*"=")
with open("data.txt",mode="r") as file:
    content = file.readline()
    print(content,end="")
    print(f"apakah file sudah ditutup : {file.closed}")

print(f"apakah file sudah ditutup : {file.closed}")

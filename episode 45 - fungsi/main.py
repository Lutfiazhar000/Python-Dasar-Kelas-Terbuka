# fungsi dengan argumen

'''

def nama_fungsi(argument):
    body functions

'''
# string
def hello_world(name):
    # fungsi hello world menerima input dengan variabel
    print(f"selamat datang {name} ")

hello_world("upi")
hello_world("azhar")

# int
def perkalian(angka1,angka2):
    hasil = angka1*angka2
    print(f"hasil perkalian dari {angka1} dan {angka2} adalah {hasil}")

perkalian(4,33)
perkalian(44,73)

# list
def say_hi(member_list):
    data_member = member_list.copy()
    for member in data_member:
        print(f"hai kamu {member}")

member_mlm = ["kiki","wawan","yanto"]
say_hi(member_mlm)

data = "ini adalah string"
print(data)
print(type(data))

# 1.membuat string
'''
    1. dengan menggunakan single quote '--'
    2. dengan menggunakan double quote "--"

'''

data = 'menggunakan single quote'
print(data)

data = "menggunakan single quote"
print(data)

print("'haloo.., apa kabar'")
print('"haloo.., apa kabar"')

# 2.menggunakan tandan \

# membuat tanda ' jadi str
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# backslash
print("C:\\user\\upi")

# tab
print("upi\tazhar, jauhan")

# backspace
print("upi \bazhar")

# newline
print("baris pertama, \nbaris kedua") # line feed
print("baris pertama, \rbaris kedua") # carriage retrun
print("baris pertama, \r\nbaris kedua") # line read carriage return

# 3. string literal atau raw

# hati2
print('C:new folder') # salah

# raw string
print(r'C:new folder')

# multiline string literal
print('''
nama: upi
semester: 1
''')

# raw dan multiline literal
print('''
nama: upi
semester: 1\ILPUS
web: www.upi.com/home
''')

# operator dalam method

# merubah case dari string
## merubah ke uppercase
salam = "bro!"
print("normal = " + salam)
salam2 = salam.upper()
print("upper = " + salam2)

## merubah ke lowercase
alay = "UpI suKA NGaNtUk"
print("normal = " + alay)
alay2 = alay.lower()
print("lower = " + alay2)

## pengecekan dengan isX() method

# mengecek lowercase
nama = "uvuvwevwevwe onyetenvewve ugwemubwem ossas"
apakah_lower = nama.islower() 
print(nama + "is lower = " + str(apakah_lower)) # hasil .islower() berupa boolean, jd harus di casting ke str

# mengecek uppercase
apakah_upper = nama.isupper() 
print(nama + "is upper = " + str(apakah_upper)) # hasil .isupper() berupa boolean, jd harus di casting ke str

# contoh method pengecekan lain
# isalpha() ==> untuk mengecek semuanya huruf
# isalnum() ==> untuk mengecek semuanya huruf dan angka 
# isdecimal() ==> untuk mengecek semuanya angka 
# isspace() ==> untuk mengecek spaci, tab, newline 
# istitle() ==> untuk mengecek permulaan kata diawali huruf besar 

title = "It Is Ok To Be Not Ok"
check_title = title.istitle() # hasil berupa boolean
print(title + " is title = " + str(check_title))

## cek komponen startswith() dan endseith()
# startswith()
cek_mulia = "upi azhar".startswith("upi")
print("start = " + str(cek_mulia))

# endwith()
cek_mulia = "upi azhar".endswith("azhar")
print("end = " + str(cek_mulia))

## penggunaan join() dan split()
# join
berpisah = ['ya','ga','tau','kok','tanya','saya']
bergabung = ','.join(berpisah)
print(berpisah)
print(bergabung)

bergabung = ' '.join(berpisah)
print(bergabung)

bergabung = ' hmm '.join(berpisah)
print(bergabung)

# split
bergabung = "yahmmgahmmtauhmmkokhmmtanyahmmsaya" # menjadi object
print(bergabung.split('hmm'))

## alokasi karakter rjust() ljust() center()
# rjust
kanan = "kanan".rjust(12)
print("'"+kanan+"'")

# ljust
kiri = "kiri".ljust(12)
print("'"+kiri+"'")

# center
tengah = "tengah".center(30,"&")
print("'"+tengah+"'")

## kebalikan strip()
tengah2 = tengah.strip("&") # menghilangkan
print("'"+tengah2+"'")








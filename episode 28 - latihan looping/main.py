# latihan looping

## menggunakan for 
sisi = 10

# dummy variable
count = 1
for i in range(4):
    print("*"*count)
    count += 1

print("===akhir for===\n")

## menggunakan while
count = 1
while True:
    print("*"*count)
    count +=1

    if count > sisi:
        break

print("===akhir while===\n")

## menggunakan while -> ganjil aj
count = 1
while True:
    # akan kembali ke atas jika ganjil
    if count % 2: 
        # print jika gaanjil
        print("*"*count) 
        count +=1
    else:
        # akan kembali ke atas jika ganjil     
        count +=1
        continue

    # akan break jika melebihi sisi
    if count > sisi: 
        break

print("===akhir while===\n")

## menggunakan while -> segitiga sama kaki
count = 1
spasi = int(sisi/2)

while True:
    if count % 2: 
        # print jika gaanjil
        print(" "*spasi,"+"*count) 
        spasi -=1
        count +=1
    else:
        # akan kembali ke atas jika ganjil     
        count +=1
        continue
    

    # akan break jika melebihi sisi
    if count > sisi: 
        break
print("===akhir while===\n")

# tugas
count = 1
spasi = int(sisi/2)

while True:
    if count % 2: 
        # print jika gaanjil
        print(" "*spasi,"+"*count) 
        spasi -=1
        count +=1
    else:
        # akan kembali ke atas jika ganjil     
        count +=1
        continue
    

    # akan break jika melebihi sisi
    if count > sisi: 
        break

while True:
    if count % 2: 
        # print jika gaanjil
        spasi +=1
        print(" "*spasi,"+"*count) 
        count -=1
    else:
        # akan kembali ke atas jika ganjil     
        count -=1
        continue
    
    # akan break jika melebihi sisi
    if count == 0: 
        break
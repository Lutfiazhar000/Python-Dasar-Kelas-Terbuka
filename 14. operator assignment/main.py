# operasi yang dapat dilakukan dgn penyingkatan
# operasi ditambah dengan assignment

from numpy import true_divide


a = 5 
print("nilai a =", a)

a += 1 # penjumlahan
print("nilai a +=", a)

a -= 2 # pengurangan
print("nilai a -=", a)

a *= 4 # perkalian
print("nilai a *=", a)

a /= 2 # pembagian
print("nilai a /=", a)

b = 10
print("nilai b =", b)

b %= 3 # modulus
print("nilai b %=", b)

b = 10
print("nilai b =", b)

b //= 2 # left division
print("nilai b %=", b)

a = 5
print("nilai a =", a)

a **= 3 #eksponen
print("nilai a =", a)

# operasi bitwise
print ("\n===operasi bitwise===")

# OR
c = True
print("\nnilai c =",c)

c |= False
print("nilai c |= false, nilai c menjadi",c)

c = False
print("nilai c =",c)

c |= False
print("nilai c |= false, nilai c menjadi",c)

# AND
c = True
print("\nnilai c =",c)

c &= False
print("nilai c |= false, nilai c menjadi",c)

c = True
print("nilai c =",c)

c &= True
print("nilai c |= true, nilai c menjadi",c)

# XOR
c = True
print("\nnilai c =",c)

c ^= False
print("nilai c ^= false, nilai c menjadi",c)

c = True
print("nilai c =",c)

c ^= True
print("nilai c ^= true, nilai c menjadi",c)

# shift left & right
d = 0b0100
print("\nnilai d =", format(d,'04b'))
d>>=2
print("nilai d >>= 2, nilai d menjadi", format(d,'04b'))

d<<=1
print("nilai d >>= 2, nilai d menjadi", format(d,'04b'))
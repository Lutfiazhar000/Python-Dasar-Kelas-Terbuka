# operasi aritmatika

a = 64
b = 8

# penjumlahan
hasil = a + b
print(a,"+",b,"=",hasil)

# pengurangan
hasil = a - b
print(a,"-",b,"=",hasil)

# perkalian
hasil = a * b
print(a,"*",b,"=",hasil)

# pembagian 
hasil = a / b
print(a,"/",b,"=",hasil)

# eksponensial / pangkat
hasil = a ** b
print(a,"**",b,"=",hasil)

# modulus
hasil = a % b
print(a,"%",b,"=",hasil)

# floor devision
hasil = a // b
print(a,"//",b,"=",hasil)

# prioritas operasi, operational precendence

''' 
    1. ()
    2. eksponen
    3. perkalian, penbagian, dkk
    4. penjumlahan, pengurangan
'''

x = 3
y = 2 
z = 4

hasil = x ** y * (z + x) / y - y % z // x 
print(x,'**',y,'*','(',z,'+',x,')','/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)

hasil = (x + y) * z
print('(',x,'+',y,')','*',z,'=',hasil)
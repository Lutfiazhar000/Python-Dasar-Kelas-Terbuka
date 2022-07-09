# list

# kumpulan data angka
data_angka = [1,2,3,4]
print (data_angka)

#kumpulan data str
data_str = ["upi","ruslan","azhar","iwed"]
print (data_str)

#kumpulan data boolean
data_bool = [True, False, False, True]
print (data_bool)

#kumpulan data campuran
data_mix = ["upi",False,4557,"fahrana"]
print (data_mix)

#alternatif membuat list
data_range = range(0,15,2) #range(start,stop,step)
print (data_range)
data_list = list(data_range)
print (data_list)

#membuat list dengan loop / list comprehensive

##contoh 1
listWithFor = [i for i in range(0,10)]
print (listWithFor)

##contoh 2
listWithFor2 = [i**2 for i in range(0,10)]
print (listWithFor2)

#membuat list dengan for dan if
listForIf = [i for i in range(0,10) if i != 6]
listForIf2 = [i for i in range(0,10) if i%2 == 0]
listForIf3 = [i for i in range(0,10) if i%2 != 0]
print (listForIf)
print (listForIf2)
print (listForIf3)
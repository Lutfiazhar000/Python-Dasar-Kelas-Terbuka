# operator dictionary

data_dict = {
    'kong' : 'wukong',
    'har' : 'azhar',
    'mad' : 'mamad'
}

# melihat panjang dari dict
LENDICT = len(data_dict)
print(f"panjang dari data_dict adalah: {LENDICT}")

# mendeteksi key exist atau tidak
KEY = "ucp"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di dalam data_dict: {CHECKKEY}") # berupa boolean

# mengakses values (read) dengan get
print(data_dict['kong'])
print(data_dict.get('kong'))
print(data_dict.get('ucp','key tidak ditemukan'))

# update data dict
data_dict['har'] = 'azhar suka mie goreng'
print(data_dict)
data_dict['yuk'] = 'yayuk'
print(data_dict)

data_dict.update({'har' : 'azhar'}) # akan merubah data jika data sudah exist
print(data_dict)
data_dict.update({'yur' : 'yurii'}) # akan menambah data baru jika data tidak exist
print(data_dict)

# menghapus data pada dict
del data_dict['kong']
print(data_dict)

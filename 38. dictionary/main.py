# dictionary

# list adalah array di python, dapat diakses dengan menggunakan index
data_list = ['ya','gak','tahu','kok','tanya','saya']
print(data_list[0])

# berbedan dengan dictionary -> dict atau bisa disebut associative array
# mengakses dict menggunakan identifier -> key
data_dict = {
    # 'key' : 'value'
    'up' : 'upi',
    'az' : 'azhar',
    'yd' : 'yuda',
    'jh' : 'jhon',
    'nmbr' : 1000,
    'ls' : data_list
}

print(data_dict['az'])
print(data_dict['ls'])
print(data_dict['nmbr'])
# looping pada dictionary

pakde_squad = {
    'har' : 'hari',
    'fak' : 'fakih',
    'wan' : 'wawan',
    'gus' : 'bagus'
}

# looping 
for member in pakde_squad:
    print(member) # akan mengambil keys saja

# operator untuk mengambil item / iterables
keys = pakde_squad.keys()
print(keys) 

for key in pakde_squad.keys():
    print(pakde_squad.get(key))

values = pakde_squad.values() # mengambil value saja
print(values)

for member in pakde_squad.values():
    print(member)

# pakai items
items = pakde_squad.items()
print(items)

for item in pakde_squad.items():
    print(item)

for key,value in pakde_squad.items():
    print(f"key = {key}, value = {value}")





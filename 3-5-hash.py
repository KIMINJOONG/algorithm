# hash_table = list([0 for i in range(10)])
# print(hash_table)

# def hash_func(key):
#     return key % 5

# data1 = 'Andy'
# data2 = 'Dave'
# data3 = 'Trump'

# print(ord(data1[0]), ord(data2[0]), ord(data3[0]))
# print(ord(data1[0]), hash_func(ord(data1[0])))

# def storage_data(data, value):
#     key = ord(data[0])
#     hash_address = hash_func(key)
#     hash_table[hash_address] = value

# storage_data('Andy', '000000')
# storage_data('Dave', '111111')
# storage_data('Trump', '222222')

# def get_data(data):
#     key =ord(data[0])
#     hash_address = hash_func(key)
#     return hash_table[hash_address]

# print(get_data('Andy'))

hash_table = list([0 for i in range(10)])

def hash_func(key):
    return key % 5

def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

storage_data('Min', '00000')
storage_data('Lee', '11111')
storage_data('Kwon', '22222')

print(hash_table)

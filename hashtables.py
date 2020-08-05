HASH_DATA_SIZE = 8

hash_data = [None] * HASH_DATA_SIZE


def hash_function(s):
    bytes_list = s.encode()
    total = 0
    for b in bytes_list:
        total += b

    return total


def get_index(s):
    hash_value = hash_function(s)

    return hash_value % HASH_DATA_SIZE


def put(k, v):
    print(f"Putting {k} -> {v}")
    index = get_index(k)
    if hash_data[index] is not None:
        print("COLLISION")
    hash_data[index] = v


def get(k):
    index = get_index(k)
    return hash_data[index]


def delete(k):
    index = get_index(k)
    hash_data[index] = None


print(hash_data)
put("Beej!", "Brandon")
print(hash_data)
put("g", 123456)
print(hash_data)

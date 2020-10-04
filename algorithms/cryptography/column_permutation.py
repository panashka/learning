import math

# key is number like 231 which represents column permutation
def encode(msg, key):
    key_arr = [int(d) for d in str(key)]
    num_rows = math.ceil(len(msg) / len(key_arr))

    inverse_mapping = []
    for i in range(len(key_arr)):
        idx = key_arr[i] - 1
        inverse_mapping.insert(idx, i)

    cryptogram = ''
    index = 0
    for i in range(num_rows):
        for j in range(len(key_arr)):
            index = i * len(key_arr) + inverse_mapping[j]
            if index < len(msg):
                cryptogram += msg[index]
            else:
                cryptogram += '='
    return cryptogram

def decode(cryptogram, key):
    key_arr = [int(d) for d in str(key)]
    num_rows = math.ceil(len(cryptogram) / len(key_arr))

    msg = ''
    index = 0
    for i in range(num_rows):
        for j in range(len(key_arr)):
            index = i * len(key_arr) + key_arr[j] - 1
            if index < len(cryptogram):
                msg += cryptogram[index]
    return msg


msg = 'hello World'
cryptogram = encode(msg, 231)
print(cryptogram)
decoded_msg = decode(cryptogram, 231)
print('decoded msg: {}'.format(decoded_msg))

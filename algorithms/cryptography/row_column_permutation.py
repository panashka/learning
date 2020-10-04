import math

# key is number of columns used for row/col permutation
def encode(message, key):
    arr = []
    msg_counter = 0
    
    while msg_counter < len(message):
        row = []
        for i in range(key):
            if msg_counter < len(message):
                row.append(message[msg_counter])
                msg_counter += 1
            else:
                # append dummy symbol
                row.append('=')
        
        arr.append(row)

    encrypted_message = ''
    for column in zip(*arr):
        for ch in column:
            encrypted_message += ch

    return encrypted_message

# key is number of columns for permutation
def decode(cryptogram, key):
    num_rows = math.ceil(len(cryptogram) / float(key))
    msg = ''
    for i in range(num_rows):
        index = i
        for j in range(key):
            msg += cryptogram[index]
            index += num_rows
    return msg


msg = 'Hello world!'
crypthogram = encode(msg, 5)
print(crypthogram)
msg = decode(crypthogram, 5)
print(msg)
        

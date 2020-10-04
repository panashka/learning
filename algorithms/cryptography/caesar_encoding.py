import char_freq_counter
from char_freq_counter import ALPHABET

def encode(msg, offset):
    map = {}
    for i in range(len(ALPHABET)):
        map[ALPHABET[i]] = ALPHABET[(i + offset) % len(ALPHABET)]
    msg = "".join(msg.split()).lower()
    encoded_msg = ''
    counter = 0
    for ch in msg:
        if counter == 4:
            encoded_msg += ' '
            counter = 0
        counter += 1
        encoded_msg += map[ch]
    return encoded_msg.upper()

def decode(cryptogram, offset):
    map = {}
    for i in range(len(ALPHABET)):
        map[ALPHABET[i]] = ALPHABET[(i - offset) % len(ALPHABET)]
    cryptogram = "".join(cryptogram.split()).lower()
    msg = ''
    for ch in cryptogram:
        msg += map[ch]
    return msg

msg = 'KYVIV NRJRK ZDVNY VERTRV JRIJL SJKZK LKZFE NRJKY VJKRK VFWKY VRIK'
freq = char_freq_counter.count_frequency(msg)
for i in range(5):
    ch = list(freq.keys())[i]
    offset = char_freq_counter.char_e_offset()[ch]
    decoded_msg = decode(msg, offset)
    print('Character - {}'.format(ch))
    print(decoded_msg)


# encoded_msg = encode(msg, 13)
# print(encoded_msg)
# decoded_msg = decode(encoded_msg, 13)
# print(decoded_msg)

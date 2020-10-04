ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def count_frequency(msg):
    map = {}
    for ch in ALPHABET:
        map[ch] = 0
    
    msg = "".join(msg.split()).lower()
    for ch in msg:
        map[ch] += 1
    
    freq = {}
    for key in map:
        freq[key] = float(map[key]) / len(ALPHABET) * 100

    # sort by value
    freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}

    return freq

def char_e_offset():
    e_index = 4
    offset_map = {}
    for i in range(len(ALPHABET)):
        offset = (i - e_index) % len(ALPHABET)
        offset_map[ALPHABET[i]] = offset
    return offset_map

# offset_map = char_e_offset()
# for key in offset_map:
#     print('Character {}, offset - {}'.format(key, offset_map[key]))


# msg = 'There is a time where you need just type anything in order to measure frequency of any character in the sentence'
# freq = count_frequency(msg)
# for key in freq:
#     print('Character {} - frequency {}'.format(key, freq[key]))
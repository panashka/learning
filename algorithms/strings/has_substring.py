def has_substring(str, substr):
    for i in range(len(str)):
        for j in range(len(substr)):
            has_substring = True
            if i + j > len(str) - 1:
                return False
            elif str[i + j] != substr[j]:
                has_substring = False
                break
        
        if has_substring:
            break
    return has_substring

print(has_substring('hellomamamam3', 'mam3'))


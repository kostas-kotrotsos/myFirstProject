def SimpleSymbols(str1):
    str2 = str1
    index = 0
    print("l",len(str2))
    while index < len(str2):
        for i in str2:
            if str2[index].isalpha():
                if str2[index - 1] != '+' or str2[index + 1] != '+':
                    return 'false'
                print(index)
            index += 1
        return 'true'


print(SimpleSymbols('o+3=+s+'))
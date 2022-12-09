# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

txt = 'WWWWBBBBAAACAARR'

def encode(f):
    encodind = ''
    i = 0
    while i < len(txt):
        count = 1
        while i + 1 < len(txt) and txt[i] == txt[i+1]:
            count += 1
            i += 1
        encodind += str(count) + txt[i]
        i += 1
    return encodind

def decode(f):
    decoding = ''
    num = ''
    for i in range(len(f)):
        if not f[i].isalpha():
            num += f[i]
        else:
            decoding = decoding + f[i] * int(num)
            num = ''
    return decoding

txt2 = encode(txt)
print(txt2)
print(decode(txt2))


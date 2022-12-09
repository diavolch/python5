'''Напишите программу, удаляющую из текста все слова, содержащие ""абв"".'''

text = 'текст с абв, который удаляет и у абвгд абв'

# lst = text.split()
# lst2 = []
# for i in range(len(lst)):
#     if lst[i].find('абв'):
#         lst2.append(lst[i])
# res = ' '.join(lst2) 
# print(res)

lst2 = [i for i in text.split() if 'абв' not in i]
print(' '.join(lst2))
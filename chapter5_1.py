#программа печатает список слов в сл. порядке

import random

words=[]
word=''
i=0

vvod=input('Введите список слов через пробел: ')+' '
for symbol in vvod:
    if symbol==' ':
        if word!=' ' and word!='':
            words.append(word)
            i+=1
        word=''
    elif symbol!=' ':
        word+=symbol

#сформирован список введенных польз. слов
print('Вы ввели', words)

while words:
    vivod=random.choice(words)
    print(vivod, end=' ')
    words.remove(vivod)
input()

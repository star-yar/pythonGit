#Игра по угадыванию слова
import random
print('''
Добро пожаловать в игру!

- Ваша задача назвать загаданное компьютером слово.
- До угадывания слова вам представиться возможность проверить,
  какие буквы присутствуют в слове.
- Число вводов букв ограничено.

Удачи!

Слово загадано...

''')

WORDS=('яблоко','арматура','тритон','физиология','терапевт','Норвегия')

word=random.choice(WORDS)
print('Число букв в слове = ', len(word))

#кол-во попыток угадывания
tries=len(word)*2
tries=int(tries)

#Угаданные буквы здесь
letters=''

print('Попыток угадать букву ', tries,'\n')

while tries:
    print(tries, end='')
    char=input('. Введите букву: ')
    #char1=char.lower()
    if char in word:
        print()
        letters+=char
        for c in word:
            if char==c:
                print(c,end='')
            else:
                print('-',end='')
        print()
        print()
    else:
        print('Такой буквы в слове нет')
    tries-=1
print('__________________________________________________________________________')
if letters:
    print('Угаданные буквы', letters)
else:
    print('К сожалению, вы не угадали ни одной буквы')

theor=input('Ваш вариант слова: ')
if theor==word:
    print('Вы угадали')
else:
    print('Вы не угадали')

input('\nИгра окончена...')

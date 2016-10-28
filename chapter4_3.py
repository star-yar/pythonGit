# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
WORDS = ("питон", "перепелица", "легкость", "сложность", "ответ", "ксилофон")
HELP = ('тип змеи', 'небольшая птичка', 'ощещение невесомости, свободы', 'настройка игры подразумевает выбор ...', 'в конце задачи', 'муз. инстурмент') 
# pick one word randomly from the sequence
word = random.choice(WORDS)
wordPosition=0

for i in WORDS:
    if i==word:
        break
    wordPosition+=1


# create a variable to use later to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""
           Привет, игрок!
        
  Главная задача этой игры - расшифровать слово из набора букв.

  - Чтобы окончить игру нажмите Enter, не вводя свой вариант
  - Чтобы получить посказку вместо слова ведите команду "?"


"""
)
print("Вот набор букв:", jumble)

guess = input("\nВаш вариант: ")
while guess != correct and guess != "":
    if guess == '?':
        print('\n\t',HELP[wordPosition],'\n')
        guess = input("Ваш вариант: ")
        continue
    print("Нет, это не то слово, что я загадал.")
    guess = input("Ваш вариант: ")
       
if guess == correct:
    print("Это оно, молодчик!\n")


print("Спасибо за игру.")

input("\n\nНажмите любую клавишу чтобы закончить.")

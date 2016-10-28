# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money



def askNumber():
    print('Введите число ',end='')
    global guess
    guess=int(input(''))

def getAnswer(number, guess, tries):
    if guess==number:
        print("Угадал! Это было число ", number)
        print("Это заняло у тебя ", tries, "попытки!\n")
        endGame=True
    elif guess>number:
        print('Меньше')
        tries+=1
    elif guess<number:
        print('Больше')
        tries+=1
    return tries

def main():
    import random
    endGame=False
    print("\tWelcome to 'Guess My Number'!")
    print("\nI'm thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible.\n")

    # set the initial values
    number = random.randint(1, 100)
    #guess = int(input("Take a guess: "))
    tries = 1

    while not endGame:
        askNumber()
        tries=getAnswer(number, guess, tries)
      
    input("\n\nНажми enter для выхода.")


main()

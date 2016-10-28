# Trivia Challenge
# Trivia game that reads a plain text file

import sys, pickle, shelve

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)
    
    question = next_line(the_file)
    
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        
    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    stavka = next_line(the_file)
    
    explanation = next_line(the_file) 

    return category, question, answers, correct, stavka, explanation

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tДобро пожаловать в ВИКТОРИНУС\n")
    print("\t\t", title, "\n")

def addRecord(userName, record):
    myFile=shelve.open('document')
    myFile[userName]=record

def readRecords():
    print('_________________')
    print('''   SCORES''')
    print('_________________')
    myFile=shelve.open('document')
    for name in myFile:
        print(name, myFile[name])
    print('_________________')

def readDataTxt(file):
    file=open(file, 'r')

    name=' '

    print('\n___SCORES___\n')
    while name:
        name=file.readline()
        score=file.readline()

        print(name, score)
    file.close

def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    userName=input('Игрок, введите ваше имя: ')

    # get first block
    category, question, answers, correct, stavka, explanation = next_block(trivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # get answer
        answer = input("Ваш ответ: ")

        # check answer
        if answer == correct:
            print("\nВерно", end=" ")
            stavka=int(stavka)
            score += stavka
        else:
            print("\nНеправильно.", end=" ")
        print(explanation)
        print("Счет:", score, "\n\n")

        # get next block
        category, question, answers, correct, stavka, explanation = next_block(trivia_file)

    trivia_file.close()

    print("Это был последний вопрос")
    print("Ваш финальный счет", score)

    #addRecord(userName, score)
    #readRecords()

main()
input("\n\nНажмите Enter чтобы выйти.")

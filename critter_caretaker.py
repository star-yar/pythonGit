# Critter Caretaker
# A virtual pet to care for

import random

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        print(self.name, 'появился на свет')

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def __str__(self):
        rep = "Объект класса Critter\n"
        rep+='имя: '+str(self.name)+'\n'
        rep+='голод: '+str(self.hunger)+'\n'
        rep+='скука: '+str(self.boredom)+'\n'
        return rep
        
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "замечательно"
        elif 5 <= unhappiness <= 10:
            m = "посредственно"
        elif 11 <= unhappiness <= 15:
            m = "плохо"
        else:
            m = "ужасно"
        return m
            
    def talk(self):
        print("Я ", self.name, ",и я увствую себя ", self.mood, ".\n")
        self.__pass_time()
    
    def eat(self, food):
        print("Ммм...  Спасибо.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
        

    def play(self, fun):
        print("Уррра!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    critters=[]
    
    print('Сколько зверей хотите на ферме? ', end='')
    nCrits=int(input())
    
    if nCrits>1:
        critList=[]
        for i in range(0, nCrits):
            hunger=random.randint(0,3)
            boredom=random.randint(0,3) 
            crit_name = input("Как назовете новую зверушку?: ")
            crit = Critter(crit_name, hunger, boredom)
            critList.append(crit)
    else:
        crit_name = input("Как назовете новую зверушку?: ")
        crit = Critter(crit_name)
    
    choice = None  
    while choice != "0":
        print \
        ("""
        Тамагочи
    
        0 - Выйти
        1 - Поговорить со зверушками
        2 - Покормить зверушек
        3 - Поиграть со зверушками
        """)
    
        choice = input("Выбор: ")
        print()

        # exit
        if choice == "0":
            print("Пока-пока.")

        # listen to your critter
        elif choice == "1":
            for i in range(0,nCrits):
                criter=critList[i]
                criter.talk()
        
        # feed your critter
        elif choice == "2":
            food=int(input('Сколько пачек корма дать питомцу? '))
            for i in range(0,nCrits):
                criter=critList[i]
                crit.eat(food)
         
        # play with your critter
        elif choice == "3":
            fun=int(input('Сколько часов поиграем с питомцем? '))
            for i in range(0,nCrits):
                criter=critList[i]
                crit.play(fun)

        elif choice== '11':
            for i in range(0,nCrits):
                criter=critList[i]
                print(criter)

        # some unknown choice
        else:
            print("\nК сожалению", choice, "пункта в меню нет.")

main()
("\n\nPress the enter key to exit.") 

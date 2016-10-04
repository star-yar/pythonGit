# Critter Caretaker
# A virtual pet to care for

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

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
    crit_name = input("Как назовете новую зверушку?: ")
    crit = Critter(crit_name)

    choice = None  
    while choice != "0":
        print \
        ("""
        Тамагочи
    
        0 - Выйти
        1 - Поговорить со зверушкой
        2 - Покормить зверушку
        3 - Поиграть со зверушкой
        """)
    
        choice = input("Выбор: ")
        print()

        # exit
        if choice == "0":
            print("Пока-пока.")

        # listen to your critter
        elif choice == "1":
            crit.talk()
        
        # feed your critter
        elif choice == "2":
            food=int(input('Сколько пачек корма дать питомцу? '))
            crit.eat(food)
         
        # play with your critter
        elif choice == "3":
            fun=int(input('Сколько часов поиграем с питомцем? '))
            crit.play(fun)

        elif choice== '11':
            print(crit)

        # some unknown choice
        else:
            print("\nК сожалению", choice, "пункта в меню нет.")

main()
("\n\nPress the enter key to exit.") 

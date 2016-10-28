print('''
Добро пожаловать в генератор персонажей!
Вам предстоит создать своего героя''')
print('''____________________________________________________\n''')
freePoints=int(30)
print('У вас есть ', freePoints, ' свободных пунктов для распределения\nмежду следующими характеристиками:')

#формируем список хар-к героя
hero=[('Сила   ', 0),
('Ловкость', 0),
('Интеллект', 0),
('Здоровье', 0)]

#выписываем хар-ки
for i in range(len(hero)):
    print('- ',hero[i][0])
print('Распределяйте их с умом. Да прибудет с вами сила!')
print('''____________________________________________________\n''')
input('\nНажмите Enter чтобы начать распределение очков...')

otvet=None
set=None

#чтобы выйти из цикла нужно распределить все свободные поинты
while otvet!=1:
    print('\n\n\n\nСвободные очки \t', freePoints)
    print('\nТекущие характеристики: ')
    print('''_________________________________________\n''')
    for i in range(len(hero)):
        while not set:
            #забрали в переменную (Название хар-ки, её знач.)
            heroChar=hero[i]
            print(heroChar[0],'\t', heroChar[1],end='')
            #тут бы проверку добавить еще на int значение и чтобы больше 0 было
            new=input(' | Новое значение: ')
            new=int(new)
            if new<=freePoints+heroChar[1]:
                freePoints+=int(heroChar[1])
                freePoints-=new
                heroChar=(heroChar[0],new)
                hero[i]=heroChar
                set=1
            elif new>freePoints+heroChar[1]:
                if freePoints>=new:
                    heroChar=(heroChar[0],new)
                    hero[i]=heroChar
                    freePoints-=new
                    set=1
                else:
                    print('\nВам не хватает ', new-heroChar[1]-freePoints, ' свободных очков,\nпопробуйте обновить характеристику...\n')   
        set=None
    print('''_________________________________________''')
    print('\nСвободные очки \t', freePoints)
    
    print('''
 Готово?
  1. Да
  2. Я еще не закончил
''')
    otvet=int(input(' Ваш выбор: '))
    if otvet==1 and freePoints:
        otvet=2
        print('\nУ вас остались свободные очки!')
        input('\nНажмите Enter чтобы продолжить распределение очков...')

print('\n\n\nО чудо, ваш герой готов!')
print('''_________________________________________\n''')
for i in range(len(hero)):
    now=hero[i]
    print(now[0], now[1])
print('''_________________________________________''')
input('\n\n\nНажмите Enter чтобы выйти...')

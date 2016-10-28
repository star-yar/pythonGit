print('''
Добро пожаловать в базу поиска родителей!
У нас Вы можете выполнить поиск отца или деда.''')

base = {'СТАРУХИН ЯРОСЛАВ': 'СТАРУХИН АЛЕКСЕЙ',
              'КУРИЛЬЧЕНКО МАРИНА': 'КУРИЛЬЧЕНКО АНДРЕЙ',
              'СТАРУХИН АЛЕКСЕЙ': 'Старухин Николай',
              'ЛЫКОВ АНДРЕЙ': 'Лыков Игорь',
              'ЦАПКОВА ЕЛЕНА': 'Цапков Анатолий'
        }    
choice=1

while choice:

    print('''
    1. Найти отца
    2. Найти деда

    4. Добавить в базу данных родственную связь
    
    0. Выйти''')
    
    choice=int(input('\nВаш выбор '))

    if choice==1:
        print ('\nЧтобы найти вашего отца в нашей базе,', end='')
        son=input('введите ваше имя: ')
        son=son.upper()
        print('Ваш отец', end=' ')
        print(base.get(son, 'в нашей базе не найден'))
        input('...')
    elif choice==2:
        son=input('введите ваше имя: ')
        son=son.upper()
        print('Ваш дед', end=' ')
        error='в базе не найден'
        dad=base.get(son,error)
        print(base.get(dad,error))
        input('...')
    elif choice==4:
        print('Введите фамилию и имя сына: ', end='')
        nameSon=input()
        nameSon=nameSon.upper()
        if nameSon in base:
            print('Такая запись в БД уже есть: ', end='')
            print('Сын: ', nameSon, 'Отец:' , base[nameSon])
        else:
            print('Введите фамилию и имя отца: ', end='')
            nameDad=input()
            base[nameSon]=nameDad
    elif choice==0:
        input('\nВозвращайтесь еще!')
    else:
        print('\nВыберите один из пунктов меню!')
        #input('...')
        

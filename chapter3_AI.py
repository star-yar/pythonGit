otvet=''

while otvet!='y':
    print('Загадали число от 1 до 100? ', end=' ')
    otvet=input(' y/n? ')

theory=50
interval=50

print('Это ', theory, ' ?    y/n', end=' ')
otvet=input()
if otvet!='n':
    ugadal=1
else:
    ugadal=0
    print('Это больше', theory, ' ?    y/n', end=' ')
    otvet=input()
    if otvet=='n':
        chislo=theory+1
    else:
        chislo=theory-1
while not ugadal:
    if theory<chislo:
        interval=interval//2
        theory-=interval
    elif theory>chislo:
        interval=interval//2
        theory+=interval
    else:
        ugadal=1
    print('Это ', theory, ' ?    y/n', end=' ')
    otvet=input()
    if otvet=='y':
        ugadal=1
    elif otvet=='n':
        print('Это больше', theory, ' ?    y/n', end=' ')
        otvet=input()
        if otvet=='n':
            chislo=theory+1
        else:
            chislo=theory-1
print('Ваше число ',theory, ' угадано')  

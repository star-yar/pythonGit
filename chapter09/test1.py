def type_arg (x):
    if type(x) == int:
        print('int')
    elif type(x) == str:
        print('str')
    else:
        print('empty')


for i in range (1,10):
    x = (input ('Введите х = '))
    type_arg(x)



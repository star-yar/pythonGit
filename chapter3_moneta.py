import random

count0=0
count1=0
al=0

for i in range(0,100):
    rand=random.randrange(2)
    al+=1
    if rand == 1:
        count1+=1
    else:
        count0+=1

p0=count0/al
p1=count1/al

print('Выпало орлов ',count0, '\nВероятность выпадения орла ', p0,'\n')
print('Выпало решек ',count1,'\nВероятность выпадения решки ', p1,'\n')

input()

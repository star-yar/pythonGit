class TV():
    def __init__(self,code,maxChannel=int(5), maxVolume=int(10), channel=int(1), volume=int(0)):
        print('Связь с TV #', code, ' успешно установлена.')
        self.code = code
        self.maxChannel = maxChannel
        self.maxVolume = maxVolume
        self.channel=channel
        self.volume=volume

    def __str__(self):
        rep = '\nСерийный номер: '+self.code+'\n'
        rep +='Текущий канал: '+str(self.channel)+'\n'
        rep +='Текущий уровень громкости: '+str(self.volume)+'\n\n'
        return rep

    def changeChannel (self, channel=0):
        if self.maxChannel<channel:
            print('Превышен диапазон доступных каналов', self.maxChannel)
        else:
            self.channel=channel
        print(self.channel,' Канал')

    def changeVolume (self, volume=0):
        if self.maxVolume<volume:
            print('Превышен диапазон доступной громкости ', self.maxVolume)
        else:
            self.volume=volume
        print('Громкость ', self.volume)
        

def main():
    code=input('Введите серийный номер вашего TV: ')
    newTV=TV(code)

    #задали стартовое значение
    choice=9
    
    while choice:

        print\
            ('''\n
            Управление TV

            1. Сменить канал
            2. Изменить громкость

            0. Отключиться от TV\n
            ''')
        
        choice=int(input('Ваш выбор: '))

        #exit
        if choice == 0:
            print('Отключаю от TV #', newTV.code)

        #сменяем канал    
        elif choice == 1:
            channel=int(input('Какой канал включаем? '))
            newTV.changeChannel(channel)

        #переключаем звук    
        elif choice == 2:
            volume=int(input('Какую громкость поставить? '))
            newTV.changeVolume(volume)

        #тайное инфо о телевизоре     
        elif choice == 11:
            print(newTV)

        #кнтроль ввода     
        else:
            print('Такого пункта меню не было найдено! ')



main()
input('\nНажмите enter чтобы завершить программу...')

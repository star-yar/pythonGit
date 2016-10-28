autoCost=int(input('Цена желаемого авто: '))
autoCostNDS=autoCost*1.2*1.5+30000+15000
print('Цена с НДС составит ', autoCostNDS)
print('\nВ том числе:\n')
print('Цена за доставку ', 30000)
print('Налог ', autoCost*0.5)
print('регистрационный сбор', autoCost*0.2)
print('Агентский сбор ', 15000)
print('')

# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.

NumberOfCoins = int(input('Введите количество монет: '))
avers = 0
revers = 0
print('Введите какая монета лежит вверх орлом, а какая решкой')
for i in range(NumberOfCoins):
    x = int(input('Орел(1) или решка(0)? '))
    if x == 1:
        revers += 1
    else:
        avers += 1
if revers < avers:
    print(f'Переверните {revers} монет с орла на решку, их меньше всего')
elif revers == avers:
    print(f'Количество орлов и решек одинаково, по {revers} штук')
else:
    print((f'Переверните {avers} монет с решки на орла, их меньше всего'))
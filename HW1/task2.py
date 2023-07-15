#Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке


for i in range(2):
    for j in range(2,10):
        for k in range(i*4+2, i*4+6):
            print(f'{k:<2} * {j:<2} = {i * k: < 10}\t', end='')
        print('')
    print('')

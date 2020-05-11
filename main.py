numberCount = input('Until When do i stop?\n')


for x in range(int(numberCount)):
    printerString = ''
    M3, M5 = [False,False]
    if x % 3 == 0:
        printerString += 'Fizz'
    if x % 5 == 0:
        printerString += 'Buzz'
    if printerString == '':
        printerString = x
    print(printerString)

import listpractical

while True:
    int1 = int(input('Enter you first integer here:-'))
    int2 = int(input('Enter you first integer here:-'))

    compare1 = bool(listpractical.less_then(int1, int2))
    compare2 = bool(listpractical.greater_than(int1, int2))
    compare3 = bool(listpractical.equals_to(int1, int2))
    if compare1 is True:
        print(int1, 'is less than', int2)
    elif compare2 is True:
        print(int1, 'is greater than', int2)
    elif compare3 is True:
        print(int1, 'is equal to', int2)
    else:
        print('error')
        break
    print('')
    print('Do you want to continue if yes then enter values')
    print('else'.center(50))
    print('Enter any string')
    print('')

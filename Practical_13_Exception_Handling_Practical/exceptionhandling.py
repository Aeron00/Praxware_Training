try:
    A = int(input('Enter value one:-'))
    B = int(input('Enter value two:-'))

except Exception as e:
    print(e)

else:
    print('Addition:-', A + B)
    print('Subtraction:-', A - B)
    print('Multiplication:-', A * B)
    print('Division:-', A / B)

finally:
    print('Program run successfully'.center(50))

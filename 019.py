try:
    num = int(input('Enter: '))
    print(10 / num)

except ValueError:
    print('please enter the input with type of number')

except ZeroDivisionError:
    print('0 is not good input')

try:
    input1 = int(input('Write the number from where to start:'))
    input2 = int(input('Write the end of the number you need:'))
    print()
    print('Multiplication table of', input1)
    for i in range(input1, input2 + 1):
        print(input1, 'x', i, '=', input1*i)
except:
    print("Input proper convention.")
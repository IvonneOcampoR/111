#method on the top
def separator():
    print(40 * '-')

def menu():
    print(5 * '\n')
    separator()
    print('Welcomr to PyCalc')
    separator()

    print('[1] - Add')
    print('[2] - Substract')
    print('[3] - Multiply')
    print('[4] - Divide')
    print('[x] - Exit')

#instruction on the bottom

opc = ''
while(opc != 'x'):
    menu ()
    opc = input('Select an option: ')

    if(opc == 'x'):
        break

    num1 = float(input('First number: '))
    num2 = float(input('Second number: '))
   
    if(opc == '1'):
       res = num2 + num2
       print('Sum = ' + str(res))

    elif(opc == '4'):
        if(num2 == 0):
            print("Error: Dividing by 00 it's not allowed")
        else:
            res = num1 / num2
            print('Div = ' + str(res))


    input('Press Enter to continue... ')

    print('Thank you!!')
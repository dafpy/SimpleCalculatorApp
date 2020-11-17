while True:
    epilogi = input('Press Enter to continue, or q to exit.')
    if epilogi == 'q':
        break
    
    
    first_number = int(input('Give the first number: '))
    second_number = int(input('Give the second number: '))
    telestis = input('Give the operator (+, -, *, /): ')
    apotelesma = 0

    if telestis == '+':
        apotelesma = first_number + second_number
        print(apotelesma)
    elif telestis == '-':
        apotelesma = first_number - second_number
        print(apotelesma)
    elif telestis == '*':
        apotelesma = first_number * second_number
        print(apotelesma)
    elif telestis == '/':
        apotelesma = first_number / second_number
        print(apotelesma)
    else:
        print('Wrong operator.')
        
print('Exit')

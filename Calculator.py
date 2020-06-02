def welcome():
    print('''Welcome to calculator.''')
    print ('')
welcome()
#define our function
def calculate():
    operation = input('''Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
    number1 = int(input('Input the first number please!:'))
    number2 = int(input('Input the second number please!:'))

    #Adicao
    if operation == '+':
        print ('{} + {} ='.format(number1,number2))
        print (number1+number2)

    #Subtracao
    elif operation =='-':
        print ('{} - {} ='.format(number1,number2))
        print (number1-number2)

    #divisao
    elif operation =='/':
        print ('{} / {} ='.format(number1,number2))
        print (number1/number2)

    #multiplicacao
    elif operation =='/':
        print ('{} * {} ='.format(number1,number2))
        print (number1+number2)
    else:
        print('')
        print('You have not typed a valid operator')
 # Add again() function to calculate() function
    again()
def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    # Accept 'y' or 'Y' by adding str.upper()
    if calc_again.upper() == 'Y':
        calculate()

    # Accept 'n' or 'N' by adding str.upper()
    elif calc_again.upper() == 'N':
        print('See you later.')

    else:
        again()
...

# Call calculate() outside of the function
calculate()

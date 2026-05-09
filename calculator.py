num1 = int(input(('Enter your first number: ')))
operator = (input('Enter your operator: (+,-,*,/ ): '))
num2 = int(input(('Enter your second number: ')))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    if num2 == 0:
        print('Division by 2 is not allowed!') 
    else:
        print(num1 / num2) 
    
#Samuel Wylie 12/9/2023
#modulo recreation without modulo

def modulo(num1, divisor):
    while num1 >= divisor:
        num1 = num1 - divisor
    print(num1)

choice1 = int(input('What is the first number? '))
choice2 = int(input('What is the divisor? '))

modulo(choice1, choice2)

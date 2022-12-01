def add(a,b):
    return f'{a} + {b} = {a+b}'

def subtract(a,b):
    return f'{a} - {b} = {a-b}'

def multiply(a,b):
    return f'{a} * {b} = {a*b}'

def divide(a,b):
    return f'{a} / {b} = {a/b}'

calculator = {
    'Add':add,
    'Subtract':subtract,
    'Multiply':multiply,
    'Divide':divide
}

print('Select Operation.')
for i,option in enumerate(calculator,start=1):
    print(f'{i}. {option}')

choice = list(calculator)[int(input('\nEnter Choice(1/2/3/4): '))-1]

num1 = float(input('\nEnter First Number: '))
num2 = float(input('Enter Second Number: '))
print(calculator[choice](num1,num2))


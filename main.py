#الجزء الاول
my_name = input('what is your name?')
my_age = input('how old are you?')
print(f'my name is {my_name} and i am {my_age} years old')

#الجزء الثاني
first_number = int(input('choose a number'))
second_number = int(input('choose a second number'))
operation = input('choose an operation (+-*/)')
if operation == '+' :
    print(first_number + second_number)
elif operation == '-' :
    print(first_number - second_number)
elif operation == '*' :
    print(first_number * second_number)
elif operation == '/' :
    print(first_number / second_number)
else:
    print('operation is not valid')

    #الجزء الثالث
bus_capacity = 20
people_on_the_bus = int(input('how many people are on the bus?'))
empty_seats = bus_capacity - people_on_the_bus
if empty_seats > people_on_the_bus :
    print(f'there are {empty_seats} empty seats')
elif empty_seats <= people_on_the_bus :
    print('the bus is full')
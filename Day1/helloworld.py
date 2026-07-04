# #Aquí inicia el código de Python
# print("¡Hola, mundo!")
# # Day 1 - 30DaysOfPython Challenge

# print(2 + 3)             # addition(+)
# print(3 - 1)             # subtraction(-)
# print(2 * 3)             # multiplication(*)
# print(3 / 2)             # division(/)
# print(3 ** 2)            # exponential(**)
# print(3 % 2)             # modulus(%)
# print(3 // 2)            # Floor division operator(//)

# # Checking data types
# print(type(10))          # Int
# print(type(3.14))        # Float
# print(type(1 + 3j))      # Complex number
# print(type('Asabeneh'))  # String
# print(type([1, 2, 3]))   # List
# print(type({'name':'Asabeneh'})) # Dictionary
# print(type({9.8, 3.14, 2.7}))    # Set
# print(type((9.8, 3.14, 2.7)))    # Tuple

# name: str = input("What is your name? ")
# print("Hello, " + name + "!")
# print("La longitud de tu nombre es:", len(name))
# print("El tipo de dato de tu nombre es:", type(name))
# first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

# print(first_name, last_name, country, age, is_married)
# print('First name:', first_name)
# print('Last name: ', last_name)
# print('Country: ', country)
# print('Age: ', age)
# print('Married: ', is_married)

# first_name = input('What is your name: ')
# age = input('How old are you? ')

# print(first_name)
# print(age)

# print(type(zip([1,2],[3,4])))

# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)  # Convert the string to a float first
num_int = int(num_float)    # Then convert the float to an integer
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']
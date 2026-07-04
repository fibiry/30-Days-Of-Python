# 'Day 2: 30 Days of python programming'
first_name = 'Santy'
last_name = 'Gonzalez'
full_name = first_name + ' ' + last_name
country = 'Colombia'
city = 'Medellín'
age = 33
year = 2026
is_married = False
is_true = False
is_light_on = False
pet_1 = 'Maggie', pet_2 = 'Chidi', pet_3 = 'Eros'

# Check the data types of the variables
print(type(first_name))  # str 
print(type(last_name))   # str
print(type(full_name))   # str 
print(type(country))     # str
print(type(city))        # str
print(type(age))         # int
print(type(year))        # int
print(type(is_married))  # bool
print(type(is_true))     # bool
print(type(is_light_on)) # bool
print(type(pet_1))       # str
print(type(pet_2))       # str
print(type(pet_3))       # str

#Check the length of a variable
print(len(first_name))  # 5

#compare the length of your first name and your last name
len_first_name = len(first_name)
len_last_name = len(last_name)
difference = len_first_name - len_last_name
print(difference)

#numbers
num_1 = 5
num_2 = 4
total = num_1 + num_2
diff = num_1 - num_2
mult = num_1 * num_2
div = num_1 / num_2
reminder = num_1 % num_2
exp = num_1 ** num_2
print(total, diff, mult, div, reminder, exp)
floor_div = num_1 // num_2
print(floor_div)   
area_of_circle = 3.14 * (30 ** 2)
radius = 30
circum_of_circle = 2 * 3.14 * radius
print(area_of_circle, circum_of_circle)
rad_user = int(input('Enter the radius of a circle: '))
area_of_circle_user = 3.14 * (rad_user ** 2)
print(area_of_circle_user)

#inputs
first_name_user = input('What is your first name? ')
last_name_user = input('What is your last name? ')
full_name_user = first_name_user + ' ' + last_name_user
print(full_name_user)

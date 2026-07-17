# 💻 Exercises: Day 10

# Exercises: Level 1

# Iterate 0 to 10 using for loop, do the same using while loop.

for k in range(11):
    print(k)
print("Esos son los números del 0 al 10 con ciclo for.")

s = 0
while s < 11:
    print(s)
    s += 1
print("Esos son los números del 0 al 10 con ciclo while.")


# Iterate 10 to 0 using for loop, do the same using while loop.

for reverse in range(10, -1, -1):
    print(reverse)
print("Cuenta regresiva método for y range")

countdown = 10
while countdown >= 0:
    print(countdown)
    countdown -= 1
print("Cuenta regresiva método while")

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:

#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######

a = 0
while a <= 7:
    print(
        "#" * a
    )  # Como el primero es vacio porque a = 0, cumple la función de un separador con el ejercicio anterior
    a += 1

# Use nested loops to create the following:

# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #

x = 9
for i in range(x):
    for j in range(x):
        print("#", end=" ")
    print()


# Print the following pattern:

multiplication_number = 0
while multiplication_number < 11:
    print(
        multiplication_number,
        "x",
        multiplication_number,
        "=",
        multiplication_number * multiplication_number,
    )
    multiplication_number += 1
    print()

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

bases = ["Python", "Numpy", "Pandas", "Django", "Flask"]
for item in bases:
    print(item)

# Use for loop to iterate from 0 to 100 and print only even numbers

for even in range(0, 101, 2):
    print(even)

# Use for loop to iterate from 0 to 100 and print only odd numbers

for odd in range(1, 101, 2):
    print(odd)

# Exercises: Level 2

# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.

total = 0
for num in range(101):
    total += num
print(total)


# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

sum_even = 0
for pair in range(0, 101, 2):
    sum_even += pair
sum_odd = 0
for notpair in range(1, 101, 2):
    sum_odd += notpair  # Se mantienen separados por si en el futuro se quiere utilizar como datos aparte

print("La suma de números pares es: ", sum_even)
print("La suma de números impares es: ", sum_odd)

# The sum of all evens is 2550. And the sum of all odds is 2500.

# Exercises: Level 3

# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

from data.countries import countries

word_land = []
for country in countries:
    if "land" in country:
        word_land.append(country)

print(word_land)

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

fruits = ["banana", "orange", "mango", "lemon"]
size = int(len(fruits))
for fruit in range(-1, -size - 1, -1):
    print(fruits[fruit])

# Go to the data folder and use the countries_data.py file.

# What are the total number of languages in the data

from data.countries_data import countries_data

unique_languages = set()
for country in countries_data:
    for language in country.get("languages", []):
        unique_languages.add(language)
total_languages = len(unique_languages)
print(f"Hay en total: {total_languages} idiomas diferentes en nuestros datos")

# Find the ten most spoken languages from the data

from data.countries_data import countries_data

spoken_lang = {}
for each_country in countries_data:
    for lang_count in each_country.get("languages", []):
        if lang_count in spoken_lang:
            spoken_lang[lang_count] += 1
        else:
            spoken_lang[lang_count] = 1

lang_lst = list(spoken_lang.items())
# print(type(lang_lst))
# print(lang_lst)
ordered = sorted(lang_lst, key=lambda times_lang: times_lang[1], reverse=True)
print("Los idiomas más hablados por país son: ", ordered[0:10])

# Find the 10 most populated countries in the world

country_population = {}
for country in countries_data:
    name = country.get("name")
    population = country.get("population", 0)
    if name is not None:
        country_population[name] = population

ordered_pop = sorted(country_population.items(), key=lambda item: item[1], reverse=True)
print("Los países más poblados son:", ordered_pop[0:10])

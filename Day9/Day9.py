# 💻 Exercises: Day 9

# Exercises: Level 1

# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

user_age = int(input("Enter your age: "))
if user_age < 18:
    missing_age = (
        18 - user_age
    )  # Podría añadirse una condición en caso de que el numero ingresado sea menor que 0 para que muestre dato inválido y vuelva a pedir la edad hasta que ingrese un dato >= 0
    print("Debes esperar ", missing_age, "año/s para poder aprender a conducir")
else:
    print(
        "Gracias por confirmar que tienes 18 años o más, ya puedes aprender a conducir"
    )

# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

my_age = 33
your_age = int(input("Ingresa tu edad: "))
age_diff = my_age - your_age
if age_diff == 1:
    print("Yo soy mayor que tu ", age_diff, "año")
elif age_diff > 1:
    print("Yo soy mayor que tu ", age_diff, "años")
elif age_diff == -1:
    print("Tu eres mayor que yo ", age_diff * (-1), "año")
elif age_diff == 0:
    print("Tenemos la misma edad: ", my_age)
else:
    print("Tu eres mayor que yo ", age_diff * (-1), "años")


# Enter your age: 30
# You are 5 years older than me.
# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3

a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
if a > b:
    print("El primer numero es mas grande que el segundo por ", a - b)
elif a == b:
    print("Ambos numeros son iguales")
else:
    print(
        "El segundo numero es mas grande que el primero por: ", (a - b) * (-1)
    )  # Tambien podria ser b - a

# Exercises: Level 2

# Write a code which gives grade to students according to theirs scores:

# ```sh
# 90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F
# ```

student_score = int(input("Ingresa el resultado del estudiante: "))
if student_score >= 0 and student_score < 60:
    print("La calificacion del estudiante es: F")
elif student_score > 59 and student_score < 70:
    print("La calificacion del estudiante es: D")
elif student_score > 69 and student_score < 80:
    print("La calificacion del estudiante es: C")
elif student_score > 79 and student_score < 90:
    print("La calificacion del estudiante es: B")
elif student_score > 89 and student_score < 101:
    print("La calificacion del estudiante es: A")
elif student_score < 0 or student_score > 100:
    print(
        "El resultado del estudiante debe ser entre 0 y 100"
    )  # Todo esto puede funcionar mejor con un ciclo for y el uso de diccionarios

# Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring. June, July or August, the season is Summer.

# months = {
#     "enero": 1,
#     "febrero": 2,
#     "marzo": 3,
#     "abril": 4,
#     "mayo": 5,
#     "junio": 6,
#     "julio": 7,
#     "agosto": 8,
#     "septiembre": 9,
#     "octubre": 10,
#     "noviembre": 11,
#     "diciembre": 12,
# } Quería usar este diccionario en caso de que el usuario ingresara el numero de un mes en lugar de texto para compararlo con la estacion a la que corresponde el mes
seasons = {
    "diciembre": "Invierno",
    "enero": "Invierno",
    "febrero": "Invierno",
    "marzo": "Primavera",
    "abril": "Primavera",
    "mayo": "Primavera",
    "junio": "Verano",
    "julio": "Verano",
    "agosto": "Verano",
    "septiembre": "Otoño",
    "octubre": "Otoño",
    "noviembre": "Otoño",
}
user_month = (
    input("Ingrese un mes: ").strip().lower()
)  # Añadimos una pequeña compación para que el dato sea correcto y para que lo transforme a minúsculas para que coincida con el diccionario que establecimos previamente
if user_month in seasons:
    print("La estación es:", seasons[user_month])
else:
    print("Mes inválido")

# The following list contains some fruits:
# ```sh
fruits = ["banana", "orange", "mango", "lemon"]
# ```

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

user_fruit = input("Ingresa una fruta: ").strip().lower()
if user_fruit in fruits:
    print("Esa fruta ya existe en la lista")
else:
    fruits.append(user_fruit)
    print("La lista se actualizó: ", fruits)

# Exercises: Level 3

# Here we have a person dictionary. Feel free to modify it!
person = {
    "first_name": "Lukas",
    "last_name": "Kyle",
    "age": 888,
    "country": "USA",
    "is_married": True,
    "skills": ["Gaming", "Streaming", "Edición", "Camarografo", "Producción"],
    "address": {"street": "Siempre Viva", "zipcode": "456789"},
}
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

if "skills" in person:
    skills = person["skills"]
    mid_skill = len(skills) // 2
    print(
        "la habilidad de la mitad es: ", skills[mid_skill]
    )  # Se solicita que imprima el texto contenido en el indice que coincide con mid_skill ya que mid_skill por si solo imprime un número
else:
    print("skills no está dentro del diccionario person.")

#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

if "Python" in skills:
    print(
        "Python está en la lista de habilidades: ", skills
    )  # Anteriormente determinamos si skills estaba en el diccionario, partimos de la suposición que si existe
else:
    print("Python no se encuentra entre las habilidades registradas: ", skills)

#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

# front_end = ["JavaScript", "React"]
# back_end = ["Node", "Python", "MongoDB"]
# fullstack = ["React", "Node", "MongoDB"]

if "React" in skills and "Node" in skills and "MongoDB" in skills:
    print(person["first_name"], person["last_name"], "is a fullstack developer")
elif "Node" in skills and "Python" in skills and "MongoDB" in skills:
    print(person["first_name"], person["last_name"], "is a back end developer")
elif "JavaScript" in skills and "React" in skills:
    print(person["first_name"], person["last_name"], "is a front end developer")
else:
    print(
        "unknown title - ",
        person["first_name"],
        person["last_name"],
        "No ha registrado habilidades de desarrollador",
    )  # Ampliamos el print porque la lista de habilidades previamente fué modificada

#  * If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.

is_married = person["is_married"]
country = person["country"]
# Podríamos añador una variable status que sea str y no bool y que se asigne dependiendo de is_married True o False
if is_married == True:
    is_married = "married"
else:
    is_married = "single"
if is_married == "married" and country == "Finland":
    # Print formatted sentence when married and lives in Finland
    print(
        f"{person['first_name']} {person['last_name']} lives in {country}. He is {is_married}"
    )
elif is_married == "single":
    print(
        f"{person['first_name']} {person['last_name']} lives in {country}. He is {is_married}"
    )

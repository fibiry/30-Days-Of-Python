# 💻 Exercises: Day 8

# Create an empty dictionary called dog

dog = dict()

# Add name, color, breed, legs, age to the dog dictionary

dog = {"name": "Tom", "color": "Red", "breed": "Criollo", "legs": 4, "age": 5}
print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student = {
    "first_name": "Dany",
    "last_name": "Rivera",
    "gender": "Female",
    "age": 29,
    "marital status": "married to an alien",
    "skills": ["Fortnite", "Phasmophobia", "The Witcher"],
    "country": ["Colombia", "USA"],
    "city": "El Dorado",
    "address": "Av Siempreviva 568978",
}
print(student)

# Get the length of the student dictionary

print("Este estudiante tiene ", len(student), " datos.")

# Get the value of skills and check the data type, it should be a list

print(
    "Esta ",
    type(student.get("skills")),
    "contiene habilidades en: ",
    student.get("skills"),
)

# Modify the skills values by adding one or two skills

student["skills"].append("Subnáutica")
student["skills"].append("Left 4 Dead")
print(
    "La lista de habilidades de ",
    student["first_name"],
    "ha sido actualizada por: ",
    student["skills"],
)

# Get the dictionary keys as a list

print("La lista de llaves es: ", list(student.keys()))

# Get the dictionary values as a list

print("Los datos del estudiante son: ", list(student.values()))

# Change the dictionary to a list of tuples using items() method

print(list(student.items()))

# Delete one of the items in the dictionary

student_bkp = student.copy()
if student_bkp.get("last_name"):
    student_bkp.pop("last_name")
    print("Se ha borrado el apellido del estudiante ", student["first_name"])
else:
    print("No se encontró el dato solicitado")

# Delete one of the dictionaries

del student_bkp

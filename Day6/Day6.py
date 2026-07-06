# Ecercices level 1 Day 6

# 1. Create an empty tuple

empty_tpl = ()
if empty_tpl == ():
    print("Tupla vacía")

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
bros = ("Thor", "Loki", "Ares")
sis = ("Athenea", "Afrodita")
print("Hermanos: ", bros, "Hermanas: ", sis)

# 3. Join brothers and sisters tuples and assign it to siblings

siblings = tuple(bros + sis)
print("Todos los hermanos y hermanas: ", siblings)

# 4. How many siblings do you have?

total_sib = len(siblings)
print("Tengo en total ", total_sib, "hermanos y hermanas.")

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members

total_list = list(siblings)
total_list.append("Zeus")
total_list.append("Era")
family_members = total_list
family_members = tuple(family_members)
print(
    "Mis hermanos y hermanas son: ",
    siblings,
    "mi padre es: ",
    family_members[-2],
    "mi madre es: ",
    family_members[-1],
    "Y todos los miembros de mi familia son: ",
    family_members,
)

# Exercises: Level 2

# 1. Unpack siblings and parents from family_members

member1, *rest = family_members

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

veg = ("Cebolla", "Zanahoria", "Papa")
fru = ("Tomate", "Aguacate", "Pepino")
ani = ("Costilla", "Solomito", "Hígado", "Chuleta")
food_stuff_tp = veg + fru + ani
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list

food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

food_stuff_lt.pop(len(food_stuff_lt) // 2)
print("La lista sin el producto de la mitad queda así:", food_stuff_lt)

# Slice out the first three items and the last three items from food_stuff_lt list

print(
    "Los primeros 3 productos son: ",
    food_stuff_lt[:3],
    " y los últimos 3 son: ",
    food_stuff_lt[-3:],
)

# Delete the food_stuff_tp tuple completely

del food_stuff_tp

# Check if an item exists in tuple:
try:
    is_empty = (
        "Cebolla" in food_stuff_tp
    )  # The tuple food_stuff_tp was deleted before so it will show an error

    if is_empty == True:
        print("Se encontró el producto en la lista")
except NameError:
    print("La lista está vacía porque ya se eliminó")


# Check if 'Estonia' is a nordic country

nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")

print("Estonia" in nordic_countries)

# Check if 'Iceland' is a nordic country

print("Iceland" in nordic_countries)

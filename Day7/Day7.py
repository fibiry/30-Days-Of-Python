# 💻 Exercises: Day 7

# # sets

it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1

# Find the length of the set it_companies

print("El set tiene ", len(it_companies), "elementos")

# Add 'Twitter' to it_companies

it_companies.add("Twitter")
print(it_companies)

# Insert multiple IT companies at once to the set it_companies

more_companies = ["Nvidia", "OpenAI", "Discord"]
it_companies.update(more_companies)
print(it_companies)

# Remove one of the companies from the set it_companies

removed_form_companies = it_companies.pop()
print("Se ha removido ", removed_form_companies, "del set")
print("El set actualizado es: ", it_companies)
manual_remove = it_companies.remove(
    "Oracle"
)  # I wanted to practice both methods in the same exercice but this can cause an error because pop() could removes this element before so we can still use it_companies.discard("Oracle") to avoid errors
print("Se decidió remover Oracle del set. El set actualizado es: ", it_companies)

# What is the difference between remove and discard

print("""La diferencia entre remove y discard es que 
      si al hacer remove no se encuentra el elemento que se desea eliminar del set, 
      aparecerá un error, mientras que al usar discard
      no saltará error
      """)

# Exercises: Level 2

# Join A and B

C = A | B
print("El resustado de unir A y B es:", C)

# Find A intersection B

inter = A.intersection(B)
print("La intersección de A y B es: ", inter)

# Is A subset of B

if A.issubset(B):
    print("A es un subset de B")
else:
    print("A NO es un subset de B")

# Are A and B disjoint sets

print("Son A y B sets sin elementos en común?... la respuesta es: ", A.isdisjoint(B))

# Join A with B and B with A

join_a = A.union(B)
join_b = B.union(A)
print("A + B es: ", join_a, "... B + A es: ", join_b)


# What is the symmetric difference between A and B

sym_diff = A.symmetric_difference(B)
print("La diferencia simétrica entre A y B es: ", sym_diff)

# Delete the sets completely

del A
del B

try:
    if not A == {} and not B == {}:
        print("A y B todavía existen")
except NameError:
    print("A y B fueron destruidos")

# Exercises: Level 3

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?

age_st = set(age)
len_age_st = len(age_st)
len_age_lst = len(age)
if len_age_st > len_age_lst:
    print("El set es más largo que la lista: ", len_age_st, "VS ", len_age_lst)
else:
    print("La lista es más larga que el set: ", len_age_lst, "VS ", len_age_st)

# Explain the difference between the following data types: string, list, tuple and set
print("""Las diferencias entre string, list, tuple y set:
- string: cadena de texto ordenada e indexada. No se puede modificar directamente.
- list: colección ordenada, indexada, modificable y permite duplicados.
- tuple: colección ordenada, indexada, no modificable y permite duplicados.
- set: colección no ordenada, no indexada, modificable y no permite duplicados.
""")

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

phrase_lst = "I am a teacher and I love to inspire and teach people"
word_by_word = phrase_lst.split()
phrase_st = set(word_by_word)
print("En total hay ", len(phrase_st), "palabras únicas en la frase: ", phrase_lst)

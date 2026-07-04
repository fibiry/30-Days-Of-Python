# my_age = 33
# mi_altura = 1.80
# complex_number = 3 + 4j
# base = int(input("Ingrese la base: "))
# altura = int(input("Ingrese la altura: "))
# area = base * altura / 2
# print("El área del triángulo es:", area)

# #perímetro
# lado1 = int(input("Ingrese el primer lado: "))
# lado2 = int(input("Ingrese el segundo lado: "))
# lado3 = int(input("Ingrese el tercer lado: "))
# perimetro = lado1 + lado2 + lado3
# print("El perímetro del triángulo es:", perimetro)

# #area de un rectángulo
# largo = int(input("Ingrese el largo: "))
# ancho = int(input("Ingrese el ancho: "))
# area_rectangulo = largo * ancho
# print("El área del rectángulo es:", area_rectangulo)

# #area de un círculo
# pi = 3.14159
# radio = int(input("Ingrese el radio del círculo: "))
# area_circulo = pi * (radio ** 2)
# print("El área del círculo es:", area_circulo)

# #circunferencia de un círculo
# circunferencia = 2 * pi * radio
# print("La circunferencia del círculo es:", circunferencia)

# #slope
# x_intercept = int(input("Ingrese la intersección en x: "))
# y_intercept = int(input("Ingrese la intersección en y: "))

# #python vs dragon
# vs = len("python") > len("dragon")
# print("¿La longitud de 'python' es mayor que 'dragon'?", vs)   
# print("'on' in 'python' and 'dragon':", 'on' in 'python' and 'dragon')
# print("'jargon' in 'I hope this course is not full of jargon.':", 'jargon' in 'I hope this course is not full of jargon.')
# print("not 'on' in 'python' and not 'dragon':", not 'on' in 'python' and not 'dragon')


# cfx = len('python')
# floatincfx = float(cfx)
# real = str(floatincfx)
# print("La longitud de 'python' como número flotante es:", real)


# #es divisible entre 2
# num = int(input("Ingrese un número: "))
# if num % 2 == 0:
#     print(num, "es divisible entre 2.")
# else:
#     print(num, "no es divisible entre 2.")

# #converted value

# a = 7 % 3
# b = int(2.7)
# if a == b:
#     print("El valor convertido es igual a 2.")
# else:
#     print("El valor convertido no es igual a 2.")

# #type comparison
# c = type('10')
# d = type(10)
# if c == d:
#     print("Los tipos son iguales.")
# else:
#     print("Los tipos no son iguales.")

# try:
#     e = int(float('9.8'))
# except ValueError:
#     e = None
# if e == 10:
#     print("El valor convertido es igual a 10.")
# else:
#     print("El valor convertido no es igual a 10.")

# #payment calculation
# hours = int(input("Ingrese el número de horas trabajadas: "))
# rate = int(input("Ingrese la tarifa por hora: "))
# payment = hours * rate
# print("El pago es:", payment)

# #seconds of life
# years = int(input("Ingrese su edad en años: "))
# seconds = years * 365 * 24 * 60 * 60
# print("El número de segundos que has vivido es:", seconds)

#exponential table
# for i in range(1, 6):
#     for j in range(0, 5):
#         print(i ** j, end=" ")
#     print()
    
for i in range(1, 6):
    #for j in range(0, 5):
    print(i ** 1, i ** 0, i ** 1, i ** 2, i **  3, end=" ")
    print()
    
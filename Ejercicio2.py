Nombre = input("Dime tu nombre y apellido ")
primero= Nombre.split()
print(primero[0])
palabra = input("Dime una palabra ")
vocal = input("Dime una vocal ")
mayus = vocal.upper()
print(palabra.replace(vocal,mayus))
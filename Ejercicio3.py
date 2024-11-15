numero = int(input("Dime un numero entero positivo "))
if numero%2 == 0:
    print(numero, "es par")
else:
    print(numero, "es impar")
entero = int(input("Dime un numero entero "))
lista=[]
for i in range(1,entero+1):
    x= i*3 
    lista.append(x)
print(lista)
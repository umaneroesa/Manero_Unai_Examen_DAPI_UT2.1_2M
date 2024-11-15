def area_cuadrado (lado):
    """Funcion calculo area de un cuadrado segun longitud.
    
    Parametros
    lado: longitud de un lado
    Devuelve el area de un cuadrado con esa longitud
    """
    return lado*lado
medida= int(input("Dime la longitud de un lado "))
print(area_cuadrado(medida))

def mayor_de_tres(a, b, c):
    """Funcion mayor numero de tres.

    Parametros
    a, b, c: tres numeros
    Salida: el mayor de los tres numeros
    """
    if a<b<c:
        print(a)
    elif b<c<a:
        print(b)
    else:
        print(c)
d=int(input("Dime un numero "))
e=int(input("Dime un segundo numero "))
f=int(input("Dame un tercer numero "))
mayor_de_tres(d, e, f)
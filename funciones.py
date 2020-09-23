def cuadrado(a:int)->int:
    return a * a

def triangulo(a:int, b:int)->int:
    return (a * b) / 2

def circulo(a:int)->int:
    return 3.14 * (a * a)

print("Area del cuadrado")
lado = int(input("Ingresa el valor del lado: "))
print("El area del cuadrado es: ", cuadrado(lado))

print("Area del triangulo")
base = int(input("Ingresa el valor de la base: "))
alt = int(input("Ingresa el valor de la altura: "))
print("El area del triangulo es: ", triangulo(base, alt))

print("Area del circulo")
radio = int(input("Ingresa el valor del radio: "))
print("El area del circulo es: ", circulo(radio))
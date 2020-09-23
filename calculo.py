def fact(a:int)->int:
    r = 1
    while a > 1:
        r = r * a
        a = a - 1
    return r

print(fact(3))


limite = 10
n = 0
e = 0
while n < limite:
    e += 1/fact(n)
    n = n + 1
    print("Valor de e: ", e)
   


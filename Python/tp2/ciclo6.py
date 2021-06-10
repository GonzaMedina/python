mayor = int(input("ingrese un numero"))

for i in range(1,15):
    numero = int(input('ingrese un numero'))
    if(numero > mayor):
        mayor = numero

print('el mayor es', mayor)
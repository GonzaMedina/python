from random import randint


numeros = []

for i in range (0,78):
    numero1 = randint(1,77)
    numeros.append(numero1)

numeros.sort()

print ("El menor de la lista es",numeros[0])
print ("El mayor de la lista es",numeros[77])

print(numeros)
for lista in range (0,78):
    if (lista % 2==0):
        print(lista)
maximo = int(input("ingrese numero")) 

for i in range(0,4):
    numero= int(input("ingrese un numero"))


    if(numero > maximo):
        maximo =numero
    print(maximo, numero)

print("el numero maximo es", maximo)
numero = int(input("Ingrese un número: "))
if(numero % 2 == 0):
    print("El número es multiplo de 2.", "Elevado al cubo daría: ", (numero ** 3))
elif(numero % 5 == 0):
    print("El número es multiplo de 5.", "Elevado al cubo daría: ", (numero ** 3))
else:
    print("El número no es divisible por 2 ni por 5")
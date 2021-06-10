numero1 = int(input("Ingrese el número 1: "))
numero2 = int(input("Ingrese el número 2: "))
numero3 = int(input("Ingrese el número 3: "))
if(numero1 > numero2 and numero1 > numero3):
    print("El número", numero1, "es el mayor")
elif(numero2 > numero1 and numero2 > numero3):
    print("El número ", numero2, "es el mayor")
else:
    print("El numero " , numero3 , "es el mayor")
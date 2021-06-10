numero = int(input("ingrese un numero")) 
i = 0
positivos=0
negativos=0

while (numero != 0):
    if(numero > 0):
        positivos +=1
    else:
        negativos+=1
    numero= int(input("ingrese un numero"))
print("cantidad de positivos", positivos)
print("cantidad de negativos", negativos)
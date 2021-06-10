nu_mes = int(input("Ingrese el número de mes: "))
if(nu_mes == 1 or nu_mes == 3 or nu_mes == 5 or nu_mes == 7 or nu_mes == 8 or nu_mes == 10 or nu_mes == 12):
    print("El mes tiene 31 días")
elif(nu_mes == 2):
    print("El mes tiene 28 días")
elif(nu_mes == 4 or nu_mes == 6 or nu_mes == 9 or nu_mes == 11):
    print("El mes tiene 30 días")
else:
    print("Wacho, ese mes no existe.")
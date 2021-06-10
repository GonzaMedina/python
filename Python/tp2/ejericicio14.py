cant_dias = int(input("Ingrese la cantidad de días: "))
nu_mes = int(input("Ingrese el número de mes: "))
if(nu_mes > 12):
    print("El mes no existe")
if((nu_mes == 1 or nu_mes == 3 or nu_mes == 5 or nu_mes == 7 or nu_mes == 8 or nu_mes == 10 or nu_mes == 12) and (cant_dias <= 31)):
    print("La cantidad de días coinciden con el mes indicado.")
elif((nu_mes == 2) and (cant_dias <= 28)):
    print("La cantidad de días coinciden con el mes indicado.")
elif((nu_mes == 4 or nu_mes == 6 or nu_mes == 9 or nu_mes == 11) and (cant_dias <= 30)):
    print("La cantidad de días coinciden con el mes indicado.")
else:
    print("La cantidad de días no coinciden con el mes.")
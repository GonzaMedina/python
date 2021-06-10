escala = input("Ingrese la inicial de la escala (F o C): ")
temperatura = float(input("Ingrese la temperatura: "))
if(escala == "c"):
    print("La temperatura en Farenheit es: ", ((temperatura * 9 / 5) + 32))
elif(escala == "f"):
    print("La temperatura en Centigrados es: ", ((temperatura - 32) * 5 / 9))
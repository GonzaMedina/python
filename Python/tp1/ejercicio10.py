#Determinar cuánto demora una persona en ir en bicicleta de un lugar a otros, suponiendo
#que esta se mueve a una velocidad constante y se conocen la cantidad de kilómetros del
#camino.


print("La bicicleta se mueve a 5KM/h")
velocidad = 5
cant_kilom = int(input("Ingrese la cantidad de kilometros a recorrer: "))

print("La bicicleta tardará", round(cant_kilom / velocidad), "horas")
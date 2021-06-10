#Calcular el promedio de temperatura y presión recolectado por una estación
#meteorológica en una semana, considerando que realiza solo una medición al día.


temp_dia_uno = float(input("Ingrese la temperatura del Domingo: "))
presion_dia_uno = float(input("Ingrese la presión del Domingo: "))
temp_dia_dos = float(input("Ingrese la temperatura del Lunes: "))
presion_dia_dos = float(input("Ingrese la presión del Lunes: "))
temp_dia_tres = float(input("Ingrese la temperatura del Martes: "))
presion_dia_tres = float(input("Ingrese la presión del Martes: "))
temp_dia_cuatro = float(input("Ingrese la temperatura del Miercoles: "))
presion_dia_cuatro = float(input("Ingrese la presión del Miercoles: "))
temp_dia_cinco = float(input("Ingrese la temperatura del Jueves: "))
presion_dia_cinco = float(input("Ingrese la presión del Jueves: "))
temp_dia_seis = float(input("Ingrese la temperatura del Viernes: "))
presion_dia_seis = float(input("Ingrese la presión del Viernes: "))
temp_dia_siete = float(input("Ingrese la temperatura del Sabado: "))
presion_dia_siete = float(input("Ingrese la presión del Sabado: "))

print("El promedio de temperatura es: ", (temp_dia_uno + temp_dia_dos + temp_dia_tres + temp_dia_cuatro + temp_dia_cinco + temp_dia_seis + temp_dia_siete) / 7)
print("El promedio de temperatura es: ", (presion_dia_uno + presion_dia_dos + presion_dia_tres + presion_dia_cuatro + presion_dia_cinco + presion_dia_seis + presion_dia_siete) / 7)


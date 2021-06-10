#Una empresa telefónica debe facturar el costo de las llamadas telefónicas a sus cliente
#para esto les cobra por tiempo de llamada (por minuto) pero además le adiciona un 0,5 %
#del monto total de la llamada.


precio_minuto = float(input("Ingrese el precio por minuto: "))
cant_minutos = int(input("Ingrese la cantidad de minutos: "))

print("El costo total es: ", round((precio_minuto * cant_minutos) * 1.005,1))
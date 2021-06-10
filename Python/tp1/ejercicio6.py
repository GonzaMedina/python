# Una pinturería debe elaborar el presupuesto para un cliente y necesita calcular el costo
# total, este se deriva de la cantidad de pintura requerida y de la mano de obra, teniendo en
# cuenta lo siguiente: se requiere un litro de pintura por m2 y el costo de mano de obra es
# del 45 % del precio total de pintura.


cantidad_m2 = int(input("Ingrese la cantidad de metros cuadrados: "))
precio_pintura = int(input("Ingrese el precio de la pintura: "))

print("El presupuesto sería: ", (cantidad_m2 * precio_pintura) + (cantidad_m2 * precio_pintura * 0.45), "ARS")

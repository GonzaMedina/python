#Una empresa distribuidora de energía le cobrar a sus abonados el consumo de kW por
#hora, pero además debe sumarle el 0,21 % de impuesto, pero actualmente todos los
#cliente están dentro de un plan de promoción que les descuenta el 3,7 % del monto total a
#pagar.

precio_kw = 10
consumo = int(input("Ingrese la cantidad de Kw consumidos: "))

print("El costo total es: ", round(((precio_kw * consumo) * 1.0021) / 1.037,2))
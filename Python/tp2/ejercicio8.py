# Dado el nombre, apellido y año de nacimiento de tres personas mostrar los datos de los que son mayores de edad

monto = float(input("Ingrese el monto de la compra: "))
cuotas = int(input("Ingrese la cantidad de cuotas: "))
tarjeta = input("Ingrese la tarjeta: ")
recargo_visa = 1.07
recargo_master = 1.11
if(cuotas == 3):
    monto = monto * 1.03
elif(cuotas == 8):
    monto = monto * 1.17
elif(cuotas == 12):
    monto = monto * 1.32
if(tarjeta == "visa"):
    recargo_visa = monto * recargo_visa
    print("El monto total es: ", recargo_visa)
elif(tarjeta == "mastercard" ):
    recargo_master = monto * recargo_master
    print("El monto total es: ", recargo_master)











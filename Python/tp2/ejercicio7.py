monto = float(input("ingrese el monto"))
tarjeta = input("ingrese el nombre de la tarjeta")
cuotas = int(input("ingrese el numero e cuotas"))

if(cuotas == 3):
    monto = monto * 1.03
elif(cuotas == 8):
    total = monto * 1.17
elif(cuotas == 12):
    total = monto * 1.32

if(tarjeta == "visa"):
    recargo_visa = monto * 1.07
    print("monto total:", recargo_visa)



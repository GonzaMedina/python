cantidad = 0 
while(True):
    numero = int(input("ingrese el numero de la carta"))
    palo = input("ingrese el palo de la carta")
    cantidad += 1
    if(palo == 'copa' and numero == 7):
        break

print('cantidad de cartas', cantidad)
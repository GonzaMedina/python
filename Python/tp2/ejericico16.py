dd = int(input("Ingrese el número de día: "))
mm = int(input("Ingrese el número de mes: "))
aaaa = int(input("Ingrese el año: "))
if(dd < 31 and mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12):
    print("El día siguiente es: ", (dd + 1), mm, "del año", (aaaa))
if(dd < 30 and mm == 4 or mm == 6 or mm == 9 or mm == 11):
    print("El día siguiente es: ", (dd + 1), mm, "del año", (aaaa))
if(dd < 28 and mm == 2):
    print("El día siguiente es: ", (dd + 1), mm, "del año", aaaa)
if(dd == 31 and mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 and mm != 12):
    print("El día siguiente es: ", "1", mm + 1, "del año", aaaa + 1)
if(dd == 31 and mm == 12):
    print("El día siguiente es: ", "1", "1", "del año", aaaa + 1)
if(dd == 30 and mm == 4 or mm == 6 or mm == 9 or mm == 11):
    print("El día siguiente es: ", "1", "1", "del año", aaaa + 1)
if(dd == 28 and mm == 2):
    print("El día siguiente es: ", 1, "de marzo del año", aaaa)
nota_uno = float(input("ingrese la primer nota"))
nota_dos = float(input("ingrese la segunda nota"))
nota_tres= float(input("ingrese la tercer nota"))

nota_final = round((nota_uno + nota_dos + nota_tres) / 3, 2 )

if(nota_final >=6):
    print("esta aprobado")
else:
    print("esta desaprobado")

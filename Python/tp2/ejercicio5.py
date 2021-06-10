anio_naciemieto = int(input("ingrese año de nacimiento"))
anio_actual = int(input("ingrese fechaactual"))

Edad_de_postulantes = anio_actual - anio_naciemieto 

if(Edad_de_postulantes >22):
    print("es apto para el puesto")
else:
    print("no es apto para el puesto") 
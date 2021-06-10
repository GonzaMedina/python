#Se desea calcular cuántos metros se deben recorreré para atravesar una plaza en diagonal,
#pero solo se conocen las distancia de las cuadras de ambos lados.

from math import sqrt

lado1 = int(input("Ingrese los metros del lado 1: "))
lado2 = int(input("Ingrese los metros del lado 2: "))

diagonal = round(sqrt(lado1 * 2 + lado2 * 2),2)
print(diagonal, "metros")
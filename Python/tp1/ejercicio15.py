#Un grupo de amigos se hospedan en un hotel, y al momento de pagar se dividen los gastos
#de la siguiente manera:
#a. Iván paga el 40 %
#b. German paga el 33 %
#c. Esteban paga el 55 % de lo que pago Iván
#d. Hernán paga el resto
#Determinar cuánto debe pagar cada uno.


gastos_hotel = float(input("Ingrese el total gastado en el hotel: "))
ivan = 0.4
german = 0.33
esteban = (ivan * 0.55)
hernan = (1 - ivan - german - esteban)

print("Ivan tendrá que pagar: $", (gastos_hotel * ivan))
print("German tendrá que pagar: $", (gastos_hotel * german))
print("Esteban tendrá que pagar: $", round((gastos_hotel * esteban),2))
print("Hernan tendrá que pagar: $", round((gastos_hotel * hernan)))

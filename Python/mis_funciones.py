def listado(conjunto_datos):
    for persona in conjunto_datos:
        print(persona)


#! variables primitivas inmutables numericas, string, boolean
def suma(num1, num2, total):
    total = num1 + num2


#! cualquiera que no sea primitiva mutables
def agregar(lista, valor):
    lista[0] = valor
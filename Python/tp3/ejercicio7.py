operaciones = {'+' : suma, '-': resta, '*' : producto, '/': division, '^':potencia}



def calculadora(numero1, operador, numero2):
    if(operador in operaciones):
        return operaciones[operador](numero1, numero2)
    else:
        return None
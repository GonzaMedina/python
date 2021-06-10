def es_palindromo(cadena):
    """determina si una cadena es palindromo"""
    cadena_aux = list(cadena)
    cadena_aux.reverse()
    cadena_invertida = ''
    cadena_invertida = cadena_invertida.join(cadena_aux)

    return cadena_invertida == cadena
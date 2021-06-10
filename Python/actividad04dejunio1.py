from consumo_api import get_charter_by_id

personaje_a = get_charter_by_id(12)
personaje_b= get_charter_by_id(20)

class Persona(object):
    """Clase que representa a una persona."""

    def __init__(self, name):
        self.__name = name

    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        """Cambia el valor del atributo mail."""
        self.__name = name
    
    def mostrar_nombre(self):
        """Muestra los datos de cada persona."""
        print(self.__name,)

personaje1 = Persona(personaje_a['name']) 
personaje2 = Persona(personaje_b['name'])
personaje1.mostrar_nombre()
personaje2.mostrar_nombre()
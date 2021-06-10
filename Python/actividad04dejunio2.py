from consumo_api import get_charter_by_id

personaje1 = get_charter_by_id(20)


class Personaje():
    def __init__(self, nombre=None, nave=None, especie=None):
        self.__nombre = nombre
        self.__nave = nave
        self.__especie = especie

    def mostrar_personaje(self):
        print(self.__nombre, self.__nave, self.__especie)


per1 = Personaje(personaje1["name"], personaje1["starships"], personaje1["species"])

per1.mostrar_personaje()
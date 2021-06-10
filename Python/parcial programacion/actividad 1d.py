from consumo_api import get_charter_by_id, get_all_sw_characters
from random import randint

id_1 = randint(1, 83)
id_2 = randint(1, 83)

personaje1 = get_charter_by_id(id_1)
personaje2 = get_charter_by_id(id_2)

print(personaje1['name'], personaje2['name'])

print('nombres')
if(personaje1['name'] == "Yoda" or personaje1['name'] == "Grevious"):
     print('personaje 1', personaje1['name'])
if(personaje2['name'] == "Yoda" or personaje2['name'] == "Grevious"):
     print('personaje 2', personaje2['name'])

def nombre(item):
     return item['name']
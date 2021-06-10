from consumo_api import get_charter_by_id, get_all_sw_characters
from random import randint
 
id_1 = randint(1, 83)
id_2 = randint(1, 83)

personaje1 = get_charter_by_id(id_1)
personaje2 = get_charter_by_id(id_2)

print(personaje1['name'], personaje2['name'])

print('peliculas')
if(len(personaje1['films']) > len(personaje2['films'])):
     print(personaje1['name'])
elif(len(personaje2['films']) > len(personaje1['films'])):
     print(personaje2['name'])
else:
     print(personaje1['name'], personaje2['name'])
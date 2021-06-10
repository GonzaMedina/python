from consumo_api import get_charter_by_id, get_all_sw_characters
from random import randint

def peso(item):
    if(item['mass'].isdecimal()):
         return float(item['mass'])
    else:
        return 0

id_1 = randint(1, 83)
id_2 = randint(1, 83)

personaje1 = get_charter_by_id(id_1)
personaje2 = get_charter_by_id(id_2)

print(personaje1['name'], personaje2['name'])

 
print('peso')
if(peso(personaje1) > peso(personaje2)):
     print(personaje1['name'])
else:
     print(personaje2['name'])
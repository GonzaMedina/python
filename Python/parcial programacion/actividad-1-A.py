from consumo_api import get_all_sw_characters_names, get_charter_by_id
from consumo_api import altura
from consumo_api import peso
from random import randint

sw_data= get_charter_by_id, get_all_sw_characters_names 

id_1 = randint(1,83),
personaje1 = get_charter_by_id(1)


id_2 = randint(1,83),
personaje2 = get_charter_by_id(2)
if (altura(personaje1) > altura(personaje2)) :
   print ("El personaje mas alto es",personaje1["name"],"la altura es", altura(personaje1))

else:
    print ("El personaje mas alto es",personaje2["name"],"la altura es", altura(personaje2))
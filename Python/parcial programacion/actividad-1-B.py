from consumo_api import get_all_sw_characters_names, get_charter_by_id
from consumo_api import altura
from consumo_api import peso
from random import randint

sw_data= get_charter_by_id, get_all_sw_characters_names 


id1 = randint(1,83),
personaje1 = get_charter_by_id(1)


id2 = randint(1,83),
personaje2 = get_charter_by_id(2)

if (peso(personaje1)) > (peso(personaje2)):

   print ("El personaje mas pesado es",personaje1["name"],"el peso es", altura(personaje1))

else:
    print ("El personaje mas pesado es",personaje2["name"],"el peso es", altura(personaje2))

if (personaje1 == "Yoda" or personaje2 == "Grievous" or  personaje1 == "Grievous" or personaje2 == "Yoda") :
    print(personaje1)
    print(personaje2)
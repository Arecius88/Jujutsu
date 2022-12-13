import random
from Modules import Technique_selecter, OrangeBelt

ukewasa = OrangeBelt.ukewasa()

test = Technique_selecter.technique_selected_random(ukewasa)
print(test)
print(type(test))



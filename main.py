import random
from Modules import uke_wasa, atemi_wasa, kansetsu_wasa, nage_wasa, kihon, kihon_selecter

start = False
uke_wasa = uke_wasa()
atemi_wasa = atemi_wasa()
kansetsu_wasa = kansetsu_wasa()
nage_wasa = nage_wasa()
kihon = kihon()


while start != True:
    choice = input("\nVälj teknikfamilj (Uke wasa, Atemi wasa, Kansetsu wasa, Nage wasa or all kihon):")

    if choice == "u":
        selected_group = kihon_selecter(uke_wasa)
        
        if len(selected_group) == 0:
            start = True


    elif choice == "a":
        selected_group = kihon_selecter(atemi_wasa)
        
        if len(selected_group) == 0:
            start = True
    
    elif choice == "k":
        selected_group = kihon_selecter(kansetsu_wasa)
    
        if len(selected_group) == 0:
            start = True
    
    elif choice == "n":
        selected_group = kihon_selecter(nage_wasa)
        
        if len(selected_group) == 0:
            start = True    
    
    elif choice == "ki":
        selected_group = kihon_selecter(atemi_wasa)
        
        if len(selected_group) == 0:
            start = True        
 
    elif choice == "quit":
        start = True

    else:
        print("Ange teknikfamilj")
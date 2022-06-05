import random
from Modules import uke_wasa, atemi_wasa, kansetsu_wasa, nage_wasa, kihon, kihon_selecter

start = False

#Importerar och konverterar listorna från Modules.py
uke_wasa = uke_wasa()
atemi_wasa = atemi_wasa()
kansetsu_wasa = kansetsu_wasa()
nage_wasa = nage_wasa()
kihon = kihon()

#Loop för att starta valen
while start != True:
    choice = input("\nVälj teknikfamilj (Uke wasa, Atemi wasa, Kansetsu wasa, Nage wasa or all kihon):").lower()

    if choice == "u":
        selected_group = kihon_selecter(uke_wasa)

        #Försök till att lägga till extra val om jag vill fortsätta i samma teknikfamilj. 
        choice2 = input("ny teknik j/n: ").lower() 
        while choice2 == "j":
            selected_group = kihon_selecter(uke_wasa)
            choice2 = input("ny teknik j/n: ").lower()

            if choice2 == "n":
                break 

#Avslutningskriterium.                
            elif len(selected_group) == 0:
                start = True
            
#Behöver lösa denna Else statment - Hoppar tillbaka till första Whileloop
            else:
                print("Svara med j eller n")
      



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
 
    elif choice == "q":
        start = True

    else:
        print("/n Ange teknikfamilj")
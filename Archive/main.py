import random
from Modules import uke_wasa, atemi_wasa, kansetsu_wasa, nage_wasa, kihon, kihon_selecter

start = False
inner_loop_start = False

#Importerar och konverterar listorna från Modules.py (finns säkert smartare sätt att göra detta på)
uke_wasa = uke_wasa()
atemi_wasa = atemi_wasa()
kansetsu_wasa = kansetsu_wasa()
nage_wasa = nage_wasa()
kihon = kihon()


#Loop för att starta valen
while start != True:
    choice = input("\nVälj teknikfamilj (Uke wasa, Atemi wasa, Kansetsu wasa, Nage wasa or all kihon):").lower()

# Choice Uke Wasa
    if choice == "u":
        selected_group = kihon_selecter(uke_wasa)
        inner_loop_start = True
    
        while inner_loop_start == True:
            choice2 = input("\n ny teknik j/n: ").lower()
            
            if choice2 == "j":
                selected_group = kihon_selecter(uke_wasa)
                
                if len(selected_group) == 0:
                    inner_loop_start = False

            if choice2 == "n":
                break 
            
            elif choice2 != "j":  
                print("\n Ange j eller n: ")


# Choice Atemi Wasa
    elif choice == "at":
        selected_group = kihon_selecter(atemi_wasa) 
        inner_loop_start = True
    
        while inner_loop_start == True:
            choice2 = input("\n ny teknik j/n: ").lower()
            
            if choice2 == "j":
                selected_group = kihon_selecter(uke_wasa)
                
                if len(selected_group) == 0:
                    inner_loop_start = False

            if choice2 == "n":
                break 
            
            elif choice2 != "j":  
                print("\n Ange j eller n: ")
                

# Choice Kansetsu Wasa    
    elif choice == "ka":
        selected_group = kihon_selecter(kansetsu_wasa)
        inner_loop_start = True
    
        while inner_loop_start == True:
            choice2 = input("\n ny teknik j/n: ").lower()
            
            if choice2 == "j":
                selected_group = kihon_selecter(uke_wasa)
                
                if len(selected_group) == 0:
                    inner_loop_start = False

            if choice2 == "n":
                break 
            
            elif choice2 != "j":  
                print("\n Ange j eller n: ")
 
                
# Choice Nage Wasa    
    elif choice == "na":
        selected_group = kihon_selecter(nage_wasa)
        inner_loop_start = True
    
        while inner_loop_start == True:
            choice2 = input("\n ny teknik j/n: ").lower()
            
            if choice2 == "j":
                selected_group = kihon_selecter(uke_wasa)
                
                if len(selected_group) == 0:
                    inner_loop_start = False

            if choice2 == "n":
                break 
            
            elif choice2 != "j":  
                print("\n Ange j eller n: ")
                   
# Choice All Kihon    
    elif choice == "ki":
        selected_group = kihon_selecter(atemi_wasa)
        inner_loop_start = True
    
        while inner_loop_start == True:
            choice2 = input("\n ny teknik j/n: ").lower()
            
            if choice2 == "j":
                selected_group = kihon_selecter(uke_wasa)
                
                if len(selected_group) == 0:
                    inner_loop_start = False

            if choice2 == "n":
                break 
            
            elif choice2 != "j":  
                print("\n Ange j eller n: ")
            

            elif choice2 != "j":  
                choice2 = input("ny teknik j/n: ").lower() 
 
 
    elif choice == "q":
        start = True


    else:
        print("\n Ange teknikfamilj")
        
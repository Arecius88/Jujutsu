import random 

#todo rad 77 början på classerna som ska föras över till jujutsu.py

def uke_wasa():
    uke_wasa = ["Ju morote jodan uke, mot svingslag",
                "Jodan uchi uke, mot rakt slag",
                "Gedan uchi uke, mot cirkulär spark",
                "Gedan juji uke, mot knästöt och rak spark", 
                "Morote jodan uke, mot svingslag",
                "Chudan soto uke, mot rakt slag",
                "Gedan soto uke, mot rak spark",
                "Jodan soto uke, mot rakt slag",
                "San ren uke, mot cirkulär spark",
                "Chudan uchi uke, mot rakt slag"]
    return uke_wasa

def atemi_wasa():
    atemi_wasa = ["Shotei uchi, jodan och chudan",
                  "Me uchi, insidan och utsidan",
                  "Gedan geri",
                  "Chudan tski",
                  "Kin geri",
                  "Kizami tski, jodan och chudan",
                  "Mae geri, chudan",
                  "Gyaku tski, chudan",
                  "Hiza geri, chudan",
                  "Mawashi geri, chudan och gedan",
                  "Empi uchi, jodan och chudan",
                  "Uraken uchi , jodan",
                  "Yoko geri, chudan",
                  "Haito uchi, jodan",
                  "Shuto uchi, jodan, höger och vänster sida"]
    return atemi_wasa

def kansetsu_wasa():
    kansetsu_wasa = ["Ude osae, mot grepp i ärmen, ude osae gatame",
                     "Kote gaeshi, mot diagonalt grepp, kote gaeshi gatame",
                     "O soto osae, mot grepp i ärmen, ude henkan gatame",
                     "Kote mawashi, mot grepp i ärmen, kote mawashi gatame",
                     "Shiho nage, mot diagonalt grepp, shiho nage gatame",
                     "Kote hineri, mot diagonalt grepp. ude henkan gatame",
                     "Irimi nage, mot diagonalt grepp, ude henkan gatame",
                     "Waki gatame, mot diagonalt grepp, ude osae gatame",
                     "Hiji gatame, gripa, ude hishigi hiza gatame",
                     "Ude hishigi, gripa",
                     "Kuzure kote gaeshi gatame, gripa",
                     "Ude garami, gripa, kote gatame"]
    return kansetsu_wasa


def nage_wasa():
    nage_wasa = ["O soto otoshi, mot grepp i ärmen, ude hishigi hiza gatame",
            "Ko soto gari, mot grepp i ärmen, ude hishigi hiza gatame",
            "O goshi, mot grepp i ärmen, ude hishigi hiza atame",
            "Ko uchi gari, mot grepp i ärmen, ude hishigi hiza gatame",
            "Seoi nage, mot grepp i ärmen, ude hishigi hiza gatame",
            "Uki otoshi, mot grepp i ärmen, ude henkan gatame",
            "Harai goshi, mot grepp i ärmen, ude hishigi hiza gatame",
            "Sukui nage, mot grepp i ärmen, ude hishigi hiza gatame"]

    return nage_wasa



def kihon():
    kihon = uke_wasa( ) + kansetsu_wasa( ) + atemi_wasa() + nage_wasa()
    return kihon


#Function för att välja teknik och radera teknik från listan.
def kihon_selecter(technic_group):
    technic = random.choice(technic_group)
    print(f"\n Tekniken är: {technic} \n")
    technic_group.remove(technic)
    return technic_group

# * Början på att föra över all kod från ovan functions till class
class YellowBelt():
    def ukewasa():
        ukewasa = ["Ju morote jodan uke, mot svingslag",
                            "Jodan uchi uke, mot rakt slag",
                            "Gedan uchi uke, mot cirkulär spark",
                            "Gedan juji uke, mot knästöt och rak spark"]    
        return ukewasa

    def atemiwasa():
        atemiwasa = ["Shotei uchi, jodan och chudan",
                        "Me uchi, insidan och utsidan",
                            "Gedan geri",]
        return atemiwasa
    
    def kansetsuwasa():
        kansetsuwasa = ["Ude osae, mot grepp i ärmen, ude osae gatame"]
        return kansetsuwasa

           
class OrangeBelt():
    def ukewasa():
        ukewasa = ["Morote jodan uke, mot svingslag",
                    "Chudan soto uke, mot rakt slag",
                    "Gedan soto uke, mot rak spark"]
        ukewasa = YellowBelt.ukewasa() + ukewasa
        return ukewasa
      
    def atemiwasa():
        atemiwasa = ["Chudan tski",
                    "Kin geri"]
        atemiwasa = YellowBelt.atemiwasa()+atemiwasa        
        return atemiwasa
    
    def kansetsuwasa():
        kansetsuwasa = ["Kote gaeshi, mot diagonalt grepp, kote gaeshi gatame",
                        "O soto osae, mot grepp i ärmen, ude henkan gatame",]
        kansetsuwasa = YellowBelt.kansetsuwasa() + kansetsuwasa
        return kansetsuwasa 
    
    def nagewasa():
        nagewasa = ["O soto otoshi, mot grepp i ärmen, ude hishigi hiza gatame"]
        return nagewasa

  
class GreenBelt():
    def ukewasa():
        ukewasa = ["Jodan soto uke, mot rakt slag",
                     "San ren uke, mot cirkulär spark"]
        ukewasa = OrangeBelt.ukewasa() + ukewasa
        return ukewasa
    
    def atemiwasa():
        atemiwasa = ["Kizami tski, jodan och chudan",
                  "Mae geri, chudan"]
        atemiwasa = OrangeBelt.atemiwasa + atemiwasa
        return atemiwasa
    
    def kansetsuwasa(): 
        kansetsuwasa = ["Kote mawashi, mot grepp i ärmen, kote mawashi gatame",
                            "Shiho nage, mot diagonalt grepp, shiho nage gatame",]
        kansetsuwasa = OrangeBelt.kansetsuwasa() + kansetsuwasa
        return kansetsuwasa

    def nagewasa():
        nagewasa = ["Ko soto gari, mot grepp i ärmen, ude hishigi hiza gatame",
            "O goshi, mot grepp i ärmen, ude hishigi hiza atame"]
        nagewasa = OrangeBelt.nagewasa() + nagewasa
        return nagewasa


class BlueBelt():
    def ukewasa():
        ukewasa = [ "Chudan uchi uke, mot rakt slag"]
        ukewasa = GreenBelt.ukewasa + ukewasa
        return ukewasa
    
    def atemiwasa():
        atemiwasa = [ "Gyaku tski, chudan",
                        "Hiza geri, chudan",
                        "Mawashi geri, chudan och gedan"]
        atemiwasa = GreenBelt.atemiwasa() + atemiwasa
        return atemiwasa
    
    def kansetsuwasa ():
        kansetsuwasa = ["Kote hineri, mot diagonalt grepp. ude henkan gatame",
                     "Irimi nage, mot diagonalt grepp, ude henkan gatame",]
        kansetsuwasa = GreenBelt.kansetsuwasa + kansetsuwasa
        return kansetsuwasa
    
    def nagewasa():
        nagewasa =   ["Ko uchi gari, mot grepp i ärmen, ude hishigi hiza gatame"]
        nagewasa = GreenBelt.nagewasa() + nagewasa
        return nagewasa
    
    
class BrownBelt():
    def ukewasa():
        ukewasa = BlueBelt.ukewasa()
        return ukewasa
    def atemiwasa():   
        atemiwasa = ["Empi uchi, jodan och chudan",
                       "Uraken uchi , jodan",
                        "Yoko geri, chudan",]
        atemiwasa = BlueBelt.atemiwasa + atemiwasa
        return atemiwasa
   
    def kansetsuwasa():
        kansetsuwasa = ["Hiji gatame, gripa, ude hishigi hiza gatame"]
        kansetsuwasa = BlueBelt.kansetsuwasa() + kansetsuwasa
        return kansetsuwasa
    
    def nagewasa():
        nagewasa = ["Seoi nage, mot grepp i ärmen, ude hishigi hiza gatame",
                      "Uki otoshi, mot grepp i ärmen, ude henkan gatame",]
        nagewasa = BlueBelt.nagewasa + nagewasa
        return nagewasa
        
    
class FirstDan():
    def ukewasa():
        ukewasa_firstdan = BlueBelt.ukewasa()
        return ukewasa_firstdan
    
    def atemiwasa():
        atemiwasa_firstdan = ["Haito uchi, jodan",
                  "Shuto uchi, jodan, höger och vänster sida"]
        atemiwasa_firstdan = BrownBelt.atemiwasa + atemiwasa_firstdan
        return atemiwasa_firstdan
    
    def kansetsuwasa():
        kansetsuwasa_firstdan = ["Ude hishigi, gripa",
                     "Kuzure kote gaeshi gatame, gripa",
                     "Ude garami, gripa, kote gatame"]
        kansetsuwasa_firstdan = BrownBelt.kansetsuwasa() + kansetsuwasa_firstdan
        return kansetsuwasa_firstdan
        
    def nagewasa ():
        nagewasa = ["Harai goshi, mot grepp i ärmen, ude hishigi hiza gatame",
            "Sukui nage, mot grepp i ärmen, ude hishigi hiza gatame"]
        nagewasa = BrownBelt.nagewasa() + nagewasa
        return nagewasa
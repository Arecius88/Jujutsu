#! Försöker ordna datan i classer. Syfte: lära mig OOP


class YellowBelt():
    def __init__(self, ukewasa, atemiwasa,  kansetsuwasa):
        self.ukewasa = ukewasa
        self.atemiwasa = atemiwasa
        self.kansetsuwasa = kansetsuwasa
        
    def blokeringar(self):
        self.ukewasa = ["Ju morote jodan uke, mot svingslag",
                            "Jodan uchi uke, mot rakt slag",
                            "Gedan uchi uke, mot cirkulär spark",
                            "Gedan juji uke, mot knästöt och rak spark"]    
    
    def slag(self):
        self.atemiwasa = ["Shotei uchi, jodan och chudan",
                        "Me uchi, insidan och utsidan",
                            "Gedan geri",]
    def ledtekniker(self):
        self.kansetsuwasa = ["Ude osae, mot grepp i ärmen, ude osae gatame"]
        
        
        
p1 = YellowBelt(ukewasa, atemiwasa,kansetsuwasa)
print(p1.slag())
        
class OragneBelt(YellowBelt):
     
    ukewasa_orange = ["Morote jodan uke, mot svingslag",
                   "Chudan soto uke, mot rakt slag",
                   "Gedan soto uke, mot rak spark"]

    atemiwasa_orange = ["Chudan tski",
                        "Kin geri"]
    
    kansetsuwasa_orange = []
    
    
    
class GreenBelt():
    ukewasa_green = ["Jodan soto uke, mot rakt slag",
                     "San ren uke, mot cirkulär spark"]
    
    atemiwasa_green = ["Kizami tski, jodan och chudan",
                  "Mae geri, chudan"]
    
    kansetsuwasa_green = []

class BlueBelt():
    ukewasa_blue = [ "Chudan uchi uke, mot rakt slag"]
    
    atemiwasa_blue = [ "Gyaku tski, chudan",
                      "Hiza geri, chudan",
                      "Mawashi geri, chudan och gedan"]
    kansetsuwasa_blue = []

class BrownBelt():
    ukewasa_brown = []
    
    atemiwasa_brown = ["Empi uchi, jodan och chudan",
                       "Uraken uchi , jodan",
                        "Yoko geri, chudan",]
    
    kansetsuwasa_brown = []
    
class FirstDan():
    ukewasa_firstdan = []
    
    atemiwasa_firstdan = ["Haito uchi, jodan",
                  "Shuto uchi, jodan, höger och vänster sida"]
    
    kansetsuwasa_firstdan = []
    

y1 = YellowBelt()

print(type(y1.atemiwasa_yellow))


'''
uke_wasa_yellow = add_ukewasa_yellow
uke_wasa_orange = add_ukewasa_yellow + add_ukewasa_orange 
uke_wasa_green = add_ukewasa_yellow + add_ukewasa_orange + add_ukewasa_green
uke_wasa_blue = add_ukewasa_yellow + add_ukewasa_orange + add_ukewasa_green + add_ukewasa_blue
uke_wasa_brown = uke_wasa_blue
'''
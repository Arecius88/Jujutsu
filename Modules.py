import random 


class Technique_selecter():
    """This class handles all the technique choises. 
    It has two methods, one random and one nonrandom. 
    """

    def technique_selected_random(technique_group):
        """Random selects a technique from the list that was input. 

        Args:
            technique_group (list): list of the techniques you want to display

        Returns:
            str: the element that was removed from the list. 
        """
        technique = random.choice(technique_group)
        #*Are left behind for debugging purposes
        # print(f"\n Tekniken är: {technique} \n")
        technique_group.remove(technique)
        return technique
	
    def technique_selected_nonrandom(self, technique_group):
        """Selects the elemment on index 0 from the list of techniques that was input. 

        Args:
            technique_group (list): list of the techniques you want to display

        Returns:
            str: the element that was removed from the list.
        """
        technique = technique_group[0]
        #*Are left behind for debugging purposes
        # print(f"\nNonrandom tecnic is {technique}\n")
        technique_group.remove(technique)
		
        return technique

class Messages_to_app():
    """This is the class for all the messages that a send to the app. I've chosen to make them constants.  
    """

    def WELCOME_TEXT(self):
        WELCOME_TEXT = f"You have chosen {self}"
        return WELCOME_TEXT
    
    def END_OF_TECHNIQUE_TEXT(self):
        END_OF_TECHNIQUE_TEXT = "Well done. Choose a new technic family"
        return END_OF_TECHNIQUE_TEXT

    def RESET_TECHNIQUE_TEXT(self):
        RESET_TECHNIQUE_TEXT = "You have pressed reset.\nChoose a new technic family"
        return RESET_TECHNIQUE_TEXT
    
    def RESET_SPINNER_TEXT(self):
        RESET_SPINNER_TEXT = "Choose technique family"
        return RESET_SPINNER_TEXT

    def ERROR_MESSAGE(self):
        ERROR_MESSAGE = "Please choose a technique family first"
        return ERROR_MESSAGE

class Progressbar():
    """Class to handle the progressbar max and min values. 
    """

    def minimum(self):
        return 0

    def maximum(self, max_value):
        return len(max_value)

class YellowBelt():
    """Class to handle all the techniques. The methods are the technique families. Every grade have the same layout and adds of from the previous grade. 
    
    """
    def ukewasa():
        ukewasa = ["Ju morote jodan uke, mot svingslag",
                   "Jodan uchi uke, mot rakt slag",
                   "Gedan uchi uke, mot cirkulär spark",
                   "Gedan juji uke, mot knästöt och rak spark"]
        return ukewasa

    def atemiwasa():
        atemiwasa = ["Shotei uchi, jodan och chudan",
                     "Me uchi, insidan och utsidan",
                     "Gedan geri", ]
        return atemiwasa

    def kansetsuwasa():
        kansetsuwasa = ["Ude osae, mot grepp i ärmen, ude osae gatame"]
        return kansetsuwasa

    def all_kihon():
        all_kihon = YellowBelt.ukewasa() + YellowBelt.atemiwasa() +YellowBelt.kansetsuwasa()
        return all_kihon

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
        atemiwasa = YellowBelt.atemiwasa() + atemiwasa
        return atemiwasa

    def kansetsuwasa():
        kansetsuwasa = ["Kote gaeshi, mot diagonalt grepp, kote gaeshi gatame",
                        "O soto osae, mot grepp i ärmen, ude henkan gatame", ]
        kansetsuwasa = YellowBelt.kansetsuwasa() + kansetsuwasa
        return kansetsuwasa


    def nagewasa():
        nagewasa = ["O soto otoshi, mot grepp i ärmen, ude hishigi hiza gatame"]
        return nagewasa


    def all_kihon():
        all_kihon = OrangeBelt.ukewasa() + OrangeBelt.atemiwasa() + OrangeBelt.kansetsuwasa() + OrangeBelt.nagewasa()
        return all_kihon

class GreenBelt():
    def ukewasa():
        ukewasa = ["Jodan soto uke, mot rakt slag",
                   "San ren uke, mot cirkulär spark"]
        ukewasa = OrangeBelt.ukewasa() + ukewasa
        return ukewasa

    def atemiwasa():
        atemiwasa = ["Kizami tski, jodan och chudan",
                     "Mae geri, chudan"]
        atemiwasa = OrangeBelt.atemiwasa() + atemiwasa
        return atemiwasa

    def kansetsuwasa():
        kansetsuwasa = ["Kote mawashi, mot grepp i ärmen, kote mawashi gatame",
                        "Shiho nage, mot diagonalt grepp, shiho nage gatame", ]
        kansetsuwasa = OrangeBelt.kansetsuwasa() + kansetsuwasa
        return kansetsuwasa

    def nagewasa():
        nagewasa = ["Ko soto gari, mot grepp i ärmen, ude hishigi hiza gatame",
                    "O goshi, mot grepp i ärmen, ude hishigi hiza atame"]
        nagewasa = OrangeBelt.nagewasa() + nagewasa
        return nagewasa

    def all_kihon():
        all_kihon = GreenBelt.ukewasa() + GreenBelt.atemiwasa() + GreenBelt.kansetsuwasa() + GreenBelt.nagewasa()
        return all_kihon

class BlueBelt():
    def ukewasa():
        ukewasa = ["Chudan uchi uke, mot rakt slag"]
        ukewasa = GreenBelt.ukewasa() + ukewasa
        return ukewasa

    def atemiwasa():
        atemiwasa = ["Gyaku tski, chudan",
                     "Hiza geri, chudan",
                     "Mawashi geri, chudan och gedan"]
        atemiwasa = GreenBelt.atemiwasa() + atemiwasa
        return atemiwasa

    def kansetsuwasa():
        kansetsuwasa = ["Kote hineri, mot diagonalt grepp. ude henkan gatame",
                        "Irimi nage, mot diagonalt grepp, ude henkan gatame", ]
        kansetsuwasa = GreenBelt.kansetsuwasa() + kansetsuwasa
        return kansetsuwasa

    def nagewasa():
        nagewasa = ["Ko uchi gari, mot grepp i ärmen, ude hishigi hiza gatame"]
        nagewasa = GreenBelt.nagewasa() + nagewasa
        return nagewasa

    def all_kihon():
        all_kihon = BlueBelt.ukewasa() + BlueBelt.atemiwasa() + BlueBelt.kansetsuwasa() + BlueBelt.nagewasa()
        return all_kihon

class BrownBelt():
    def ukewasa():
        ukewasa = BlueBelt.ukewasa()
        return ukewasa

    def atemiwasa():
        atemiwasa = ["Empi uchi, jodan och chudan",
                     "Uraken uchi , jodan",
                     "Yoko geri, chudan", ]
        atemiwasa = BlueBelt.atemiwasa() + atemiwasa
        return atemiwasa

    def kansetsuwasa():
        kansetsuwasa = ["Hiji gatame, gripa, ude hishigi hiza gatame"]
        kansetsuwasa = BlueBelt.kansetsuwasa() + kansetsuwasa
        return kansetsuwasa

    def nagewasa():
        nagewasa = ["Seoi nage, mot grepp i ärmen, ude hishigi hiza gatame",
                    "Uki otoshi, mot grepp i ärmen, ude henkan gatame", ]
        nagewasa = BlueBelt.nagewasa() + nagewasa
        return nagewasa

    def all_kihon():
        all_kihon = BrownBelt.ukewasa() + BrownBelt.atemiwasa() + BrownBelt.kansetsuwasa() + BrownBelt.nagewasa()
        return all_kihon

class FirstDan():
    def ukewasa():
        ukewasa_firstdan = BlueBelt.ukewasa()
        return ukewasa_firstdan

    def atemiwasa():
        atemiwasa_firstdan = ["Haito uchi, jodan",
                              "Shuto uchi, jodan, höger och vänster sida"]
        atemiwasa_firstdan = BrownBelt.atemiwasa() + atemiwasa_firstdan
        return atemiwasa_firstdan

    def kansetsuwasa():
        kansetsuwasa_firstdan = ["Ude hishigi, gripa",
                                 "Kuzure kote gaeshi gatame, gripa",
                                 "Ude garami, gripa, kote gatame"]
        kansetsuwasa_firstdan = BrownBelt.kansetsuwasa() + kansetsuwasa_firstdan
        return kansetsuwasa_firstdan

    def nagewasa():
        nagewasa = ["Harai goshi, mot grepp i ärmen, ude hishigi hiza gatame",
                    "Sukui nage, mot grepp i ärmen, ude hishigi hiza gatame"]
        nagewasa = BrownBelt.nagewasa() + nagewasa
        return nagewasa

    def all_kihon():
        all_kihon = FirstDan.ukewasa() + FirstDan.atemiwasa() + FirstDan.kansetsuwasa() + FirstDan.nagewasa()
        return all_kihon


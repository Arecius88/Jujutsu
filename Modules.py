import random 

def uke_wasa():
    uke_wasa = ["Ju morote jodan uke, mot svingslag",
                "Jodan uchi uke, mot rakt slag",                "Gedan uchi uke, mot cirkulär spark",
                "Gedan juji uke, mot knästöt och rak spark", "Morote jodan uke, mot svingslag",
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


def kihon_selecter(technic_group):
    technic = random.choice(technic_group)
    print(f"\n Tekniken är: {technic} \n")
    technic_group.remove(technic)
    return technic_group





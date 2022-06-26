
add_ukewasa_yellow = ["Ju morote jodan uke, mot svingslag",
                  "Jodan uchi uke, mot rakt slag",
                  "Gedan uchi uke, mot cirkulär spark",
                  "Gedan juji uke, mot knästöt och rak spark"]    
    
add_ukewasa_orange = ["Morote jodan uke, mot svingslag",
                   "Chudan soto uke, mot rakt slag",
                   "Gedan soto uke, mot rak spark"]

add_ukewasa_green = ["Jodan soto uke, mot rakt slag",
                "San ren uke, mot cirkulär spark",]

add_ukewasa_blue = [ "Chudan uchi uke, mot rakt slag"]

add_ukewasa_brown = []


uke_wasa_yellow = add_ukewasa_yellow
uke_wasa_orange = add_ukewasa_yellow + add_ukewasa_orange 
uke_wasa_green = add_ukewasa_yellow + add_ukewasa_orange + add_ukewasa_green
uke_wasa_blue = add_ukewasa_yellow + add_ukewasa_orange + add_ukewasa_green + add_ukewasa_blue
uke_wasa_brown = uke_wasa_blue


'''
#Troligen den metoden jag anävnder för att slå ihop de olika list. 
orange = ukewasa_yellow + ukewasa_organge
print(len(ukewasa_yellow))
print(len(orange))
print(orange)
#yellow_belt = ukewasa_yellow
#orange_belt = ukewasa_organge.extend(ukewasa_yellow)

#print(ukewasa_organge)
#ukewasa_orange = ukewasa_yellow.extend(add_organge_ukewasa)
print(ukewasa_yellow)
orange = ukewasa_yellow.extend(ukewasa_organge)
print(ukewasa_yellow)

orange1=ukewasa_organge.extend(ukewasa_yellow)
print(orange1)
'''



atemiwasa_yellow= ["Shotei uchi, jodan och chudan",
                   "Me uchi, insidan och utsidan",
                   "Gedan geri"], 

nagewasa_yellow = [],

kansetsuwasa_yellow = ["Ude osae, mot grepp i ärmen, ude osae gatame"] 

"""yellow_belt = {
    "ukewasa" : ["Ju morote jodan uke, mot svingslag",
                "Jodan uchi uke, mot rakt slag",
                "Gedan uchi uke, mot cirkulär spark",
                "Gedan juji uke, mot knästöt och rak spark"],
    
    "atemiwasa": ["Shotei uchi, jodan och chudan",
                  "Me uchi, insidan och utsidan",
                  "Gedan geri",] 
            }           


print(yellow_belt)
print(yellow_belt["ukewasa"])

yellow_belt_update = yellow_belt["ukewasa"].pop()
print(yellow_belt_update)
print(yellow_belt["ukewasa"])

for key in yellow_belt:
    print(key)
    
for item in yellow_belt.values():
    print(item)"""
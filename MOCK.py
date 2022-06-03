import random
from Modules import uke_wasa, atemi_wasa, kansetsu_wasa, nage_wasa, kihon

start = False
uke = uke_wasa()


def stop_condition():
    if x == 0:
        start =True



def kihon_group(technic_group):
    technic = random.choice(technic_group)
    print(f"\n Tekniken är {technic} \n")
    #print(len(technic_group))
    technic_group.remove(technic)
    #print(len(technic_group))

    return technic_group


def new_exercise(answer):
    answer = input("New technic? (y/n) ")



    

while start != True:
    val = input("> ")

    if val == "u":
        test1 = kihon_group(uke)
        print(len(test1))


        if len(test1) == 0:
            start = True   


'''
        
        new_exercice =input("New technic? (y/n) ")


        while new_exercice == "y":
            print(random.choice(uke_wasa()))
            new_exercice = input("New technic? (y/n) ")

            if new_exercice == "n":
                break
'''
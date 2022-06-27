from random import choice
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from Modules import uke_wasa, atemi_wasa, kihon, kansetsu_wasa, nage_wasa
from time import sleep


#Todo Make it possible to make choises what grades you want to train for. 


class MainWidget(Widget):
    #defintioner för Kivy
    ukewasa = uke_wasa()
    atemiwasa = atemi_wasa()
    kihon = kihon()
    kansetsuwasa = kansetsu_wasa()
    nagewasa = nage_wasa()
    spinner_choice = StringProperty("0")
    end_of_technic = StringProperty("Well done. Choose a new technic family")
    technic_family_button_text = StringProperty("Choose a technic Family")
    technic_display = StringProperty("0")
    reset_text = StringProperty("You have pressed reset.\nChoose a new technic family")

    # Function for the reset button
    def reset_button(self):
        self.ukewasa = uke_wasa()
        self.atemiwasa = atemi_wasa()
        self.kihon = kihon()
        self.kansetsuwasa = kansetsu_wasa()
        self.nagewasa = nage_wasa()
        self.ids.menu.text = "Home"
        self.ids.technic_displayer_label.text = self.reset_text
        
#Function to select the technics
    def technic_selecter(self, technic_group):
        self.technic = choice(technic_group)
        technic_group.remove(self.technic)
        return technic_group


# Function for the spinner widget
    def on_spinner_select(self, spinner_choice):
        self.welcome_text = f"You have chosen {spinner_choice}"
        self.spinner_choice = spinner_choice
        self.ids.my_progressbar.value = 0

        if spinner_choice == "Home":
            self.ids.technic_displayer_label.text = self.technic_family_button_text 
            
        elif spinner_choice == "Uke Wasa":
            self.ids.technic_displayer_label.text = self.welcome_text

        elif spinner_choice == "Atemi Wasa":
            self.ids.technic_displayer_label.text = self.welcome_text

        elif spinner_choice == "Kansetsu Wasa":
            self.ids.technic_displayer_label.text = self.welcome_text

        elif spinner_choice == "Nage wasa":
            self.ids.technic_displayer_label.text = self.welcome_text

        elif spinner_choice == "All Kihon":
            self.ids.technic_displayer_label.text = self.welcome_text       

    def progressbar_max(self, max_value):
        return len(max_value)
            
# Function for the new technic button
# TODO Add a F-string technics_countdown = f"You have {x}/{y} left" /../ where x = technics left in the list  and y = technics in the list
    def new_technic_button(self):

        if self.spinner_choice == "Home":
            self.ids.technic_displayer_label.text = self.technic_family_button_text

        elif self.spinner_choice == "Uke Wasa":
            self.technic_selecter(self.ukewasa)
            self.ids.technic_displayer_label.text = self.technic         
            
            #Increment the progressbar with 1 to the maximum of def progressbar_max.
            self.ids.my_progressbar.max = self.progressbar_max(uke_wasa())
            self.ids.my_progressbar.value += 1
            
            #Check if the list of technics are empty
            if len(self.ukewasa) == 0:
                self.ids.technic_displayer_label.text = self.end_of_technic
                self.spinner_choice = ""
                self.ukewasa = uke_wasa()
                

        elif self.spinner_choice == "Atemi Wasa":
            self.technic_selecter(self.atemiwasa)
            self.ids.technic_displayer_label.text = self.technic
            
            #Increment the progressbar with 1 to the maximum of def progressbar_max.
            self.ids.my_progressbar.max = self.progressbar_max(atemi_wasa())
            self.ids.my_progressbar.value += 1

            #Check if the list of technics are empty
            if len(self.atemiwasa) == 0:
                self.ids.technic_displayer_label.text = self.end_of_technic
                self.spinner_choice = ""
                self.atemiwasa = atemi_wasa()

        elif self.spinner_choice == "Kansetsu Wasa":
            self.technic_selecter(self.kansetsuwasa)
            self.ids.technic_displayer_label.text = self.technic
            
            #Increment the progressbar with 1 to the maximum of def progressbar_max.
            self.ids.my_progressbar.max = self.progressbar_max(kansetsu_wasa())
            self.ids.my_progressbar.value += 1

            #Check if the list of technics are empty
            if len(self.kansetsuwasa) == 0:
                self.ids.technic_displayer_label.text = self.end_of_technic
                self.spinner_choice = ""
                self.kansetsuwasa = kansetsu_wasa()


        elif self.spinner_choice == "Nage wasa":
            self.technic_selecter(self.nagewasa)
            self.ids.technic_displayer_label.text = self.technic
            
            #Increment the progressbar with 1 to the maximum of def progressbar_max.
            self.ids.my_progressbar.max = self.progressbar_max(nage_wasa())
            self.ids.my_progressbar.value += 1

            if len(self.nagewasa) == 0:
                self.ids.technic_displayer_label.text = self.end_of_technic
                self.spinner_choice = ""
                self.nagewasa = nage_wasa()


        elif self.spinner_choice == "All Kihon":
            self.technic_selecter(self.kihon)
            self.ids.technic_displayer_label.text = self.technic
            
            #Increment the progressbar with 1 to the maximum of def progressbar_max.
            self.ids.my_progressbar.max = self.progressbar_max(kihon())
            self.ids.my_progressbar.value += 1

            #Check if the list of technics are empty
            if len(self.kihon) == 0:
                self.ids.technic_displayer_label.text = self.end_of_technic
                self.spinner_choice = ""
                self.kihon = kihon()
        else:
            pass



class JujutsuApp(App):
    pass


JujutsuApp().run()

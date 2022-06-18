from random import choice
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from Modules import uke_wasa, atemi_wasa, kihon, kansetsu_wasa, nage_wasa
from time import sleep


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
    down_counter_of_technics = StringProperty("-")
    static_technics_left = StringProperty("Technics left: ")
    static_length_of_list = StringProperty("Technics in family")



    def spinner_selected_welcome_text(self):
        self.ids.technic_displayer_label.text = self.welcome_text


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



# Function for the new technic button
    def new_technic_button(self):

        if self.spinner_choice == "Home":
            self.ids.technic_displayer_label.text = self.technic_family_button_text

        elif self.spinner_choice == "Uke Wasa":
            self.ids.technic_list_length.text = str(len(uke_wasa()))
            self.technic_selecter(self.ukewasa)
            self.ids.technic_displayer_label.text = self.technic
            self.ids.length_of_list_counter.text = str(len(self.ukewasa))
            

            if len(self.ukewasa) == 0:
                self.ids.technic_displayer_label.text = self.end_of_technic
                self.spinner_choice = ""
                self.ukewasa = uke_wasa()

        elif self.spinner_choice == "Atemi Wasa":
            self.technic_selecter(self.atemiwasa)
            self.ids.technic_displayer_label.text = self.technic
            self.ids.length_of_list_counter.text = str(len(self.atemiwasa))

            if len(self.atemiwasa) == 0:
                self.ids.technic_displayer_label.text = self.end_of_technic
                self.spinner_choice = ""
                self.atemiwasa = atemi_wasa()

        elif self.spinner_choice == "Kansetsu Wasa":
            self.technic_selecter(self.kansetsuwasa)
            self.ids.technic_displayer_label.text = self.technic
            self.ids.length_of_list_counter.text = str(len(self.kansetsuwasa))

            if len(self.kansetsuwasa) == 0:
                self.ids.technic_displayer_label.text = self.end_of_technic
                self.spinner_choice = ""
                self.kansetsuwasa = kansetsu_wasa()


        elif self.spinner_choice == "Nage wasa":
            self.technic_selecter(self.nagewasa)
            self.ids.technic_displayer_label.text = self.technic
            self.ids.length_of_list_counter.text = str(len(self.nagewasa))

            if len(self.nagewasa) == 0:
                self.ids.technic_displayer_label.text = self.end_of_technic
                self.spinner_choice = ""
                self.nagewasa = nage_wasa()


        elif self.spinner_choice == "All Kihon":
            self.technic_selecter(self.kihon)
            self.ids.technic_displayer_label.text = self.technic
            self.ids.length_of_list_counter.text = str(len(self.kihon))

            if len(self.kihon) == 0:
                self.ids.technic_displayer_label.text = self.end_of_technic
                self.spinner_choice = ""
                self.kihon = kihon()
        else:
            pass



class JujutsuApp(App):
    pass


JujutsuApp().run()

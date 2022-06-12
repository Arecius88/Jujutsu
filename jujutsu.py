from random import choice
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from Modules import uke_wasa, atemi_wasa, kihon, kansetsu_wasa, nage_wasa



class MainWidget(Widget):
    #defintioner för Kivy
    ukewasa = uke_wasa()
    atemiwasa = atemi_wasa()
    kihon = kihon()
    kansetsuwasa = kansetsu_wasa()
    nagewasa = nage_wasa()
    spinner_choice = StringProperty("0")
    end_of_technic = StringProperty("Grattis, välj ny teknikfamilj")
    welcome_text = StringProperty("You have chosen ")
    reset_text = StringProperty("You have pressed reset")

#Function to select the technics

    def technic_selecter(self, technic_group):
        self.technic = choice(technic_group)
        #print(f"\n Tekniken är: {self.technic} \n")
        technic_group.remove(self.technic)
        return technic_group


# Function for the spinner widget
    def on_spinner_select(self, spinner_choice):

        if spinner_choice == "Home":
            self.ids.technic_displayer_label.text = "Choose a technic Family"
            self.spinner_choice = spinner_choice

        elif spinner_choice == "Uke Wasa":
            self.spinner_choice = spinner_choice
            self.ids.technic_displayer_label.text = self.welcome_text + spinner_choice


        elif spinner_choice == "Atemi Wasa":
            self.ids.technic_displayer_label.text = self.welcome_text + spinner_choice
            self.spinner_choice = spinner_choice

        elif spinner_choice == "Kansetsu Wasa":
            self.ids.technic_displayer_label.text = self.welcome_text + spinner_choice
            self.spinner_choice = spinner_choice

        elif spinner_choice == "Nage wasa":
            self.ids.technic_displayer_label.text = self.welcome_text + spinner_choice
            self.spinner_choice = spinner_choice

        elif spinner_choice == "All Kihon":
            self.ids.technic_displayer_label.text = f"You have chosen {spinner_choice}!"
            self.spinner_choice = spinner_choice


# Function for the new technic button
    def new_technic_button(self):
        if self.spinner_choice == "Home":
            print(self.spinner_choice)

        elif self.spinner_choice == "Uke Wasa":
            self.technic_selecter(self.ukewasa)
            self.ids.technic_displayer_label.text = f"Tekniken är {self.technic}"

            if len(self.ukewasa) == 0:
                self.ids.technic_displayer_label.text = self.end_of_technic
                # innebär att jag tvingar användaren att välja en ny teknikfamilj.
                # self.spinner_choice = " "
                self.ukewasa = uke_wasa()

        elif self.spinner_choice == "Atemi Wasa":
            self.technic_selecter(self.atemiwasa)
            self.ids.technic_displayer_label.text = f"Tekniken är {self.technic}"

            if len(self.atemiwasa) == 0:
                self.ids.technic_displayer_label.text = self.end_of_technic
                # innebär att jag tvinga användaren att välja en ny teknikfamilj.
                # self.spinner_choice = " "
                self.atemiwasa = atemi_wasa()

        elif self.spinner_choice == "Kansetsu Wasa":
            self.technic_selecter(self.kansetsuwasa)
            self.ids.technic_displayer_label.text = f"Tekniken är {self.technic}"

            if len(self.kansetsuwasa) == 0:
                self.ids.technic_displayer_label.text = self.end_of_technic
                # innebär att jag tvinga användaren att välja en ny teknikfamilj.
                # self.spinner_choice = " "
                self.kansetsuwasa = kansetsu_wasa()


        elif self.spinner_choice == "Nage wasa":
            self.technic_selecter(self.nagewasa)
            self.ids.technic_displayer_label.text = f"Tekniken är {self.technic}"

            if len(self.nagewasa) == 0:
                self.ids.technic_displayer_label.text = self.end_of_technic
                # innebär att jag tvinga användaren att välja en ny teknikfamilj.
                # self.spinner_choice = " "
                self.nagewasa = nage_wasa()



        elif self.spinner_choice == "All Kihon":
            self.technic_selecter(self.kihon)
            self.ids.technic_displayer_label.text = f"Tekniken är {self.technic}"

            if len(self.kihon) == 0:
                self.ids.technic_displayer_label.text = self.end_of_technic
                # innebär att jag tvinga användaren att välja en ny teknikfamilj.
                # self.spinner_choice = " "
                self.kihon = kihon()
        else:
            print("NOT UKEAWASA")

    # Function for the reset button
#Todo set the Spinner to Home when reset is pressed.
    def reset_button(self):
        self.spinner_choice = "Home"
        self.ukewasa = uke_wasa()
        self.atemiwasa = atemi_wasa()
        self.kihon = kihon()
        self.kansetsuwasa = kansetsu_wasa()
        self.nagewasa = nage_wasa()
        self.ids.technic_displayer_label.text = self.reset_text

        print("reset")


class JujutsuApp(App):
    pass


JujutsuApp().run()

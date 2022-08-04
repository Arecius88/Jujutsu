from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from Modules import YellowBelt, OrangeBelt
from random import choice


#Sakpa en class som hanterar alla byten av skärmar

''' class spinner_handler():
		def on_spinner_select_grades
			Ändra från Home till en grad
			
		def on_spinner_select_technique
			val av teknik som föregående ver av appen. 
'''
def technique_selecter_random(technique_group):
    technique = choice(technique_group)
    print(f"\n Tekniken är: {technique} \n")
    technique_group.remove(technique)
    return technique_group


#Define our different screens
class HomeScreen(Screen):
	def on_spinner_select_grades(self, spinner_value):
		self.spinner_value = spinner_value
		if spinner_value == "Home":
			self.parent.current = "home"

		if spinner_value == "Yellow":
			self.parent.current = "yellow"

		elif spinner_value == "Orange":
			self.parent.current = "orange"

class YellowScreen(Screen):

	#TODO fixa så att YellowScreen kan anävnda sig av Teknikväljaren.

	yellow_ukewasa = YellowBelt.ukewasa()
	yellow_atemiwasa = YellowBelt.atemiwasa()
	yellow_kansetsuwasa	= YellowBelt.kansetsuwasa()

	def on_spinner_select_technique(self, spinner_value):
		self.welcome_text = f"You have chosen {spinner_value}"
		self.spinner_value = spinner_value

		if self.spinner_value == "Uke wasa":
			self.ids.technic_displayer_label.text = self.welcome_text

		elif spinner_value == "Atemi wasa":
			self.ids.technic_displayer_label.text = self.welcome_text


	def new_technic_button(self):

		if self.spinner_value == "Uke wasa":
			self,technique_selecter_random(self.yellow_ukewasa)
			self.ids.technic_displayer_label.text = self.technique

			# Increment the progressbar with 1 to the maximum of def progressbar_max.
			#self.ids.my_progressbar.max = self.progressbar_max()
			self.ids.my_progressbar.value += 1

			# Check if the list of technics are empty
			if len(self.yellow_ukewasa) == 0:
				self.ids.technic_displayer_label.text = self.end_of_technic
				self.spinner_value = ""
				self.yellow_ukewasa = YellowBelt.ukewasa()


class OrangeScreen(Screen):
	pass

class GreenScreen(Screen):
	pass

class BlueScreen(Screen):
	pass

class BrownScreen(Screen):
	pass

class FirstDanScreen(Screen):
	pass

class SecondDanScreen(Screen):
	pass

class ThirdDanScreen(Screen):
	pass

class WindowManager(ScreenManager):
	pass




sm = ScreenManager()
sm.add_widget(HomeScreen(name="home"))
sm.add_widget(YellowScreen(name = "yellow"))


# Designate Our .kv design file
kv = Builder.load_file('screens.kv')


class jujutsu_screenApp(App):
	def build(self):
		return kv



if __name__ == '__main__':
	jujutsu_screenApp().run()
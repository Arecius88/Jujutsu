from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

import Modules
from Modules import YellowBelt, OrangeBelt, Progressbar, Messages_to_app
from random import choice

#TODO: When Kihos is implemented, expand to Jigowasa and REnraku wsa
#TODO: Test Yellow screens for bugs. Then implement it for the rest od the belts.
#Todo: Implement the class Technique selceter from Modules in this program.
#Todo: After that implement a button to chosse between random or not random.



UKEWASA = "Uke wasa"
ATEMIWASA = "Atemi wasa"
KANSETSUWASA = "Kansetsu wasa"
NAGEWASA = "Nage wasa"
KIHON = "Kihon"

'''
____________Not implemented_______________ 
JIGOWASA = "jigowasa"
RENRAKUWASA	= "renrakuwasa"
__________________________________________
'''


#Define our different screens
class HomeScreen(Screen):
	def home_spinner_text(self):
		'''
		This function returns the text that will be displayed in the spinner on the home screen
		:return: The string "Choose grade" is being returned.
		'''
		home_spinner = "Choose grade"
		return home_spinner

	def on_spinner_select_grades(self,spinner_value):
		"""
		When the user selects a value from the spinner, the function `on_spinner_select_grades` is called with the value of
		the spinner as the argument

		:param spinner_value: The value of the spinner that was selected
		"""
		self.spinner_value = spinner_value
		if spinner_value == "Home":
			self.parent.current = "home"

		if spinner_value == "Yellow":
			self.parent.current = "yellow"


		elif spinner_value == "Orange":
			self.parent.current = "orange"

		elif spinner_value == "Green":
			self.parent.current = "green"

		elif spinner_value == "Blue":
			self.parent.current = "blue"

		elif spinner_value == "Brown":
			self.parent.current = "brown"

		elif spinner_value == "1st Dan":
			self.parent.current = "firstdan"


class YellowScreen(Screen):
	yellow_ukewasa = YellowBelt.ukewasa()
	yellow_atemiwasa = YellowBelt.atemiwasa()
	yellow_kansetsuwasa	= YellowBelt.kansetsuwasa()
	yellow_kihon = YellowBelt.all_kihon()
	progressbar = Progressbar()


	def technique_selected_random(self, technique_group):
		"""
		This function takes in a list of techniques and returns a random technique from that list.

		:param technique_group: This is the list of techniques that you want to select from
		"""
		self.technique = choice(technique_group)
		print(f"\n Tekniken är: {self.technique} \n")
		technique_group.remove(self.technique)
		return technique_group


	def on_spinner_select_technique(self, spinner_value):
		"""
		> When the user selects a value from the spinner, the value is passed to the function and the function updates the
		value of the variable `technique` to the value of the spinner

		:param spinner_value: The value of the spinner that was selected
		"""

		#Displays the spinner choice in the label
		self.spinner_value = spinner_value
		WELCOME_TEXT = Messages_to_app.WELCOME_TEXT(spinner_value)

		if self.spinner_value == UKEWASA:
			#Display a message in on the label
			self.ids.technic_displayer_label.text = WELCOME_TEXT

			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = 0

		elif spinner_value == ATEMIWASA:
			self.ids.technic_displayer_label.text = WELCOME_TEXT

			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = 0

		elif spinner_value == KANSETSUWASA:
			self.ids.technic_displayer_label.text = WELCOME_TEXT

			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = 0

		elif spinner_value == NAGEWASA:
		#added an if-statement if HomeScreen spinner is Yellow and if so display an error message.
			if self.manager.get_screen("home").ids.spinner_menu_home.text == "Yellow":
				self.ids.technic_displayer_label.text = f"This grade do not have {self.spinner_value}.\n " \
														f"Please choose an other technique group."
			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = 0
			else:
				self.ids.technic_displayer_label.text = WELCOME_TEXT
				if self.ids.my_progressbar.value > 0:
					self.ids.my_progressbar.value = 0

		elif spinner_value == KIHON:
			self.ids.technic_displayer_label.text = WELCOME_TEXT
			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = 0

	def new_technic_button(self):
		"""
		Function to control the New technic button.
		Checks the value of the spinner and then display the technic family name.
		Thereafter, the functions takes the list of the selected group and runs the technique_selected_random function
		increments the progressbar by 1

		When the list is empty the function resets:
			- Spinner
			- The list of techniques.
		and display a message in the label.
		"""
		try:
			#checks the vaule of the spinner
			if self.spinner_value == UKEWASA:
				#runs the technique selecter function
				self.technique_selected_random(self.yellow_ukewasa)
				#Modules.Technique_selecter.random_technique(self.yellow_ukewasa)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(YellowBelt.ukewasa())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty
				if len(self.yellow_ukewasa) + 1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)

					#resets the list
					self.yellow_ukewasa = YellowBelt.ukewasa()

			elif self.spinner_value == ATEMIWASA:
				#runs the technique selecter function
				self.technique_selected_random(self.yellow_atemiwasa)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(YellowBelt.atemiwasa())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty. +1 is to add one more step in to the
				#click of the button
				if len(self.yellow_atemiwasa) +1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)

					#resets the list
					self.yellow_atemiwasa = YellowBelt.atemiwasa()

			elif self.spinner_value == KANSETSUWASA:
				#runs the technique selecter function
				self.technique_selected_random(self.yellow_kansetsuwasa)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(YellowBelt.kansetsuwasa())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty. +1 is to add one more step in to the
				# click of the button
				if len(self.yellow_kansetsuwasa) +1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)
					#resets the list
					self.yellow_kansetsuwasa = YellowBelt.kansetsuwasa()

			elif self.spinner_value == NAGEWASA:
				#Passes this choise in this grade
				pass

			elif self.spinner_value == KIHON:
				#runs the technique selecter function
				self.technique_selected_random(self.yellow_kihon)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(YellowBelt.all_kihon())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty. +1 is to add one more step in to the
				# click of the button
				if len(self.yellow_kihon) + 1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)

					#resets the list
					self.yellow_kihon = YellowBelt.all_kihon()

		except:
			self.ids.technic_displayer_label.text = Messages_to_app.ERROR_MESSAGE(self)

	def reset_button(self):
		self.ids.my_progressbar.value = 0
		self.yellow_ukewasa = YellowBelt.ukewasa()
		self.atemiwasa = YellowBelt.atemiwasa()
		self.kihon = YellowBelt.all_kihon()
		self.kansetsuwasa = YellowBelt.kansetsuwasa()
		self.ids.technic_displayer_label.text = Messages_to_app.RESET_TECHNIQUE_TEXT(self)
		self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)


	def home_screen_button(self):
		reference_to_home_screen = self.manager.get_screen("home")
		reference_to_home_screen.ids.spinner_menu_home.text = HomeScreen.home_spinner_text(self)
		self.parent.current = "home"


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



# Designate Our .kv design file
kv = Builder.load_file('screens.kv')


class jujutsu_screenApp(App):
	def build(self):
		return kv



if __name__ == '__main__':
	jujutsu_screenApp().run()
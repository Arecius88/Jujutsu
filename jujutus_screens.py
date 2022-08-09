from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from Modules import YellowBelt, OrangeBelt, Progressbar
from random import choice

#TODO: When Kihos is implemented, expand to Jigowasa and REnraku wsa

ukewasa = "Uke wasa"
atemiwasa = "Atemi wasa"
kansetsuwasa = "Kansetsu wasa"
nagewasa = "Nage wasa"
kihon = "kihon"

#Define our different screens
class HomeScreen(Screen):
	def home_spinner_text(self):
		home_spinner = "Choose grade"
		return home_spinner

	def on_spinner_select_grades(self, spinner_value):
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
			print(self.ids.spinner_menu_home.text)

		elif spinner_value == "Orange":
			self.parent.current = "orange"


class YellowScreen(Screen):
	yellow_ukewasa = YellowBelt.ukewasa()
	yellow_atemiwasa = YellowBelt.atemiwasa()
	yellow_kansetsuwasa	= YellowBelt.kansetsuwasa()
	yellow_kihon = YellowBelt.all_kihon()
	progressbar = Progressbar()
	END_OF_TECHNIQUE_TEXT = StringProperty("Well done. Choose a new technic family")
	RESET_TEXT = StringProperty("You have pressed reset.\nChoose a new technic family")
	RESET_SPINNER_TEXT = StringProperty("Choose technique family")



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
		The function is called when the user selects a value from the spinner.
		The function takes the value of the spinner as an argument.
		The function then sets the welcome_text variable to a string that includes the value of the spinner
		and displays that text in the label.
		The function then sets the spinner_value variable to the value of the spinner.

		The function then checks if the value of the spinner is equal to "Uke wasa".
		If it is, the function sets the text of the technic_displayer_label to the welcome_text.
		If it isn't, the function checks if the value of the spinner is equal to "Atemi wasa".
		If it is, the function sets the text of the technic_displayer_label to the welcome_text.
		If it isn't, the function does nothing.

		:param spinner_value: The value of the spinner that was selected
		"""
		#Displays the spinner choice in the label
		self.WELCOME_TEXT = f"You have chosen {spinner_value}"
		self.spinner_value = spinner_value

		if self.spinner_value == ukewasa:
			#Display a message in on the label
			self.ids.technic_displayer_label.text = self.WELCOME_TEXT

		elif spinner_value == atemiwasa:
			self.ids.technic_displayer_label.text = self.WELCOME_TEXT

		elif spinner_value == kansetsuwasa:
			self.ids.technic_displayer_label.text = self.WELCOME_TEXT

		elif spinner_value == nagewasa:
		#added an if-statement if HomeScreen spinner is Yellow and if so display an error message.
			if self.manager.get_screen("home").ids.spinner_menu_home.text == "Yellow":
				self.ids.technic_displayer_label.text = f"This grade do not have {self.spinner_value}.\n " \
														f"Please choose an other technique group."
			else:
				self.ids.technic_displayer_label.text = self.WELCOME_TEXT

		elif spinner_value == kihon:
			self.ids.technic_displayer_label.text = self.WELCOME_TEXT

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
		#checks the vaule of the spinner

		if self.spinner_value == ukewasa:
			#runs the technique selecter function
			self.technique_selected_random(self.yellow_ukewasa)

			#Display a message in the label
			self.ids.technic_displayer_label.text = self.technique

			#Define the progressbar_max.
			self.ids.my_progressbar.max = self.progressbar.maximum(YellowBelt.ukewasa())

			#Increment the progressbar with 1 to the maximum
			self.ids.my_progressbar.value += 1

			# Check if the list of technics are empty
			if len(self.yellow_ukewasa) == 0:
				#Display a message that the list is empty
				self.ids.technic_displayer_label.text = self.END_OF_TECHNIQUE_TEXT

				#Resets the spinner
				self.ids.spinner_menu_grades.text = self.RESET_SPINNER_TEXT

				#resets the list
				self.yellow_ukewasa = YellowBelt.ukewasa()

		elif self.spinner_value == atemiwasa:
			#runs the technique selecter function
			self.technique_selected_random(self.yellow_atemiwasa)

			#Display a message in the label
			self.ids.technic_displayer_label.text = self.technique

			#Define the progressbar_max.
			self.ids.my_progressbar.max = self.progressbar.maximum(YellowBelt.atemiwasa())

			#Increment the progressbar with 1 to the maximum
			self.ids.my_progressbar.value += 1

			# Check if the list of technics are empty
			if len(self.yellow_atemiwasa) == 0:
				#Display a message that the list is empty
				self.ids.technic_displayer_label.text = self.END_OF_TECHNIQUE_TEXT

				#Resets the spinner
				self.ids.spinner_menu_grades.text = self.RESET_SPINNER_TEXT

				#resets the list
				self.yellow_atemiwasa = YellowBelt.atemiwasa()

		elif self.spinner_value == kansetsuwasa:
			# Todo - Klura ut hur jag ska kunna visa en ensam teknik, Just nu visar den inte tekniken alls.
			#runs the technique selecter function
			self.technique_selected_random(self.yellow_kansetsuwasa)

			#Display a message in the label
			self.ids.technic_displayer_label.text = self.technique

			#Define the progressbar_max.
			self.ids.my_progressbar.max = self.progressbar.maximum(YellowBelt.kansetsuwasa())

			#Increment the progressbar with 1 to the maximum
			self.ids.my_progressbar.value += 1

			# Check if the list of technics are empty
			if len(self.yellow_kansetsuwasa) == 0:
				#Display a message that the list is empty
				self.ids.technic_displayer_label.text = self.END_OF_TECHNIQUE_TEXT

				#Resets the spinner
				self.ids.spinner_menu_grades.text = self.RESET_SPINNER_TEXT

				#resets the list
				self.yellow_kansetsuwasa = YellowBelt.kansetsuwasa()


		elif self.spinner_value == nagewasa:
			#Passes this choise in this grade
			pass

	def reset_button(self):
		self.ids.my_progressbar.value = 0
		self.yellow_ukewasa = YellowBelt.ukewasa()
		self.atemiwasa = YellowBelt.atemiwasa()
		self.kihon = YellowBelt.all_kihon()
		self.kansetsuwasa = YellowBelt.kansetsuwasa()
		self.ids.technic_displayer_label.text = self.RESET_TEXT
		self.ids.spinner_menu_grades.text = self.RESET_SPINNER_TEXT


	def home_screen_button(self):
		reference_to_home_screen = self.manager.get_screen("home")
		reference_to_home_screen.ids.spinner_menu_home.text = HomeScreen.home_spinner_text("placeholder")
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
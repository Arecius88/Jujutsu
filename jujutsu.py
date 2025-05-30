from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from Modules import YellowBelt, OrangeBelt, GreenBelt, BlueBelt, BrownBelt, FirstDan, Progressbar, Messages_to_app
from random import choice

UKEWASA = "Uke wasa"
ATEMIWASA = "Atemi wasa"
KANSETSUWASA = "Kansetsu wasa"
NAGEWASA = "Nage wasa"
KIHON = "Kihon"

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

		elif spinner_value == "Home_screen_1":
			self.parent.current = "home_screen_1"

#* NEW SCREEN
class YellowScreen(Screen):
	#Sets ie ukewasa to the object och ukewasa from the "color of the belt" class in Modules.
	#This Changes with every grade.
	ukewasa = YellowBelt.ukewasa()
	atemiwasa = YellowBelt.atemiwasa()
	kansetsuwasa = YellowBelt.kansetsuwasa()
	kihon = YellowBelt.all_kihon()
	progressbar = Progressbar()


	def technique_selected_random(self, technique_group):
		"""
		This method takes in a list of techniques and returns a random technique from that list.

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

			if self.ids.my_progressbar.value > 0: #REset the progressbas when a new techniq family is chosen.
				self.ids.my_progressbar.value = Progressbar.minimum(self)

		elif spinner_value == ATEMIWASA:
			self.ids.technic_displayer_label.text = WELCOME_TEXT

			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = Progressbar.minimum(self)

		elif spinner_value == KANSETSUWASA:
			self.ids.technic_displayer_label.text = WELCOME_TEXT

			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = Progressbar.minimum(self)

		elif spinner_value == NAGEWASA:
		#added an if-statement if HomeScreen spinner is Yellow and if so display an error message.
			if self.manager.get_screen("home").ids.spinner_menu_home.text == "Yellow":
				self.ids.technic_displayer_label.text = f"This grade do not have {self.spinner_value}.\n " \
														f"Please choose an other technique group."
			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = Progressbar.minimum(self)
			else:
				self.ids.technic_displayer_label.text = WELCOME_TEXT
				if self.ids.my_progressbar.value > 0:
					self.ids.my_progressbar.value = Progressbar.minimum(self)

		elif spinner_value == KIHON:
			self.ids.technic_displayer_label.text = WELCOME_TEXT
			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = Progressbar.minimum(self)

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
				self.technique_selected_random(self.ukewasa)
				#Modules.Technique_selecter.random_technique(self.
				# ukewasa)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(YellowBelt.ukewasa())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty
				if len(self.ukewasa) + 1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)

					#resets the list
					self.ukewasa = YellowBelt.ukewasa()

			elif self.spinner_value == ATEMIWASA:
				#runs the technique selecter function
				self.technique_selected_random(self.atemiwasa)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(YellowBelt.atemiwasa())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty. +1 is to add one more step in to the
				#click of the button
				if len(self.atemiwasa) +1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)

					#resets the list
					self.atemiwasa = YellowBelt.atemiwasa()

			elif self.spinner_value == KANSETSUWASA:
				#runs the technique selecter function
				self.technique_selected_random(self.kansetsuwasa)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(YellowBelt.kansetsuwasa())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty. +1 is to add one more step in to the
				# click of the button
				if len(self.kansetsuwasa) +1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)
					#resets the list
					self.kansetsuwasa = YellowBelt.kansetsuwasa()

			elif self.spinner_value == NAGEWASA:
				#Passes this choise in this grade
				pass

			elif self.spinner_value == KIHON:
				#runs the technique selecter function
				self.technique_selected_random(self.kihon)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(YellowBelt.all_kihon())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty. +1 is to add one more step in to the
				# click of the button
				if len(self.kihon) + 1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)

					#resets the list
					self.kihon = YellowBelt.all_kihon()

		except:
			self.ids.technic_displayer_label.text = Messages_to_app.ERROR_MESSAGE(self)

	def reset_button(self):
		self.ids.my_progressbar.value = 0
		self.ukewasa = YellowBelt.ukewasa()
		self.atemiwasa = YellowBelt.atemiwasa()
		self.kihon = YellowBelt.all_kihon()
		self.kansetsuwasa = YellowBelt.kansetsuwasa()
		self.ids.technic_displayer_label.text = Messages_to_app.RESET_TECHNIQUE_TEXT(self)
		self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)

	def home_screen_button(self):
		reference_to_home_screen = self.manager.get_screen("home")
		reference_to_home_screen.ids.spinner_menu_home.text = HomeScreen.home_spinner_text(self)
		self.parent.current = "home"

#* NEW SCREEN
class OrangeScreen(Screen):
	#Sets ie ukewasa to the object och ukewasa from the "color of the belt" class in Modules.
	#This Changes with every grade.
	ukewasa = OrangeBelt.ukewasa()
	atemiwasa = OrangeBelt.atemiwasa()
	kansetsuwasa = OrangeBelt.kansetsuwasa()
	nagewasa = OrangeBelt.nagewasa()
	kihon = OrangeBelt.all_kihon()
	progressbar = Progressbar()


	def technique_selected_random(self, technique_group):
		"""
		This method takes in a list of techniques and returns a random technique from that list.

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

			if self.ids.my_progressbar.value > 0: #REset the progressbas when a new techniq family is chosen.
				self.ids.my_progressbar.value = Progressbar.minimum(self)

		elif spinner_value == ATEMIWASA:
			self.ids.technic_displayer_label.text = WELCOME_TEXT

			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = Progressbar.minimum(self)

		elif spinner_value == KANSETSUWASA:
			self.ids.technic_displayer_label.text = WELCOME_TEXT

			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = Progressbar.minimum(self)

		elif spinner_value == NAGEWASA:
		#added an if-statement if HomeScreen spinner is Yellow and if so display an error message.
			if self.manager.get_screen("home").ids.spinner_menu_home.text == "Yellow":
				self.ids.technic_displayer_label.text = f"This grade do not have {self.spinner_value}.\n " \
														f"Please choose an other technique group."
			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = Progressbar.minimum(self)
			else:
				self.ids.technic_displayer_label.text = WELCOME_TEXT
				if self.ids.my_progressbar.value > 0:
					self.ids.my_progressbar.value = Progressbar.minimum(self)

		elif spinner_value == KIHON:
			self.ids.technic_displayer_label.text = WELCOME_TEXT
			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = Progressbar.minimum(self)

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
				self.technique_selected_random(self.ukewasa)
				#Modules.Technique_selecter.random_technique(self.
				# ukewasa)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(OrangeBelt.ukewasa())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty
				if len(self.ukewasa) + 1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)

					#resets the list
					self.ukewasa = OrangeBelt.ukewasa()

			elif self.spinner_value == ATEMIWASA:
				#runs the technique selecter function
				self.technique_selected_random(self.atemiwasa)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(OrangeBelt.atemiwasa())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty. +1 is to add one more step in to the
				#click of the button
				if len(self.atemiwasa) +1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)

					#resets the list
					self.atemiwasa = OrangeBelt.atemiwasa()

			elif self.spinner_value == KANSETSUWASA:
				#runs the technique selecter function
				self.technique_selected_random(self.kansetsuwasa)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(OrangeBelt.kansetsuwasa())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty. +1 is to add one more step in to the
				# click of the button
				if len(self.kansetsuwasa) +1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)
					#resets the list
					self.kansetsuwasa = OrangeBelt.kansetsuwasa()

			elif self.spinner_value == NAGEWASA:
								#runs the technique selecter function
				self.technique_selected_random(self.nagewasa)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(OrangeBelt.nagewasa())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty. +1 is to add one more step in to the
				if len(self.nagewasa) +1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)
					#resets the list
					self.nagewasa = OrangeBelt.nagewasa()

			elif self.spinner_value == KIHON:
				#runs the technique selecter function
				self.technique_selected_random(self.kihon)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(OrangeBelt.all_kihon())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty. +1 is to add one more step in to the
				# click of the button
				if len(self.kihon) + 1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)

					#resets the list
					self.kihon = OrangeBelt.all_kihon()

		except:
			self.ids.technic_displayer_label.text = Messages_to_app.ERROR_MESSAGE(self)

	def reset_button(self):
		self.ids.my_progressbar.value = 0
		self.ukewasa = OrangeBelt.ukewasa()
		self.atemiwasa = OrangeBelt.atemiwasa()
		self.kihon = OrangeBelt.all_kihon()
		self.kansetsuwasa = OrangeBelt.kansetsuwasa()
		self.ids.technic_displayer_label.text = Messages_to_app.RESET_TECHNIQUE_TEXT(self)
		self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)

	def home_screen_button(self):
		reference_to_home_screen = self.manager.get_screen("home")
		reference_to_home_screen.ids.spinner_menu_home.text = HomeScreen.home_spinner_text(self)
		self.parent.current = "home"

#* NEW SCREEN
class GreenScreen(Screen):
    #Sets ie ukewasa to the object och ukewasa from the "color of the belt" class in Modules.
	#This Changes with every grade.
	ukewasa = GreenBelt.ukewasa()
	atemiwasa = GreenBelt.atemiwasa()
	kansetsuwasa = GreenBelt.kansetsuwasa()
	nagewasa = GreenBelt.nagewasa()
	kihon = GreenBelt.all_kihon()
	progressbar = Progressbar()


	def technique_selected_random(self, technique_group):
		"""
		This method takes in a list of techniques and returns a random technique from that list.

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

			if self.ids.my_progressbar.value > 0: #REset the progressbas when a new techniq family is chosen.
				self.ids.my_progressbar.value = Progressbar.minimum(self)

		elif spinner_value == ATEMIWASA:
			self.ids.technic_displayer_label.text = WELCOME_TEXT

			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = Progressbar.minimum(self)

		elif spinner_value == KANSETSUWASA:
			self.ids.technic_displayer_label.text = WELCOME_TEXT

			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = Progressbar.minimum(self)

		elif spinner_value == NAGEWASA:
		#added an if-statement if HomeScreen spinner is Yellow and if so display an error message.
			if self.manager.get_screen("home").ids.spinner_menu_home.text == "Yellow":
				self.ids.technic_displayer_label.text = f"This grade do not have {self.spinner_value}.\n " \
														f"Please choose an other technique group."
			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = Progressbar.minimum(self)
			else:
				self.ids.technic_displayer_label.text = WELCOME_TEXT
				if self.ids.my_progressbar.value > 0:
					self.ids.my_progressbar.value = Progressbar.minimum(self)

		elif spinner_value == KIHON:
			self.ids.technic_displayer_label.text = WELCOME_TEXT
			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = Progressbar.minimum(self)

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
				self.technique_selected_random(self.ukewasa)
				#Modules.Technique_selecter.random_technique(self.
				# ukewasa)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(GreenBelt.ukewasa())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty
				if len(self.ukewasa) + 1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)

					#resets the list
					self.ukewasa = OrangeBelt.ukewasa()

			elif self.spinner_value == ATEMIWASA:
				#runs the technique selecter function
				self.technique_selected_random(self.atemiwasa)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(GreenBelt.atemiwasa())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty. +1 is to add one more step in to the
				#click of the button
				if len(self.atemiwasa) +1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)

					#resets the list
					self.atemiwasa = GreenBelt.atemiwasa()

			elif self.spinner_value == KANSETSUWASA:
				#runs the technique selecter function
				self.technique_selected_random(self.kansetsuwasa)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(GreenBelt.kansetsuwasa())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty. +1 is to add one more step in to the
				# click of the button
				if len(self.kansetsuwasa) +1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)
					#resets the list
					self.kansetsuwasa = GreenBelt.kansetsuwasa()

			elif self.spinner_value == NAGEWASA:
								#runs the technique selecter function
				self.technique_selected_random(self.nagewasa)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(GreenBelt.nagewasa())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty. +1 is to add one more step in to the
				if len(self.nagewasa) +1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)
					#resets the list
					self.nagewasa = GreenBelt.nagewasa()

			elif self.spinner_value == KIHON:
				#runs the technique selecter function
				self.technique_selected_random(self.kihon)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(GreenBelt.all_kihon())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty. +1 is to add one more step in to the
				# click of the button
				if len(self.kihon) + 1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)

					#resets the list
					self.kihon = GreenBelt.all_kihon()

		except:
			self.ids.technic_displayer_label.text = Messages_to_app.ERROR_MESSAGE(self)

	def reset_button(self):
		self.ids.my_progressbar.value = 0
		self.ukewasa = GreenBelt.ukewasa()
		self.atemiwasa = GreenBelt.atemiwasa()
		self.kihon = GreenBelt.all_kihon()
		self.kansetsuwasa = GreenBelt.kansetsuwasa()
		self.ids.technic_displayer_label.text = Messages_to_app.RESET_TECHNIQUE_TEXT(self)
		self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)

	def home_screen_button(self):
		reference_to_home_screen = self.manager.get_screen("home")
		reference_to_home_screen.ids.spinner_menu_home.text = HomeScreen.home_spinner_text(self)
		self.parent.current = "home"

#* NEW SCREEN
class BlueScreen(Screen):
	#Sets ie ukewasa to the object och ukewasa from the "color of the belt" class in Modules.
	#This Changes with every grade.
	ukewasa = BlueBelt.ukewasa()
	atemiwasa = BlueBelt.atemiwasa()
	kansetsuwasa = BlueBelt.kansetsuwasa()
	nagewasa = BlueBelt.nagewasa()
	kihon = BlueBelt.all_kihon()
	progressbar = Progressbar()


	def technique_selected_random(self, technique_group):
		"""
		This method takes in a list of techniques and returns a random technique from that list.

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

			if self.ids.my_progressbar.value > 0: #REset the progressbas when a new techniq family is chosen.
				self.ids.my_progressbar.value = Progressbar.minimum(self)

		elif spinner_value == ATEMIWASA:
			self.ids.technic_displayer_label.text = WELCOME_TEXT

			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = Progressbar.minimum(self)

		elif spinner_value == KANSETSUWASA:
			self.ids.technic_displayer_label.text = WELCOME_TEXT

			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = Progressbar.minimum(self)

		elif spinner_value == NAGEWASA:
		#added an if-statement if HomeScreen spinner is Yellow and if so display an error message.
			if self.manager.get_screen("home").ids.spinner_menu_home.text == "Yellow":
				self.ids.technic_displayer_label.text = f"This grade do not have {self.spinner_value}.\n " \
														f"Please choose an other technique group."
			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = Progressbar.minimum(self)
			else:
				self.ids.technic_displayer_label.text = WELCOME_TEXT
				if self.ids.my_progressbar.value > 0:
					self.ids.my_progressbar.value = Progressbar.minimum(self)

		elif spinner_value == KIHON:
			self.ids.technic_displayer_label.text = WELCOME_TEXT
			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = Progressbar.minimum(self)

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
				self.technique_selected_random(self.ukewasa)
				#Modules.Technique_selecter.random_technique(self.
				# ukewasa)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(BlueBelt.ukewasa())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty
				if len(self.ukewasa) + 1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)

					#resets the list
					self.ukewasa = OrangeBelt.ukewasa()

			elif self.spinner_value == ATEMIWASA:
				#runs the technique selecter function
				self.technique_selected_random(self.atemiwasa)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(BlueBelt.atemiwasa())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty. +1 is to add one more step in to the
				#click of the button
				if len(self.atemiwasa) +1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)

					#resets the list
					self.atemiwasa = BlueBelt.atemiwasa()

			elif self.spinner_value == KANSETSUWASA:
				#runs the technique selecter function
				self.technique_selected_random(self.kansetsuwasa)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(BlueBelt.kansetsuwasa())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty. +1 is to add one more step in to the
				# click of the button
				if len(self.kansetsuwasa) +1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)
					#resets the list
					self.kansetsuwasa = BlueBelt.kansetsuwasa()

			elif self.spinner_value == NAGEWASA:
								#runs the technique selecter function
				self.technique_selected_random(self.nagewasa)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(BlueBelt.nagewasa())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty. +1 is to add one more step in to the
				if len(self.nagewasa) +1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)
					#resets the list
					self.nagewasa = GreenBelt.nagewasa()

			elif self.spinner_value == KIHON:
				#runs the technique selecter function
				self.technique_selected_random(self.kihon)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(BlueBelt.all_kihon())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty. +1 is to add one more step in to the
				# click of the button
				if len(self.kihon) + 1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)

					#resets the list
					self.kihon = BlueBelt.all_kihon()

		except:
			self.ids.technic_displayer_label.text = Messages_to_app.ERROR_MESSAGE(self)

	def reset_button(self):
		self.ids.my_progressbar.value = 0
		self.ukewasa = BlueBelt.ukewasa()
		self.atemiwasa = BlueBelt.atemiwasa()
		self.kihon = BlueBelt.all_kihon()
		self.kansetsuwasa = BlueBelt.kansetsuwasa()
		self.ids.technic_displayer_label.text = Messages_to_app.RESET_TECHNIQUE_TEXT(self)
		self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)

	def home_screen_button(self):
		reference_to_home_screen = self.manager.get_screen("home")
		reference_to_home_screen.ids.spinner_menu_home.text = HomeScreen.home_spinner_text(self)
		self.parent.current = "home"

#* NEW SCREEN
class BrownScreen(Screen):
	#Sets ie ukewasa to the object och ukewasa from the "color of the belt" class in Modules.
	#This Changes with every grade.
	ukewasa = BrownBelt.ukewasa()
	atemiwasa = BrownBelt.atemiwasa()
	kansetsuwasa = BrownBelt.kansetsuwasa()
	nagewasa = BrownBelt.nagewasa()
	kihon = BrownBelt.all_kihon()
	progressbar = Progressbar()


	def technique_selected_random(self, technique_group):
		"""
		This method takes in a list of techniques and returns a random technique from that list.

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

			if self.ids.my_progressbar.value > 0: #REset the progressbas when a new techniq family is chosen.
				self.ids.my_progressbar.value = Progressbar.minimum(self)

		elif spinner_value == ATEMIWASA:
			self.ids.technic_displayer_label.text = WELCOME_TEXT

			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = Progressbar.minimum(self)

		elif spinner_value == KANSETSUWASA:
			self.ids.technic_displayer_label.text = WELCOME_TEXT

			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = Progressbar.minimum(self)

		elif spinner_value == NAGEWASA:
		#added an if-statement if HomeScreen spinner is Yellow and if so display an error message.
			if self.manager.get_screen("home").ids.spinner_menu_home.text == "Yellow":
				self.ids.technic_displayer_label.text = f"This grade do not have {self.spinner_value}.\n " \
														f"Please choose an other technique group."
			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = Progressbar.minimum(self)
			else:
				self.ids.technic_displayer_label.text = WELCOME_TEXT
				if self.ids.my_progressbar.value > 0:
					self.ids.my_progressbar.value = Progressbar.minimum(self)

		elif spinner_value == KIHON:
			self.ids.technic_displayer_label.text = WELCOME_TEXT
			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = Progressbar.minimum(self)

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
				self.technique_selected_random(self.ukewasa)
				#Modules.Technique_selecter.random_technique(self.
				# ukewasa)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(BrownBelt.ukewasa())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty
				if len(self.ukewasa) + 1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)

					#resets the list
					self.ukewasa = BrownBelt.ukewasa()

			elif self.spinner_value == ATEMIWASA:
				#runs the technique selecter function
				self.technique_selected_random(self.atemiwasa)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(BrownBelt.atemiwasa())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty. +1 is to add one more step in to the
				#click of the button
				if len(self.atemiwasa) +1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)

					#resets the list
					self.atemiwasa = BrownBelt.atemiwasa()

			elif self.spinner_value == KANSETSUWASA:
				#runs the technique selecter function
				self.technique_selected_random(self.kansetsuwasa)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(BrownBelt.kansetsuwasa())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty. +1 is to add one more step in to the
				# click of the button
				if len(self.kansetsuwasa) +1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)
					#resets the list
					self.kansetsuwasa = BrownBelt.kansetsuwasa()

			elif self.spinner_value == NAGEWASA:
								#runs the technique selecter function
				self.technique_selected_random(self.nagewasa)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(BrownBelt.nagewasa())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty. +1 is to add one more step in to the
				if len(self.nagewasa) +1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)
					#resets the list
					self.nagewasa = BrownBelt.nagewasa()

			elif self.spinner_value == KIHON:
				#runs the technique selecter function
				self.technique_selected_random(self.kihon)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(BrownBelt.all_kihon())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty. +1 is to add one more step in to the
				# click of the button
				if len(self.kihon) + 1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)

					#resets the list
					self.kihon = BrownBelt.all_kihon()

		except:
			self.ids.technic_displayer_label.text = Messages_to_app.ERROR_MESSAGE(self)

	def reset_button(self):
		self.ids.my_progressbar.value = 0
		self.ukewasa = BrownBelt.ukewasa()
		self.atemiwasa = BrownBelt.atemiwasa()
		self.kihon = BrownBelt.all_kihon()
		self.kansetsuwasa = BrownBelt.kansetsuwasa()
		self.ids.technic_displayer_label.text = Messages_to_app.RESET_TECHNIQUE_TEXT(self)
		self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)

	def home_screen_button(self):
		reference_to_home_screen = self.manager.get_screen("home")
		reference_to_home_screen.ids.spinner_menu_home.text = HomeScreen.home_spinner_text(self)
		self.parent.current = "home"

#* NEW SCREEN
class FirstDanScreen(Screen):
	#Sets ie ukewasa to the object och ukewasa from the "color of the belt" class in Modules.
	#This Changes with every grade.
	ukewasa = FirstDan.ukewasa()
	atemiwasa = FirstDan.atemiwasa()
	kansetsuwasa = FirstDan.kansetsuwasa()
	nagewasa = FirstDan.nagewasa()
	kihon = FirstDan.all_kihon()
	progressbar = Progressbar()


	def technique_selected_random(self, technique_group):
		"""
		This method takes in a list of techniques and returns a random technique from that list.

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

			if self.ids.my_progressbar.value > 0: #REset the progressbas when a new techniq family is chosen.
				self.ids.my_progressbar.value = Progressbar.minimum(self)

		elif spinner_value == ATEMIWASA:
			self.ids.technic_displayer_label.text = WELCOME_TEXT

			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = Progressbar.minimum(self)

		elif spinner_value == KANSETSUWASA:
			self.ids.technic_displayer_label.text = WELCOME_TEXT

			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = Progressbar.minimum(self)

		elif spinner_value == NAGEWASA:
		#added an if-statement if HomeScreen spinner is Yellow and if so display an error message.
			if self.manager.get_screen("home").ids.spinner_menu_home.text == "Yellow":
				self.ids.technic_displayer_label.text = f"This grade do not have {self.spinner_value}.\n " \
														f"Please choose an other technique group."
			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = Progressbar.minimum(self)
			else:
				self.ids.technic_displayer_label.text = WELCOME_TEXT
				if self.ids.my_progressbar.value > 0:
					self.ids.my_progressbar.value = Progressbar.minimum(self)

		elif spinner_value == KIHON:
			self.ids.technic_displayer_label.text = WELCOME_TEXT
			if self.ids.my_progressbar.value > 0:
				self.ids.my_progressbar.value = Progressbar.minimum(self)

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
				self.technique_selected_random(self.ukewasa)
				#Modules.Technique_selecter.random_technique(self.
				# ukewasa)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(FirstDan.ukewasa())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty
				if len(self.ukewasa) + 1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)

					#resets the list
					self.ukewasa = FirstDan.ukewasa()

			elif self.spinner_value == ATEMIWASA:
				#runs the technique selecter function
				self.technique_selected_random(self.atemiwasa)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(FirstDan.atemiwasa())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty. +1 is to add one more step in to the
				#click of the button
				if len(self.atemiwasa) +1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)

					#resets the list
					self.atemiwasa = FirstDan.atemiwasa()

			elif self.spinner_value == KANSETSUWASA:
				#runs the technique selecter function
				self.technique_selected_random(self.kansetsuwasa)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(FirstDan.kansetsuwasa())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty. +1 is to add one more step in to the
				# click of the button
				if len(self.kansetsuwasa) +1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)
					#resets the list
					self.kansetsuwasa = FirstDan.kansetsuwasa()

			elif self.spinner_value == NAGEWASA:
								#runs the technique selecter function
				self.technique_selected_random(self.nagewasa)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(FirstDan.nagewasa())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty. +1 is to add one more step in to the
				if len(self.nagewasa) +1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)
					#resets the list
					self.nagewasa = FirstDan.nagewasa()

			elif self.spinner_value == KIHON:
				#runs the technique selecter function
				self.technique_selected_random(self.kihon)

				#Display a message in the label
				self.ids.technic_displayer_label.text = self.technique

				#Define the progressbar_max.
				self.ids.my_progressbar.max = self.progressbar.maximum(FirstDan.all_kihon())

				#Increment the progressbar with 1 to the maximum
				self.ids.my_progressbar.value += 1

				# Check if the list of technics are empty. +1 is to add one more step in to the
				# click of the button
				if len(self.kihon) + 1 == 0:
					#Display a message that the list is empty
					self.ids.technic_displayer_label.text = Messages_to_app.END_OF_TECHNIQUE_TEXT(self)

					#Resets the spinner
					self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)

					#resets the list
					self.kihon = FirstDan.all_kihon()

		except:
			self.ids.technic_displayer_label.text = Messages_to_app.ERROR_MESSAGE(self)

	def reset_button(self):
		self.ids.my_progressbar.value = 0
		self.ukewasa = FirstDan.ukewasa()
		self.atemiwasa = FirstDan.atemiwasa()
		self.kihon = FirstDan.all_kihon()
		self.kansetsuwasa = FirstDan.kansetsuwasa()
		self.ids.technic_displayer_label.text = Messages_to_app.RESET_TECHNIQUE_TEXT(self)
		self.ids.spinner_menu_grades.text = Messages_to_app.RESET_SPINNER_TEXT(self)

	def home_screen_button(self):
		reference_to_home_screen = self.manager.get_screen("home")
		reference_to_home_screen.ids.spinner_menu_home.text = HomeScreen.home_spinner_text(self)
		self.parent.current = "home"


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

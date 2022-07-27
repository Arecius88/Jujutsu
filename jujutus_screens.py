from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


#Sakpa en class som hanterar alla byten av skärmar

''' class spinner_handler():
		def on_spinner_select_grades
			Ändra från Home till en grad
			
		def on_spinner_select_technique
			val av teknik som föregående ver av appen. 
		'''


#Define our different screens
class HomeScreen(Screen):
	def on_spinner_select_grades(self, spinner_value):
		print("1. Spinner value " + spinner_value)
		if spinner_value == "Home":
			self.parent.current = "home"

		if spinner_value == "Yellow":
			self.parent.current = "yellow"

		elif spinner_value == "Orange":
			self.parent.current = "orange"

class YellowScreen(Screen):
	def on_spinner_select_technique(self, spinner_value):
		print("1. Spinner value " + spinner_value)
		if spinner_value == "Home":
			self.parent.current = "home"

		elif spinner_value == "Uke":
			self.ids.yellow_screen_label.text = "Kanske är vi på rätt väg?"

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
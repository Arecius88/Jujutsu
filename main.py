from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget

# Designate Our .kv design file
#kv = Builder.load_file('jujutsu_screen.kv')

class test_screen(Widget):
	pass

class jujutsu_screenApp(App):
	def build(self):
		return test_screen()



if __name__ == '__main__':
	jujutsu_screenApp().run()

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

# Designate Our .kv design file
#kv = Builder.load_file('jujutsu_screen.kv')

class test_scren(Widget):
	pass

class jujutsu_screenApp(App):
	def build(self):
		return test_scren()



if __name__ == '__main__':
	jujutsu_screenApp().run()

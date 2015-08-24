import kivy
from kivy.app import App
from kivy.uix.label import Button
class Shapes(Button):
	triangle = ObjectProperty(None)
	def __init__(self, **kwargs):
		super(Shapes, self).__init__(**kwargs)
		with self.canvas:
			self.triangle = Triange(points=[0,0,100,100,200,0])

class MyApp(App):
	def build(self):
		return Shapes()

if __name__=='__main__':
	MyApp().run()

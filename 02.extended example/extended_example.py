import gi 
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Mywindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title='Hello Word')

		self.button = Gtk.Button(label='Click Here')
		#self.button.connect("clicked", self.on_button_clicked())
		self.button.connect("clicked", self.on_button_clicked)
		self.add(self.button)

	def on_button_clicked(self, widget):
		print('hello')


win = Mywindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()
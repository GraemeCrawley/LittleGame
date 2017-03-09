import threading

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty

from bot import UIBot


#Widget for bot game version
class PlusOrMinusGame(Widget):
	"""
	Widget to run the graphical version of the bot game.
	@type ui_bot: None
	@param ui_bot: setting the ui_bot to be none
	"""
	ui_bot = ObjectProperty(None)

    #Starts the game thread
	def start(self):
        threading.Thread(
            target=self.ui_bot.start_bot).start()

#Builds the game
class PlusOrMinusApp(App):
	"""
	Calls the widget
	@type game: PlusOrMinusGame
	@param game: gets the PlusOrMinusGame to start
	@rtype: PlusOrMinusGame
	@return: returns the PlusOrMinusGame instance
	"""
	def build(self):
        game = PlusOrMinusGame()
        return game


if __name__ == '__main__':
    PlusOrMinusApp().run()


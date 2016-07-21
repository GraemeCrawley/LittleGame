import threading

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty

from bot import UIBot


class PlusOrMinusGame(Widget):
    ui_bot = ObjectProperty(None)

    def start(self):
        threading.Thread(
            target=self.ui_bot.start_bot).start()


class PlusOrMinusApp(App):
    def build(self):
        game = PlusOrMinusGame()
        return game


if __name__ == '__main__':
    PlusOrMinusApp().run()


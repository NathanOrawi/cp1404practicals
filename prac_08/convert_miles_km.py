"""
CP1404/CP5632 Practical
Kivy GUI program to converting miles to kilometer
Nathan Orawi
Started 12/11/2023
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_KM_FACTOR = 1.60934


class ConvertMilesKmApp(App):
    """ ConvertMilesKmApp is a Kivy App for converting miles to kilometer """
    miles = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometer"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.miles = "Enter Miles to get Km"
        return self.root

    def handle_convert(self):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = float(self.root.ids.input_number.text) * MILES_KM_FACTOR
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = str(0.0)

    def handle_increment(self, increment):
        """.Pressing the Up or Down buttons increments the number of miles by 1 or -1 mile, respectfully"""
        try:
            result = (float(self.root.ids.input_number.text) + increment) * MILES_KM_FACTOR
            self.root.ids.output_label.text = str(result)
        except ValueError:
            result = increment
            self.root.ids.output_label.text = str(result)


ConvertMilesKmApp().run()

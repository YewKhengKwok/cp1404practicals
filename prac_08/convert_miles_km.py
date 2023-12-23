"""
Convert miles to km py
A Python program (.py) and Kivy kv language file (.kv) for an app that converts miles to kilometres.
"""

from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class ConvertMilesKm(App):
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = 'Convert Miles to Kilometres'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """Calculate miles from km after error check method"""
        # Error check, set to 0.0 if invalid
        miles = self.convert_to_number(text)
        # Calculate KM from Miles
        self.root.ids.output_label.text = str(miles * MILES_TO_KM)

    def handle_increment(self, text, change):
        """Increase or decrease value method"""
        miles = self.convert_to_number(text) + change
        self.root.ids.input_number.text = str(miles)

    @staticmethod
    def convert_to_number(text):
        """Error check
        Convert text to float or 0.0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0


ConvertMilesKm().run()

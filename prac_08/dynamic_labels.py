"""
Dynamic Labels py
A very simple app that has a list of names (strings) and
dynamically creates a separate Label for each one.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label

LABEL_COLOUR = (0.5, 0.5, 1, 1)  # RGBA for Purple


class DynamicLabels(App):
    """ Main program - Kivy app to demo label widget creation."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # List of names
        self.names = ['Bob', 'Dexter', 'Adrian', 'David', 'Elijah', 'Franklin']

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from data and add them to the GUI."""
        for name in self.names:
            # create a Label for each data entry, specifying the text
            temp_label = Label(text=name)
            # set label colour
            temp_label.color = LABEL_COLOUR
            # set text size
            temp_label.font_size = 96
            # add the Label to the "main" layout widget
            self.root.ids.main.add_widget(temp_label)


DynamicLabels().run()

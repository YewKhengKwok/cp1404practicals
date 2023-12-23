from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """When greet button pressed
        greet user input text"""
        print("test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """When clear button pressed
        clear input text and output label"""
        print("clear")
        self.root.ids.output_label.text = f""
        self.root.ids.input_name.text = f""


BoxLayoutDemo().run()

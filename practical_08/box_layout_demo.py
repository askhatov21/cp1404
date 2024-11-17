from kivy.app import App
from kivy.lang import Builder

class BoxLayoutDemo(App):
    """A simple Kivy application demonstrating BoxLayout interactions"""
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle the greet button press."""
        print("test")
        self.root.ids.output_label.text = "Hello" + self.root.ids.input_name.text

    def handle_pressed(self):
        """Handle the clear button press."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = "Enter your name"

if __name__ == '__main__':
BoxLayoutDemo().run()
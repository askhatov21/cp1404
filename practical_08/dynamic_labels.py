from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """
        A Kivy application that dynamically creates and displays labels
        based on a predefined list of names.
        """

    def __init__(self, **kwargs):
        """
               Initialize the DynamicLabelsApp with a list of names.

               :param kwargs: Additional keyword arguments for the App class"""
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        self.title = "Dynamic labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """
                Dynamically create Label widgets for each name in the names list
                and add them to the main BoxLayout in the KV file.
                """
        for name in self.names:
            temp_label = Label(text=name)
            # Replace NEW_COLOUR with an actual color, e.g., (1, 0, 0, 1) for red
            temp_label.color = (1, 0, 0, 1)
            self.root.ids.main_box.add_widget(temp_label)

DynamicLabelsApp().run()

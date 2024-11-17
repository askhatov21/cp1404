from kivy.app import App
from kivy.lang import Builder


CONVERT_MILES_TO_KM= 1.60934

class MilesConverterApp(App):
    """A Kivy app to convert miles to kilometers."""
    def build(self):
        """Build the Kivy app and load the KV file."""
        self.title= "Convert miles to kilometer"
        self.root= Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Calculate and display kilometers from the given miles."""
        value= self.get_validated_miles()
        result= value * CONVERT_MILES_TO_KM
        self.root.ids.output_label.text = str(result) + ' km'

    def handle_increment(self, change):
        """Increment or decrement miles and update the calculation."""
        value= self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        """Validate and return the input miles as a float or 0 if invalid."""
        try:
            value=float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()
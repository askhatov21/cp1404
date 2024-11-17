from kivy.app import App
from kivy.lang import Builder
kv_code = '''
BoxLayout:
    orientation: 'horizontal'

    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Genesis'
        Label:
            text: 'Exodus'

    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Leviticus'
'''
class MyKvApp(App):
    def build(self):
        return Builder.load_string(kv_code)

# Run the app
if __name__ == '__main__':
    MyKvApp().run()


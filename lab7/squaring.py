from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class SquareNumberApp(App):

    def build(self):
        Window.size = (400, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self):
        value = self.get_validated_value()
        result = value ** 2
        self.root.ids.output_label.text = str(result)

    def get_validated_value(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


SquareNumberApp().run()

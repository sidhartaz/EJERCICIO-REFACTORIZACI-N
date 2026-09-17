from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class Calculadora(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Variable para controlar si acabamos de calcular algo
        self.new_input = True

    def on_button_press(self, instance):
        current = self.ids.display.text
        button_text = instance.text

        if button_text == "=":
            try:
                # Calculamos resultado
                self.ids.display.text = str(eval(current))
            except Exception:
                self.ids.display.text = "Error"
            self.new_input = True
        else:
            if self.new_input or current == "0" or current == "Error":
                self.ids.display.text = button_text
                self.new_input = False
            else:
                self.ids.display.text += button_text

    def on_clear(self):
        self.ids.display.text = "0"
        self.new_input = True

class CalculadoraApp(MDApp):
    def build(self):
        Window.size = (350, 450)  # Tamaño de ventana (configuración de app)
        return Calculadora()

if __name__ == '__main__':
    CalculadoraApp().run()

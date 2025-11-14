from kivy.app import App
from kivy.lang import Builder

class BoxLayoutDemo(App):
    """Main app for greeting GUI demo."""

    def build(self):
        """Build the Kivy GUI from the kv file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle the 'Greet' button press."""
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"

    def handle_clear(self):
        """Handle the 'Clear' button press."""
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''
BoxLayoutDemo().run()






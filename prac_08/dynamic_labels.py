from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder

class DynamicLabelsApp(App):
    def build(self):
        self.root = Builder.load_file('dynamic_labels.kv')
        names = ["Alice", "Bob", "Charlie", "David", "Eve","Lily","Charly","Michael"]

        for name in names:
            label = Label(
                text=name,
                size_hint_y=None,
                height=40,
                color=(1, 0, 1, 1)
            )

            self.root.ids.label_container.add_widget(label)
        return self.root

DynamicLabelsApp().run()
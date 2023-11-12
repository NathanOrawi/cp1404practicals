"""
Kivy exercise
Dynamically create Labels based on content of dictionary
Nathan Orawi, first version: 12/11/2023
"""


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_to_label = {"Bob Brown": "Label 1", "Cat Cyan": "Label 2", "Oren Ochre": "Label 3"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from data and add them to the GUI."""
        for name in self.name_to_label:
            # create a button for each data entry, specifying the text
            temp_button = Button(text=name)
            temp_button.bind(on_press=self.press_entry)
            temp_button.name = name
            self.root.ids.entries_box.add_widget(temp_button)

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.name_to_label:
            # create a label for each data entry, specifying the text
            temp_label = Label(text=self.name_to_label[name])
            temp_label.bind(on_press=self.press_entry)
            temp_label.value = name
            self.root.ids.entries_box.add_widget(temp_label)

    def press_entry(self, instance):
        """Handle pressing entry buttons."""
        # get label (dictionary key) from the text of Button we clicked on
        name = instance.name
        label = self.name_to_label[name]
        self.status_text = label


DynamicLabelsApp().run()

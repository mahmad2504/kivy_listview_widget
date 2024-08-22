from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty

from kivy.lang import Builder
from listbox import ListBox
from kivy.core.window import Window


Window.size = (400, 600)

Builder.load_file('main.kv')

class DataItem:
    def __init__(self, text):
        self.text = text
        self.checked = False
       
class MainScreen(RelativeLayout):
    list_box = ObjectProperty(None)
    def __init__(self, **kw):
        super().__init__(**kw)
        text = 'Item '
        data = [DataItem(text + str(i)) for i in range(300)]
        self.list_box.load_items(data)
        self.list_box.bind(on_selection_changed=self.on_selection_changed)
        
    def on_save(self):
        print("Selected items are")
        for item in self.list_box.selected_items:
            print(item.data.text)

    
    def on_selection_changed(self, listbox, item):
        pass
       
        
    
class MainApp(App):
    
    def build(self):
        return MainScreen()


if __name__ == "__main__":
    MainApp().run()
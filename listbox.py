from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty
from kivy.uix.button import ButtonBehavior
from kivy.lang.builder import Builder
from kivy.factory import Factory
from kivy.clock import Clock

Builder.load_file('listbox.kv')

class ListBox(BoxLayout):
    multi_selection = BooleanProperty(True)
    def __init__(self, **kw):
        super().__init__(**kw)
        self.register_event_type('on_selection_changed')
        self.items = []
        self.selected_index = None
        self.selected_index_ls = []
        self.previous_index = None
    
    @property
    def selected_items(self):
        if self.multi_selection:
            return [self.items[index] for index in self.selected_index_ls]
        else:
            return [self.items[self.selected_index]]
    
    @property
    def previous_item(self):
        return self.items[self.previous_index]

    def select(self, value):

        tp = type(value)
        
        if tp is int:
            item = self.items[value]
        elif value in self.items:
            item = value
        else:
            raise ValueError('{} don\'t contain {}'.format(type(self), value))
        
        item.dispatch(event_type='on_press')
    
    def load_items(self,data):
        self.items = []
        for i, data_item in enumerate(data):
            widget = ListItem(container=self, data=data_item)
            widget.index = i
            widget.selected=data_item.checked
            self.add_widget(widget)
            self.items.append(widget)
            

    def on_selection_changed(self, item):
        pass
        
class ListItem(ButtonBehavior, RelativeLayout):
    selected = BooleanProperty(False)
    def __init__(self, container=None, data=None):
        self.container = container
        self.data = data
        super().__init__()
   
    def checkbox_click(self,checkbox,value):
        self.data.checked=value
        if self.data.checked:
            self.selected = True
            self.container.selected_index_ls.append(self.index)
        else:
            self.selected = False
            self.container.selected_index_ls.remove(self.index)
        self.container.dispatch('on_selection_changed', self)

        
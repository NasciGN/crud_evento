import kivy
from kivy.app import App
from kivymd.app import MDApp
from gerencTelas import GerenciaTelas

__version__ = "0.2"
class eventoADS(App):
    def build(self):
        self.root = GerenciaTelas()
        return self.root
    
if __name__ == '__main__':
    eventoADS().run()

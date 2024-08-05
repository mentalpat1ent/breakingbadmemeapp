import os
import kivy 
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.config import Config
from kivy.core.window import Window

Config.set('graphics', 'resizable', True)

class MethCooker(App):
    def build(self):
        self.layout = GridLayout(cols = 1, padding = 10,rows=2)
        self.image = Image(source = 'bb.jpg')
        self.button = Button(text = 'learn cooking meth',
                             font_size = '25sp',
                             size=(200,150),
                             size_hint=(.1,.1),
                             background_color = [0.4,0.4,0.5]
                             )
        self.layout.add_widget(self.button)
        self.layout.add_widget(self.image)
        self.button.bind(on_press=self.onbuttonPress)
        return self.layout


    def onbuttonPress(self, button):
        layout = GridLayout(cols = 1, padding = 5)
        
        popuplabel = Label(text = "Ingredients:\n-Acetone, from paint thinner or nail polish remover.\n-Anhydrous ammonia, found in various household cleaners.\n-Sulfuric acid or hydrochloric acid, which is typically extracted from over-the-counter drain cleaners.\n-Toluene from brake fluid.\n-Phosphorous, extracted from flares, matches, and other substances.\n-Ether or chloroform.\n-Freon from air-conditioning units.\n-Energy drink instead of using over-the-counter medications.\n-Benzene and gasoline.\n-Alcohol.\n-Lithium, which is removed from car batteries.\n\n4 Steps to make Meth:\n1.Ephedrine or pseudoephedrine is combined with ammonia and lithium or iodine and phosphorus.\n2.Mixed in with water.\n3.A solvent like gasoline is added, and the person extracts the methamphetamine.\n4.The mixture is heated by using the acid or some other substance (e.g., gasoline) to crystallize the product.",
                           font_size='20sp')
        closebutton = Button(text = 'continue',
                             size_hint=(.1,.1),
                             font_size='20sp',
                             background_color=[0.4,0.4,0.5])
        layout.add_widget(popuplabel)
        layout.add_widget(closebutton)
        popup = Popup(title = 'Meth Recipe' ,
                    content=layout,
                    background_color=[0,0,0],
                    separator_color=[0.9,1,0.1])
        popup.open()
        closebutton.bind(on_press = self.btnpr)
    
    
    def btnpr(self, button):
        lyout = GridLayout(cols = 1, padding = 5)
        shaco = Image(source = 'thatsallbitc.jpg')
        clsbtn = Button(text = 'start cooking!',
                            font_size = '20sp',
                            size_hint=(.1,.1),
                            background_color=[0.4,0.4,0.5])
        lyout.add_widget(shaco)
        lyout.add_widget(clsbtn)
        pop = Popup(title = ' ',
                        content = lyout,
                        background_color=[0,0,0],
                        separator_color=[0,0,0])
        pop.open()
        clsbtn.bind(on_press = self.stop)


if __name__=='__main__':
    MethCooker().run()
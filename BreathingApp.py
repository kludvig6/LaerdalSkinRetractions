from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

from playsound import playsound
import global_hw_var

Builder.load_file("breathing.kv")
class MyLayout(Widget):

    ## App button callbacks
    def subcostal_routine(self):
        if global_hw_var.subcostal_on == 1:
            self.subcostal_btn.background_color = (0.18, 0.498, 0.631, 1)
            self.subcostal_btn.color = (1, 1 , 1, 1)
            self.subcostal_label.picture_source = 'retractions_pictures\GrayOff.png'
            global_hw_var.subcostal_on = 0
        else:
            self.subcostal_btn.background_color = (1, 1 , 1, 1)
            self.subcostal_btn.color = (0.18, 0.498, 0.631, 1)
            self.subcostal_label.picture_source = 'retractions_pictures\Subcostal.png'
            global_hw_var.subcostal_on = 1

    def substernal_routine(self):
        if global_hw_var.substernal_on == 1:
            self.substernal_btn.background_color = (0.18, 0.498, 0.631, 1)
            self.substernal_btn.color = (1, 1 , 1, 1)
            self.substernal_label.picture_source = 'retractions_pictures\GrayOff.png'
            global_hw_var.substernal_on = 0
        else:
            self.substernal_btn.background_color = (1, 1 , 1, 1)
            self.substernal_btn.color = (0.18, 0.498, 0.631, 1)
            self.substernal_label.picture_source = 'retractions_pictures\Substernal.png'
            global_hw_var.substernal_on = 1

    def intercostal_routine(self):
        if global_hw_var.intercostal_on == 1:
            self.intercostal_btn.background_color = (0.18, 0.498, 0.631, 1)
            self.intercostal_btn.color = (1, 1 , 1, 1)
            self.intercostal_label.picture_source = 'retractions_pictures\GrayOff.png'
            global_hw_var.intercostal_on = 0
        else:
            self.intercostal_btn.background_color = (1, 1 , 1, 1)
            self.intercostal_btn.color = (0.18, 0.498, 0.631, 1)
            self.intercostal_label.picture_source = 'retractions_pictures\Intercostal.png'
            global_hw_var.intercostal_on = 1
            
    def clavicular_routine(self):
        if global_hw_var.clavicular_on == 1:
            self.clavicular_btn.background_color = (0.18, 0.498, 0.631, 1)
            self.clavicular_btn.color = (1, 1 , 1, 1)
            self.clavicular_label.picture_source = 'retractions_pictures\GrayOff.png'
            global_hw_var.clavicular_on = 0
        else:
            self.clavicular_btn.background_color = (1, 1 , 1, 1)
            self.clavicular_btn.color = (0.18, 0.498, 0.631, 1)
            self.clavicular_label.picture_source = 'retractions_pictures\Clavicular.png'
            global_hw_var.clavicular_on = 1

    def suprasternal_routine(self):
        if global_hw_var.suprasternal_on == 1:
            self.suprasternal_btn.background_color = (0.18, 0.498, 0.631, 1)
            self.suprasternal_btn.color = (1, 1 , 1, 1)
            self.suprasternal_label.picture_source = 'retractions_pictures\GrayOff.png'
            global_hw_var.suprasternal_on = 0
        else:
            self.suprasternal_btn.background_color = (1, 1 , 1, 1)
            self.suprasternal_btn.color = (0.18, 0.498, 0.631, 1)
            self.suprasternal_label.picture_source = 'retractions_pictures\Suprasternal.png'
            global_hw_var.suprasternal_on = 1

class BreathingApp(App):
    def build(self):
        return MyLayout()
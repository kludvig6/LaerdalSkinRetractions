from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

import threading
import serial
from playsound import playsound
from pyfirmata import Arduino, util

from Control import Control
from HardwareControl import HardwareControl

Builder.load_file("breathing.kv")
class MyLayout(Widget):
    def __init__(self):
        super().__init__()
        self.ctrl = Control(rapid_breath=True)
        ## Retractions control
        self.rapid_breath = True
        self.subcostal_on = 0
        self.substernal_on = 0
        self.intercostal_on = 0
        self.clavicular_on = 0
        self.suprasternal_on = 0

    ## Retractions control
    def set_subcostal(self, value):
        self.subcostal_on = value
    def set_substernal(self, value):
        self.substernal_on = value
    def set_intercostal(self, value):
        self.intercostal_on = value
    def set_clavicular(self, value):
        self.clavicular_on = value
    def set_suprasternal(self, value):
        self.suprasternal_on = value

    def get_subcostal(self):
        return self.subcostal_on
    def get_substernal(self):
        return self.substernal_on
    def get_intercostal(self):
        return self.intercostal_on
    def get_clavicular(self):
        return self.clavicular_on
    def get_suprasternal(self):
        return self.suprasternal_on

    ## App button callbacks
    def subcostal_routine(self):
        if self.ctrl.get_subcostal() == 1:
            self.subcostal_btn.background_color = (1, 1 , 1, 1)
            self.subcostal_btn.color = (0.18, 0.498, 0.631, 1)
            self.subcostal_label.picture_source = 'retractions_pictures\Subcostal.png'
            self.ctrl.set_subcostal(0)
            #self.subcostal = "Off"
        else:
            self.subcostal_btn.background_color = (0.18, 0.498, 0.631, 1)
            self.subcostal_btn.color = (1, 1 , 1, 1)
            self.subcostal_label.picture_source = 'retractions_pictures\GrayOff.png'
            self.ctrl.set_subcostal(1)
            #self.subcostal = "On"

    def substernal_routine(self):
        if self.ctrl.get_substernal() == 1:
            self.substernal_btn.background_color = (1, 1 , 1, 1)
            self.substernal_btn.color = (0.18, 0.498, 0.631, 1)
            self.substernal_label.picture_source = 'retractions_pictures\Substernal.png'
            self.ctrl.set_substernal(0)
            #self.substernal = "Off"
        else:
            self.substernal_btn.background_color = (0.18, 0.498, 0.631, 1)
            self.substernal_btn.color = (1, 1 , 1, 1)
            self.substernal_label.picture_source = 'retractions_pictures\GrayOff.png'
            self.ctrl.set_substernal(1)
            #self.substernal = "On"

    def intercostal_routine(self):
        if self.ctrl.get_intercostal() == 1:
            self.intercostal_btn.background_color = (1, 1 , 1, 1)
            self.intercostal_btn.color = (0.18, 0.498, 0.631, 1)
            self.intercostal_label.picture_source = 'retractions_pictures\Intercostal.png'
            self.ctrl.set_intercostal(0)
            #self.intercostal = "Off"
        else:
            self.intercostal_btn.background_color = (0.18, 0.498, 0.631, 1)
            self.intercostal_btn.color = (1, 1 , 1, 1)
            self.intercostal_label.picture_source = 'retractions_pictures\GrayOff.png'
            self.ctrl.set_intercostal(1)
            #self.intercostal = "On"
            
    def clavicular_routine(self):
        if self.ctrl.get_clavicular() == 1:
            self.clavicular_btn.background_color = (1, 1 , 1, 1)
            self.clavicular_btn.color = (0.18, 0.498, 0.631, 1)
            self.clavicular_label.picture_source = 'retractions_pictures\Clavicular.png'
            self.ctrl.set_clavicular(0)
            #self.clavicular = "Off"
        else:
            self.clavicular_btn.background_color = (0.18, 0.498, 0.631, 1)
            self.clavicular_btn.color = (1, 1 , 1, 1)
            self.clavicular_label.picture_source = 'retractions_pictures\GrayOff.png'
            self.ctrl.set_clavicular(1)
            #self.clavicular = "On"

    def suprasternal_routine(self):
        if self.ctrl.get_suprasternal() == 1:
            self.suprasternal_btn.background_color = (1, 1 , 1, 1)
            self.suprasternal_btn.color = (0.18, 0.498, 0.631, 1)
            self.suprasternal_label.picture_source = 'retractions_pictures\Suprasternal.png'
            self.ctrl.set_suprasternal(0)
            #self.suprasternal = "Off"
        else:
            self.suprasternal_btn.background_color = (0.18, 0.498, 0.631, 1)
            self.suprasternal_btn.color = (1, 1 , 1, 1)
            self.suprasternal_label.picture_source = 'retractions_pictures\GrayOff.png'
            self.ctrl.set_suprasternal(1)
            #self.suprasternal = "On"

class BreathingApp(App):
    def build(self):
        return MyLayout()
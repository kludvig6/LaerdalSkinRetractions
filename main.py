from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

import time
import serial
import threading
from playsound import playsound
from pyfirmata import Arduino, util

from BreathingApp import BreathingApp
from HardwareControl import HardwareControl
from Control import Control

def open_app():
    BreathingApp().run()

def open_hw():
    hw_ctrl = HardwareControl(rapid_breath=True)
    hw_thread = threading.Thread(target=hw_ctrl.breathing,args=(True,))

if __name__ == '__main__':

    #app = BreathingApp()
    hw_ctrl = HardwareControl(rapid_breath=True)

    #app_thread = threading.Thread(target=app.run,args=(None,))
    hw_thread = threading.Thread(target=hw_ctrl.breathing,args=(True,))

    #app_thread.start()
    hw_thread.start()


    BreathingApp().run()


#if __name__ == '__main__':
#    a = multiprocessing.Process(target=open_parent)
#    b = multiprocessing.Process(target=open_child)
#    a.start()
#    b.start()
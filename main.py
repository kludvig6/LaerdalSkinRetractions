import threading

from BreathingApp import BreathingApp
from HardwareControl import HardwareControl

def open_app():
    BreathingApp().run()

if __name__ == '__main__':
    hw_ctrl = HardwareControl()
    hw_thread = threading.Thread(target=hw_ctrl.breathing)
    hw_thread.start()

    app_thread = threading.Thread(target=open_app)
    app_thread.start()
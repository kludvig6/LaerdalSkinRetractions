import threading

from BreathingApp import BreathingApp
from HardwareControl import HardwareControl

def open_app():
    BreathingApp().run()

def open_hw():
    hw_ctrl = HardwareControl(rapid_breath=True)
    hw_thread = threading.Thread(target=hw_ctrl.breathing,args=(True,))

if __name__ == '__main__':
    hw_ctrl = HardwareControl(rapid_breath=True)
    hw_thread = threading.Thread(target=hw_ctrl.breathing)
    hw_thread.start()

    BreathingApp().run()


#if __name__ == '__main__':
#    a = multiprocessing.Process(target=open_parent)
#    b = multiprocessing.Process(target=open_child)
#    a.start()
#    b.start()
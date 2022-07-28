import threading
import time
import serial
from playsound import playsound
from pyfirmata import Arduino, util

import global_hw_var

dir_path = "C:/Users/NOAKO2/Documents/appTesting/LaerdalSkinRetractions/"
class HardwareControl():
    def __init__(self):
        self.ventus_port = serial.Serial(port="COM9",
                            baudrate=115200,
                            bytesize=8,
                            timeout=2,
                            stopbits=serial.STOPBITS_ONE)
        self.ventus_port.write(b"#W2,0\n")
        self.ventus_port.write(b"#W0,0\n")
        self.ventus_port.write(b"#W10,0\n")
        self.ventus_port.write(b"#W11,0\n")

        if global_hw_var.rapid_breath:
            self.ventus_port.write(b"#W23,1000\n")
        else:
            self.ventus_port.write(b"#W23,100\n")

        self.board = Arduino("COM8")

        self.iterator = util.Iterator(self.board)
        self.iterator.start()

        self.subcostal_pin = self.board.get_pin("d:8:o")
        self.substernal_pin = self.board.get_pin("d:7:o")
        self.intercostal_pin = self.board.get_pin("d:6:o")
        self.clavicular_pin = self.board.get_pin("d:5:o")
        self.suprasternal_pin = self.board.get_pin("d:4:o")
        self.breast_pin = self.board.get_pin("d:10:o")

    def write_select_retractions(self, value):
        if global_hw_var.subcostal_on:
            self.subcostal_pin.write(value)
        else:
            self.subcostal_pin.write(0)
        if global_hw_var.substernal_on:
            self.substernal_pin.write(value)
        else:
            self.substernal_pin.write(0)
        if global_hw_var.intercostal_on:
            self.intercostal_pin.write(value)
        else:
            self.intercostal_pin.write(0)
        if global_hw_var.clavicular_on:
            self.clavicular_pin.write(value)
        else:
            self.clavicular_pin.write(0)
        if global_hw_var.suprasternal_on:
            self.suprasternal_pin.write(value)
        else:
            self.suprasternal_pin.write(0)

    
    def write_valves(self, value):
        self.write_select_retractions(value)
        self.breast_pin.write(value)

    def write_pump(self, value):
        if value == 1:
            self.ventus_port.write(b"#W0,1\n")
        else:
            self.ventus_port.write(b"#W0,0\n")

    def play_sound(self, filepath):
        playsound(filepath)

    def breathing(self):
        while True:
            if global_hw_var.rapid_breath:
                breath_path = dir_path + "breathing_sounds/08INNpust.mp3"

                valves_inhale = threading.Thread(target=self.write_valves,args=(1,))
                pump_inhale = threading.Thread(target=self.write_pump,args=(1,))
                sound_inhale = threading.Thread(target=self.play_sound,args=(breath_path,))

                valves_inhale.start()
                pump_inhale.start()
                sound_inhale.start()

                time.sleep(1.1)

                valves_inhale.join()
                pump_inhale.join()
                sound_inhale.join()

                breath_path = dir_path + "breathing_sounds/08UTpust.mp3"

                valves_exhale = threading.Thread(target=self.write_valves,args=(0,))
                pump_exhale = threading.Thread(target=self.write_pump,args=(0,))
                sound_exhale = threading.Thread(target=self.play_sound,args=(breath_path,))

                valves_exhale.start()
                pump_exhale.start()
                sound_exhale.start()

                time.sleep(0.9)

                valves_exhale.join()
                pump_exhale.join()
                sound_exhale.join()

            else:
                breath_path = dir_path + "breathing_sounds/12INNpust.mp3"

                valves_inhale = threading.Thread(target=self.write_valves,args=(1,))
                pump_inhale = threading.Thread(target=self.write_pump,args=(1,))
                sound_inhale = threading.Thread(target=self.play_sound,args=(breath_path,))

                valves_inhale.start()
                pump_inhale.start()
                sound_inhale.start()

                time.sleep(1.5)

                valves_inhale.join()
                pump_inhale.join()
                sound_inhale.join()

                breath_path = dir_path + "breathing_sounds/12Utpust.mp3"

                valves_exhale = threading.Thread(target=self.write_valves,args=(0,))
                pump_exhale = threading.Thread(target=self.write_pump,args=(0,))
                sound_exhale = threading.Thread(target=self.play_sound,args=(breath_path,))

                valves_exhale.start()
                pump_exhale.start()
                sound_exhale.start()

                time.sleep(1.3)

                valves_exhale.join()
                pump_exhale.join()
                sound_exhale.join()
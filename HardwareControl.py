import imp
import threading
import time
import serial
from playsound import playsound
from pyfirmata import Arduino, util

from Control import Control

class HardwareControl():
    def __init__(self, rapid_breath):
        self.rapid_breath = rapid_breath

        self.subcostal_on = 0
        self.substernal_on = 0
        self.intercostal_on = 0
        self.clavicular_on = 0
        self.suprasternal_on = 0

        self.ventus_port = serial.Serial(port="COM8",
                            baudrate=115200,
                            bytesize=8,
                            timeout=2,
                            stopbits=serial.STOPBITS_ONE)
        self.ventus_port.write(b"#W2,0\n")
        self.ventus_port.write(b"#W0,0\n")
        self.ventus_port.write(b"#W10,0\n")
        self.ventus_port.write(b"#W11,0\n")

        if self.rapid_breath:
            self.ventus_port.write(b"#W23,1000\n")
        else:
            self.ventus_port.write(b"#W23,100\n")

        self.board = Arduino("COM9")

        self.iterator = util.Iterator(self.board)
        self.iterator.start()

        self.subcostal_pin = self.board.get_pin("d:8:o")
        self.substernal_pin = self.board.get_pin("d:7:o")
        self.intercostal_pin = self.board.get_pin("d:6:o")
        self.clavicular_pin = self.board.get_pin("d:5:o")
        self.suprasternal_pin = self.board.get_pin("d:4:o")

    def digitalWrite(self, pin, value):
        if pin == 8:
            self.subcostal_pin.write(value)
        elif pin == 7:
            self.substernal_pin.write(value)
        elif pin == 6:
            self.intercostal_pin.write(value)
        elif pin == 5:
            self.clavicular_pin.write(value)
        elif pin == 4:
            self.suprasternal_pin.write(value)

    def write_pump(self, value):
        if value == 1:
            self.ventus_port.write(b"#W0,1\n")
        else:
            self.ventus_port.write(b"#W0,0\n")

    def play_sound(self, filepath):
        playsound(filepath)

    def breathing(self, rapid_breath):
        while True:
            if rapid_breath:
                breath_path = "C:\\Users\\NOLEL1\\Documents\\LaerdalSkinRetractions\\breathing_sounds\\08INNpust.mp3"

                subcostal_inhale = threading.Thread(target=self.digitalWrite,args=(8,self.subcostal_on,))
                substernal_inhale = threading.Thread(target=self.digitalWrite,args=(8,self.substernal_on,))
                intercostal_inhale = threading.Thread(target=self.digitalWrite,args=(8,self.intercostal_on,))
                clavicular_inhale = threading.Thread(target=self.digitalWrite,args=(8,self.clavicular_on,))
                suprasternal_inhale = threading.Thread(target=self.digitalWrite,args=(8,self.suprasternal_on,))

                

                pump_inhale = threading.Thread(target=self.write_pump,args=(1,))
                sound_inhale = threading.Thread(target=self.play_sound,args=(breath_path,))

                subcostal_inhale.start()
                substernal_inhale.start()
                intercostal_inhale.start()
                clavicular_inhale.start()
                suprasternal_inhale.start()

                pump_inhale.start()
                sound_inhale.start()

                self.subcostal_on = 0
                self.substernal_on = 0
                self.intercostal_on = 0
                self.clavicular_on = 0
                self.suprasternal_on = 0

                time.sleep(1.1)
                subcostal_inhale.join()
                substernal_inhale.join()
                intercostal_inhale.join()
                clavicular_inhale.join()
                suprasternal_inhale.join()
                pump_inhale.join()
                sound_inhale.join()

                breath_path = "C:\\Users\\NOLEL1\\Documents\\LaerdalSkinRetractions\\breathing_sounds\\08UTpust.mp3"

                subcostal_exhale = threading.Thread(target=self.digitalWrite,args=(8,self.subcostal_on,))
                substernal_exhale = threading.Thread(target=self.digitalWrite,args=(8,self.substernal_on,))
                intercostal_exhale = threading.Thread(target=self.digitalWrite,args=(8,self.intercostal_on,))
                clavicular_exhale = threading.Thread(target=self.digitalWrite,args=(8,self.clavicular_on,))
                suprasternal_exhale = threading.Thread(target=self.digitalWrite,args=(8,self.suprasternal_on,))

                pump_exhale = threading.Thread(target=self.write_pump,args=(0,))
                sound_exhale = threading.Thread(target=self.play_sound,args=(breath_path,))

                subcostal_exhale.start()
                substernal_exhale.start()
                intercostal_exhale.start()
                clavicular_exhale.start()
                suprasternal_exhale.start()
                pump_exhale.start()
                sound_exhale.start()

                self.subcostal_on = 1
                self.substernal_on = 1
                self.intercostal_on = 1
                self.clavicular_on = 1
                self.suprasternal_on = 1

                time.sleep(0.9)
                subcostal_exhale.join()
                substernal_exhale.join()
                intercostal_exhale.join()
                clavicular_exhale.join()
                suprasternal_exhale.join()
                pump_exhale.join()
                sound_exhale.join()

            else:
                breath_path = "C:\\Users\\NOLEL1\\Documents\\LaerdalSkinRetractions\\breathing_sounds\\12INNpust.mp3"
                subcostal_inhale = threading.Thread(target=self.digitalWrite,args=(8,self.subcostal_on,))
                substernal_inhale = threading.Thread(target=self.digitalWrite,args=(8,self.substernal_on,))
                intercostal_inhale = threading.Thread(target=self.digitalWrite,args=(8,self.intercostal_on,))
                clavicular_inhale = threading.Thread(target=self.digitalWrite,args=(8,self.clavicular_on,))
                suprasternal_inhale = threading.Thread(target=self.digitalWrite,args=(8,self.suprasternal_on,))

                pump_inhale = threading.Thread(target=self.write_pump,args=(1,))
                sound_inhale = threading.Thread(target=self.play_sound,args=(breath_path,))

                subcostal_inhale.start()
                substernal_inhale.start()
                intercostal_inhale.start()
                clavicular_inhale.start()
                suprasternal_inhale.start()

                pump_inhale.start()
                sound_inhale.start()

                time.sleep(1.5)
                subcostal_inhale.join()
                substernal_inhale.join()
                intercostal_inhale.join()
                clavicular_inhale.join()
                suprasternal_inhale.join()
                pump_inhale.join()
                sound_inhale.join()

                breath_path = "C:\\Users\\NOLEL1\\Documents\\LaerdalSkinRetractions\\breathing_sounds\\12Utpust.mp3"

                subcostal_exhale = threading.Thread(target=self.digitalWrite,args=(8,self.subcostal_on,))
                substernal_exhale = threading.Thread(target=self.digitalWrite,args=(8,self.substernal_on,))
                intercostal_exhale = threading.Thread(target=self.digitalWrite,args=(8,self.intercostal_on,))
                clavicular_exhale = threading.Thread(target=self.digitalWrite,args=(8,self.clavicular_on,))
                suprasternal_exhale = threading.Thread(target=self.digitalWrite,args=(8,self.suprasternal_on,))

                pump_exhale = threading.Thread(target=self.write_pump,args=(0,))
                sound_exhale = threading.Thread(target=self.play_sound,args=(breath_path,))

                subcostal_exhale.start()
                substernal_exhale.start()
                intercostal_exhale.start()
                clavicular_exhale.start()
                suprasternal_exhale.start()
                pump_exhale.start()
                sound_exhale.start()

                time.sleep(1.3)
                subcostal_exhale.join()
                substernal_exhale.join()
                intercostal_exhale.join()
                clavicular_exhale.join()
                suprasternal_exhale.join()
                pump_exhale.join()
                sound_exhale.join()
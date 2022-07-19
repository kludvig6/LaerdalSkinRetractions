""" Based on the 1s-pulse.py. See this program for explaination of serial functions. """

import threading
import time
import serial
import time
from playsound import playsound
from pyfirmata import Arduino, util

board = Arduino("COM9")

iterator = util.Iterator(board)
iterator.start()

valve_pin7 = board.get_pin("d:7:o")
valve_pin8 = board.get_pin("d:8:o")

serial_port = serial.Serial(port="COM8",
                            baudrate=115200,
                            bytesize=8,
                            timeout=2,
                            stopbits=serial.STOPBITS_ONE)
serial_port.write(b"#W2,0\n")
serial_port.write(b"#W0,0\n")
serial_port.write(b"#W10,0\n")
serial_port.write(b"#W11,0\n")
serial_port.write(b"#W23,1000\n")

def write_valve(valve, value):
    if valve == 8:
        valve_pin8.write(value)
    else:
        valve_pin7.write(value)

def write_pump(value):
    if value == 1:
        serial_port.write(b"#W0,1\n")
    else:
        serial_port.write(b"#W0,0\n")

def play_sound(filepath):
    playsound(filepath)

rapid_breath = True

while True:
    if rapid_breath:
        breath_path = "C:\\Users\\NOLEL1\\Documents\\ttpventus_python_library\\breathing_sounds\\08INNpust.mp3"
        valve_8_inhale = threading.Thread(target=write_valve,args=(8,1,))
        valve_7_inhale = threading.Thread(target=write_valve,args=(7,1,))
        pump_inhale = threading.Thread(target=write_pump,args=(1,))
        sound_inhale = threading.Thread(target=play_sound,args=(breath_path,))

        valve_8_inhale.start()
        valve_7_inhale.start()
        pump_inhale.start()
        sound_inhale.start()

        time.sleep(1)
        valve_8_inhale.join()
        valve_7_inhale.join()
        pump_inhale.join()
        sound_inhale.join()

        breath_path = "C:\\Users\\NOLEL1\\Documents\\ttpventus_python_library\\breathing_sounds\\08UTpust.mp3"
        valve_8_exhale = threading.Thread(target=write_valve,args=(8,0,))
        valve_7_exhale = threading.Thread(target=write_valve,args=(7,0,))
        pump_exhale = threading.Thread(target=write_pump,args=(0,))
        sound_exhale = threading.Thread(target=play_sound,args=(breath_path,))

        valve_8_exhale.start()
        valve_7_exhale.start()
        pump_exhale.start()
        sound_exhale.start()

        time.sleep(1)
        valve_8_exhale.join()
        valve_7_exhale.join()
        pump_exhale.join()
        sound_exhale.join()

    else:
        breath_path = "C:\\Users\\NOLEL1\\Documents\\ttpventus_python_library\\breathing_sounds\\inpust.mp3"
        valve_8_inhale = threading.Thread(target=write_valve,args=(8,1,))
        valve_7_inhale = threading.Thread(target=write_valve,args=(7,1,))
        pump_inhale = threading.Thread(target=write_pump,args=(1,))
        sound_inhale = threading.Thread(target=play_sound,args=(breath_path,))

        valve_8_inhale.start()
        valve_7_inhale.start()
        pump_inhale.start()
        sound_inhale.start()

        time.sleep(1)
        valve_8_inhale.join()
        valve_7_inhale.join()
        pump_inhale.join()
        sound_inhale.join()

        breath_path = "C:\\Users\\NOLEL1\\Documents\\ttpventus_python_library\\breathing_sounds\\utpust.mp3"
        valve_8_exhale = threading.Thread(target=write_valve,args=(8,0,))
        valve_7_exhale = threading.Thread(target=write_valve,args=(7,0,))
        pump_exhale = threading.Thread(target=write_pump,args=(0,))
        sound_exhale = threading.Thread(target=play_sound,args=(breath_path,))

        valve_8_exhale.start()
        valve_7_exhale.start()
        pump_exhale.start()
        sound_exhale.start()

        time.sleep(1)
        valve_8_exhale.join()
        valve_7_exhale.join()
        pump_exhale.join()
        sound_exhale.join()
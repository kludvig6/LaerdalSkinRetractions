"""
Based on the 1s-pulse.py. See python-EK-M-015-main/1s-pulse.py for explaination of serial functions.
To use this with an Arduino Uno, you must first upload the StandardFirmata sketch from Arduino.
This can be found in File -> Examples -> Firmata.
"""

import threading
import time
import serial
import time
from playsound import playsound
from pyfirmata import Arduino, util

rapid_breath = True

board = Arduino("COM9")

iterator = util.Iterator(board)
iterator.start()

valve_pin4 = board.get_pin("d:4:o")
valve_pin5 = board.get_pin("d:5:o")
valve_pin6 = board.get_pin("d:6:o")
valve_pin7 = board.get_pin("d:7:o")
valve_pin8 = board.get_pin("d:8:o")
motor_pin2 = board.get_pin("d:2:o")
motor_pin3 = board.get_pin("d:3:o")

ventus_port = serial.Serial(port="COM8",
                            baudrate=115200,
                            bytesize=8,
                            timeout=2,
                            stopbits=serial.STOPBITS_ONE)
ventus_port.write(b"#W2,0\n")
ventus_port.write(b"#W0,0\n")
ventus_port.write(b"#W10,0\n")
ventus_port.write(b"#W11,0\n")

if rapid_breath:
    ventus_port.write(b"#W23,1000\n")
else:
    ventus_port.write(b"#W23,100\n")

def digitalWrite(pin, value):
    if pin == 8:
        valve_pin8.write(value)
    elif pin == 7:
        valve_pin7.write(value)
    elif pin == 6:
        valve_pin6.write(value)
    elif pin == 5:
        valve_pin5.write(value)
    elif pin == 4:
        valve_pin4.write(value)
    elif pin == 3:
        motor_pin3.write(value)
    elif pin == 2:
        motor_pin2.write(value)

def all_valves(value):
    valve_pin8.write(value)
    valve_pin7.write(value)
    valve_pin6.write(value)
    valve_pin5.write(value)
    valve_pin4.write(value)

def writeValveAndMotor(valve_pin, valve_value, motor_pin, motor_value):
    if valve_pin == 8:
        valve_pin8.write(valve_value)
    elif valve_pin == 7:
        valve_pin7.write(valve_value)
    if motor_pin == 3:
        motor_pin3.write(motor_value)
    elif motor_pin == 2:
        motor_pin2.write(motor_value)

def write_pump(value):
    if value == 1:
        ventus_port.write(b"#W0,1\n")
    else:
        ventus_port.write(b"#W0,0\n")

def play_sound(filepath):
    playsound(filepath)

while True:
    valve_8_inhale = threading.Thread(target=digitalWrite,args=(8,1,))
    valve_7_inhale = threading.Thread(target=digitalWrite,args=(7,1,))
    valve_7_inhale.start()
    valve_8_inhale.start()
    time.sleep(1)
    valve_7_inhale.join()
    valve_8_inhale.join()

    valve_7_exhale = threading.Thread(target=digitalWrite,args=(7,0,))
    valve_8_exhale = threading.Thread(target=digitalWrite,args=(8,0,))

    valve_7_exhale.start()
    valve_8_exhale.start()
    time.sleep(1)
    valve_7_exhale.join()
    valve_8_exhale.join()

while True:
    if rapid_breath:
        breath_path = "C:/Users/NOLEL1/Documents/LaerdalSkinRetractions/breathing_sounds/08INNpust.mp3"
        valve_8_inhale = threading.Thread(target=digitalWrite,args=(8,1,))
        valve_7_inhale = threading.Thread(target=digitalWrite,args=(7,1,))
        #valve_inhale = threading.Thread(target=all_valves,args=(1,))
        #valve_motor_inhale = threading.Thread(target=writeValveAndMotor,args=(7,1,3,0))
        #motor_3_inhale = threading.Thread(target=digitalWrite,args=(3,1))
        #motor_2_inhale = threading.Thread(target=digitalWrite,args=(2,0))
        pump_inhale = threading.Thread(target=write_pump,args=(1,))
        sound_inhale = threading.Thread(target=play_sound,args=(breath_path,))

        valve_8_inhale.start()
        valve_7_inhale.start()
        #valve_inhale.start()
        #valve_motor_inhale.start()
        #motor_3_inhale.start()
        #motor_2_inhale.start()
        pump_inhale.start()
        sound_inhale.start()

        time.sleep(1.1)
        valve_8_inhale.join()
        valve_7_inhale.join()
        #valve_inhale.join()
        #valve_motor_inhale.join()
        #motor_3_inhale.join()
        #motor_2_inhale.join()
        pump_inhale.join()
        sound_inhale.join()

        breath_path = "C:/Users/NOLEL1/Documents/LaerdalSkinRetractions/breathing_sounds/08UTpust.mp3"
        
        valve_8_exhale = threading.Thread(target=digitalWrite,args=(8,0,))
        valve_7_exhale = threading.Thread(target=digitalWrite,args=(7,0,))
        #valve_exhale = threading.Thread(target=all_valves,args=(0,))
        #valve_motor_exhale = threading.Thread(target=writeValveAndMotor,args=(7,0,3,1))
        #motor_3_exhale = threading.Thread(target=digitalWrite,args=(3,0))
        #motor_2_exhale = threading.Thread(target=digitalWrite,args=(2,1))
        pump_exhale = threading.Thread(target=write_pump,args=(0,))
        sound_exhale = threading.Thread(target=play_sound,args=(breath_path,))

        valve_8_exhale.start()
        valve_7_exhale.start()
        #valve_exhale.start()
        #valve_motor_exhale.start()
        #motor_3_exhale.start()
        #motor_2_exhale.start()
        pump_exhale.start()
        sound_exhale.start()

        time.sleep(0.9)
        valve_8_exhale.join()
        valve_7_exhale.join()
        #valve_exhale.join()
        #valve_motor_exhale.join()
        #motor_3_exhale.join()
        #motor_2_exhale.join()
        pump_exhale.join()
        sound_exhale.join()

    else:
        breath_path = "C:/Users/NOLEL1/Documents/LaerdalSkinRetractions/breathing_sounds/12INNpust.mp3"
        #valve_8_inhale = threading.Thread(target=digitalWrite,args=(8,1,))
        valve_7_inhale = threading.Thread(target=digitalWrite,args=(7,1,))
        #motor_3_inhale = threading.Thread(target=digitalWrite,args=(3,1))
        #motor_2_inhale = threading.Thread(target=digitalWrite,args=(2,0))
        pump_inhale = threading.Thread(target=write_pump,args=(1,))
        sound_inhale = threading.Thread(target=play_sound,args=(breath_path,))

        #valve_8_inhale.start()
        valve_7_inhale.start()
        #motor_3_inhale.start()
        #motor_2_inhale.start()
        pump_inhale.start()
        sound_inhale.start()

        time.sleep(1.5)
        #valve_8_inhale.join()
        valve_7_inhale.join()
        #motor_3_inhale.join()
        #motor_2_inhale.join()
        pump_inhale.join()
        sound_inhale.join()

        breath_path = "C:/Users/NOLEL1/Documents/LaerdalSkinRetractions/breathing_sounds/12Utpust.mp3"
        
        #valve_8_exhale = threading.Thread(target=digitalWrite,args=(8,0,))
        valve_7_exhale = threading.Thread(target=digitalWrite,args=(7,0,))
        #motor_3_exhale = threading.Thread(target=digitalWrite,args=(3,0))
        #motor_2_exhale = threading.Thread(target=digitalWrite,args=(2,1))
        pump_exhale = threading.Thread(target=write_pump,args=(0,))
        sound_exhale = threading.Thread(target=play_sound,args=(breath_path,))

        #valve_8_exhale.start()
        valve_7_exhale.start()
        #motor_3_exhale.start()
        #motor_2_exhale.start()
        pump_exhale.start()
        sound_exhale.start()

        time.sleep(1.3)
        #valve_8_exhale.join()
        valve_7_exhale.join()
        #motor_3_exhale.join()
        #motor_2_exhale.join()
        pump_exhale.join()
        sound_exhale.join()
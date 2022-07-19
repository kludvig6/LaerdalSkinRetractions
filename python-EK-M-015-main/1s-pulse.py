"""
Turn the pump on at 1W for 1 second, then turn it off
"""

import serial
import time
from playsound import playsound
from pyfirmata import Arduino, util


board = Arduino("COM9")

iterator = util.Iterator(board)
iterator.start()

valve_pin9 = board.get_pin("d:7:o")
valve_pin8 = board.get_pin("d:8:o")


# set up port – replace COM port number with the COM port you are using
serial_port = serial.Serial(port="COM8",
                            baudrate=115200,
                            bytesize=8,
                            timeout=2,
                            stopbits=serial.STOPBITS_ONE)

# turn off data streaming mode
serial_port.write(b"#W2,0\n")

# turn the pump off whilst configuring system
serial_port.write(b"#W0,0\n")

# set the pump to manual control mode
serial_port.write(b"#W10,0\n")

# set the drive power input to register 23
serial_port.write(b"#W11,0\n")

# set the drive power set point to 1000 mW
serial_port.write(b"#W23,1000\n")

rapid_breath = True

while True:
    if rapid_breath:
        valve_pin9.write(1)
        valve_pin8.write(1)
        serial_port.write(b"#W0,1\n")
        playsound("C:\\Users\\NOLEL1\\Documents\\ttpventus_python_library\\breathing_sounds\\inpustrask.mp3")
        time.sleep(0.5)

        valve_pin8.write(0)
        valve_pin9.write(0)
        serial_port.write(b"#W0,0\n")
        playsound("C:\\Users\\NOLEL1\\Documents\\ttpventus_python_library\\breathing_sounds\\utpustrask.mp3")
        time.sleep(0.5)

    else:
        valve_pin9.write(1)
        valve_pin8.write(1)
        serial_port.write(b"#W0,1\n")
        playsound("C:\\Users\\NOLEL1\\Documents\\ttpventus_python_library\\breathing_sounds\\inpust.mp3")
        time.sleep(2)

        valve_pin8.write(0)
        valve_pin9.write(0)
        serial_port.write(b"#W0,0\n")
        playsound("C:\\Users\\NOLEL1\\Documents\\ttpventus_python_library\\breathing_sounds\\utpust.mp3")
        time.sleep(2)

# close serial port
serial_port.close()

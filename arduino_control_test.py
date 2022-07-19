import time
from pyfirmata import Arduino, util

board = Arduino("COM10")

iterator = util.Iterator(board)
iterator.start()

valve_pin8 = board.get_pin("d:9:p")

while True:
    board.digital[9].write(1)
    #valve_pin8.write(1)
    time.sleep(4)
    board.digital[9].write(0)
    #valve_pin8.write(0)
    time.sleep(1)
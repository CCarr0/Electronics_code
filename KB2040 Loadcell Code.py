import time
import board
import analogio
import digitalio

load = analogio.AnalogIn(board.A0)

SmallLoad = digitalio.DigitalInOut(board.D3)
SmallLoad.direction = digitalio.Direction.OUTPUT
MedLoad = digitalio.DigitalInOut(board.D4)
MedLoad.direction = digitalio.Direction.OUTPUT
HighLoad = digitalio.DigitalInOut(board.D5)
HighLoad.direction = digitalio.Direction.OUTPUT

def read_load():
    return (load.value/65535) * 5

while True:
    voltage = (load.value / 65535) * 5
    print(f"{voltage:.3f}")   # send clean number
    time.sleep(0.5)
    if voltage < 2.2:
        SmallLoad.value = True
        MedLoad.value = False
        HighLoad.value = False
    elif voltage > 2.4 and voltage < 2.8:
        SmallLoad.value = False
        MedLoad.value = True
        HighLoad.value = False
    elif voltage > 3:
        SmallLoad.value = False
        MedLoad.value = False
        HighLoad.value = True

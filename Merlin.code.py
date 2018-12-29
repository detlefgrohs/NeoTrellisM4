import math
import time
import array
import board
import busio
import audioio
import adafruit_trellis_express
import adafruit_adxl34x

time.sleep(10.0)

trellis = adafruit_trellis_express.TrellisM4Express(rotation=90)

i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)

print('Starting up...')

# Clear all pixels
trellis.pixels._neopixel.fill((255, 0, 0))
trellis.pixels._neopixel.show()

color = 0

while True:
    print('In loop')
    stamp = time.monotonic()

    trellis.pixels._neopixel.fill((color, color, color))
    trellis.pixels._neopixel.show()

    color = color + 1
    if color > 255:
        color = 0

    while time.monotonic() - stamp < 0.1:
        time.sleep(0.01)  # a little delay here helps avoid debounce annoyances


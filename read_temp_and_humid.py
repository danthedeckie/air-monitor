import sys
import time

import board
import adafruit_shtc3

from df_aio import DFAIO

SLEEP_TIME = 20.0

i2c = board.I2C()
sht = adafruit_shtc3.SHTC3(i2c)

df = DFAIO()

TEMP = "temp"
HUMID = "humidity"

feed_temp = df.get_or_create_feed(TEMP)
feed_humid = df.get_or_create_feed(HUMID)

while True:
    temp, humidity = sht.measurements
    # print("%s,%s" % (temp, humidity))
    df.post(TEMP, temp)
    df.post(HUMID, humidity)
    sys.stdout.flush()
    time.sleep(SLEEP_TIME)

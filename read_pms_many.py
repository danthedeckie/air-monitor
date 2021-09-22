import sys
from time import sleep

from df_aio import DFAIO
from pms_a003 import Sensor

df = DFAIO()

# Names to be lowercase, as retrival keys are lowercase...
PM10 = "pm10"
PM25 = "pm25"
PM100 = "pm100"

feed_pm10 = df.get_or_create_feed(PM10)
feed_pm25 = df.get_or_create_feed(PM25)
feed_pm100 = df.get_or_create_feed(PM100)

SLEEP_TIME = 30.0


air_mon = Sensor()
air_mon.connect_hat(port="/dev/ttyAMA0", baudrate=9600)

while True:
    values = air_mon.read()
    # print("{},{},{}".format(values.pm10_cf1, values.pm25_cf1, values.pm100_cf1))
    df.post(PM10, values.pm10_cf1)
    df.post(PM25, values.pm25_cf1)
    df.post(PM100, values.pm100_cf1)
    sys.stdout.flush()
    sleep(SLEEP_TIME)

air_mon.disconnect_hat()

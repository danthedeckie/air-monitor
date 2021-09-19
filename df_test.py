import time
import sys

from sgp30 import SGP30

from df_aio import DFAIO

df = DFAIO()

CO2 = 'co2'
TVOC = 'tvoc'

feed_co2 = df.get_or_create_feed(CO2)
feed_tvoc = df.get_or_create_feed(TVOC)

SLEEP_TIME=20.0

sgp30 = SGP30()

# result = sgp30.command('set_baseline', (0xFECA, 0xBEBA))
# result = sgp30.command('get_baseline')
# print(["{:02x}".format(n) for n in result])

print("Sensor warming up, please wait...")
def crude_progress_bar():
    sys.stdout.write('.')
    sys.stdout.flush()

sgp30.start_measurement(crude_progress_bar)
sys.stdout.write('\n')

while True:
    result = sgp30.get_air_quality()
    print('%s,%s'%(result.equivalent_co2, result.total_voc))
    df.post(CO2, result.equivalent_co2)
    df.post(TVOC, result.total_voc)
    sys.stdout.flush()
    time.sleep(SLEEP_TIME)

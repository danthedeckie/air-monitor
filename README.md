# Air monitoring -> Adafruit IO

This project takes data from an:
- SGP30 (CO2 and TVOC over I2C)
- PMS A003 (PM1, PM2.5, PM10)
- SHTC3 (temperature and relative humidity over I2C)
and pushes them to Adafruit IO.

# TO USE:

You'll need to put your adafruit.io username & API key into environment variables:

```sh
export IO_USERNAME="<my username>"
export IO_KEY="<my API key>"
```

# References

- https://github.com/pimoroni/sgp30-python
- https://github.com/sbcshop/Air-Monitoring-Breakout (pms_a003.py comes straight from there)
- io.adafruit.com

# Other notes:

To get the 3 components working, I needed to turn ON the I2C interface w/ `raspbi-config`,
and I added these to my `/boot/config.txt`:

```ini
enable_uart=1
dtoverlay=disable-bt
```

# TODO / Roadmap:

- Quiet mode (so it can run w/o posting things to a local log file & disk IO on pi)
- Better install / test scripts
- Common interfaces for monitoring device & logging output
- Sampling (eg. read values ever second, post average or peak or trough every 30 seconds to logs..)
- catch common errors / retrying if network fails, etc.
- humidity / temperature monitoring too.
- deployment helps (systemd files...)
- alternative logging outputs (Sqlite? prometheus? other HTTP endpoints for remote logging? local tiny screen?)

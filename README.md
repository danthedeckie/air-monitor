# Air monitoring -> Adafruit IO

This project takes data from an SGP30 (CO2 and TVOC) and PMS A003 (PM1, PM2.5, PM10) values
and pushes them to Adafruit IO.

# TO USE:

You'll need to put your adafruit.io username & API key into environment variables:

```sh
export IO_USERNAME="<my username>"
export IO_KEY="<my API key>"
```

# References

- https://github.com/pimoroni/sgp30-python
- https://github.com/sbcshop/Air-Monitoring-Breakout
- io.adafruit.com

# Other notes:

To get the 2 components working, I needed to turn ON the I2C interface w/ `raspbi-config`,
and I added these to my `/boot/config.txt`:

```ini
enable_uart=1
dtoverlay=disable-bt
```

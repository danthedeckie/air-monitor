# This is one way to deploy this...

I don't know if it's the best though!

- Edit the service files for appropriate paths.
- Edit /etc/adafruit_io.conf to have the correct env vars in `ENV=value` format.

```sh
cp ./deployment/co2_and_tvoc_monitor.service /etc/systemd/system/co2_and_tvoc_monitor.service
sudo systemctl daemon-reload
sudo systemctl enable co2_and_tvoc_monitor.service
sudo service co2_and_tvoc_monitor start
```

and then you can monitor the log files:

```sh
journalctl -b -e -f
```

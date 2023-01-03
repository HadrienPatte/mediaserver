# Mediaserver

## Setup

Download [ubuntu image](https://ubuntu.com/download/raspberry-pi) and extract it in [ubuntu](./ubuntu):

```
xz -d ubuntu/ubuntu-22.04.1-preinstalled-server-arm64+raspi.img.xz
```

# Hardware setup

Connect BME280 sensor to raspberry pi like so:
* VIN - P1 (3V3)
* GND - P9 (Ground)
* SCL - P5 (I2C1 SCL)
* SDA - P3 (I2C1 SDA)

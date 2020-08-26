#!/bin/sh
apt-get update -y
apt-get upgrade -y
apt-get install fonts-dejavu
pip3 install --upgrade pip setuptools wheel
pip3 install inky pytz spidev RPI.gpio smbus2 numpy Pillow

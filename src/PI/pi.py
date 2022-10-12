#!/usr/bin/python3
import urllib.request as urq
import PILIB.i2c as i2c
import time

while True:
    try:
        temp = urq.urlopen("http://192.168.1.6:8080").read().decode("utf-8")
        i2c.i2c.write(temp)
        temp = 0
    except:
        i2c.i2c.write(0)
    time.sleep(6)

#!/usr/bin/python3

from smbus import SMBus
class i2c:
    def write(temp):
        addr = 0x8 # bus address
        bus = SMBus(1) # indicates /dev/ic2-1
        try:
            bus.write_byte(addr, int(temp)) # send value
        except:
            return -1
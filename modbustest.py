#!/usr/bin/python
import minimalmodbus
instrument = minimalmodbus.Instrument("/dev/ttyS6", 0, minimalmodbus.MODE_RTU)
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout = 0.05

raw_req = "\x04\x05\x00\x01\xFF\x00\xDD\xAF"
try:
    instrument._communicate(raw_req, 3)
except Exception:
    pass

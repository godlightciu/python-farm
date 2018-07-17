#!/usr/bin/python

import cgi
import minimalmodbus
instrument = minimalmodbus.Instrument("/dev/ttyS6", 0, minimalmodbus.MODE_RTU)
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout = 0.05
reshtml = '''Content-Type: text/html\n
<HTML><HEAD><TITLE>
send modbus request demo
</TITLE></HEAD>
<BODY><H3>You have <B>%s</B> successfully!
</BODY></HTML>'''

form = cgi.FieldStorage()
if form["con"].value == "open_v4":
	raw_req = "\x04\x05\x00\x01\xFF\x00\xDD\xAF"
elif form["con"].value == "close_v4":
	raw_req = "\x04\x05\x00\x01\x00\x00\x9C\x5F"
elif form["con"].value == "open_v11":
	raw_req = "\x0B\x05\x00\x01\xFF\x00\xDD\x50"
elif form["con"].value == "close_v11":
	raw_req = "\x0B\x05\x00\x01\x00\x00\x9C\xA0"
try:
	instrument._communicate(raw_req, 3)
except Exception:
	pass
print reshtml %(form["con"].value)

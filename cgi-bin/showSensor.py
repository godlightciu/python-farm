!/usr/bin/python

import cgi
import minimalmodbus
instrument = minimalmodbus.Instrument("/dev/ttyS6", 1)#十进制的从站地址1
instrument.serial.baudrate = 9600
#instrument.serial.bytesize = 8
#instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
#instrument.serial.stopbits = 1
#instrument.serial.timeout = 0.05


## Read temperature (PV = ProcessValue) ##
temperature = instrument.read_register(32, 1) # Registernumber, number of decimals十进制！
t2 = instrument.read_register(33, 1)
t3 = instrument.read_register(33, 1)
t4 = instrument.read_register(34, 1)

# return page
reshtml = '''Content-Type: text/html\n
<HTML><HEAD><TITLE>
show sensor demo
</TITLE></HEAD>
<BODY><H3>Sensor value: \n<B>%s</B> \n<B>%s</B> \n<B>%s</B> \n<B>%s</B> 
</BODY></HTML>'''
print reshtml %(temperature,t2,t3,t4)

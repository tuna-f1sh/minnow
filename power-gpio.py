"""
Example to toggle the power of the target board using the FTDI CBUS GPIO
"""
import time

from pyftdi.ftdi import Ftdi
from pyftdi.eeprom import FtdiEeprom

ftdi = Ftdi()
ftdi.open_from_url('ftdi:///1')

# validate CBUS EEPROM configuration with the current device
eeprom = FtdiEeprom()
eeprom.connect(ftdi)
# here we confirm CBUS3 is GPIO
assert eeprom.cbus_mask & 0b1000 == 0b1000
# configure CBUS3 as output
ftdi.set_cbus_direction(0b1000, 0b1000)
# set CBUS3 - power disable
print('Power off')
ftdi.set_cbus_gpio(1 << 3)
time.sleep(1)
print('Power on')
# set CBUS3 - power enable
ftdi.set_cbus_gpio(0 << 3)

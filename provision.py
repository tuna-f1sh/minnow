"""
Provision a new Minnow device with a unique incrementing serial number and records the device and serial number in a file

Writes the EEPROM './pyftdi-minnow.ini' file with the device serial number
"""
import os
import sys
import datetime
import logging

from pyftdi.ftdi import Ftdi
from pyftdi.bin import ftconf

logger = logging.getLogger('provision')
logging.basicConfig(level=logging.INFO)

def select_device(devices):
    """
    Returns first device or allows user input to select index to use
    """
    if not devices or len(devices) == 0:
        raise RuntimeError("No devices found")

    print(f"Found devices:")
    for i, d in enumerate(devices):
        print(f"[{i}]: {d}")
    if len(devices) > 1:
        # let user select device to use
        return devices[int(input("Enter device index to use: "))]
    else:
        return devices[0]

def get_first_device():
    """Return the first FTDI device found"""
    devices = Ftdi.list_devices_urls()
    return select_device(devices)

def get_device_num(fn: str = 'devices.txt'):
    # create file if not exists
    if not os.path.isfile(fn):
        logger.warning(f"Creating {fn}")
        open(fn, 'w').close()

    with open(fn, 'r') as f:
        lines = f.readlines()
        return len(lines)

VERSION = 0x1
DEVICE = get_first_device()[0]
DT = datetime.datetime.now()
YEAR = DT.year % 100
FILE = f'./devices_{YEAR:02d}{VERSION:01x}.txt'
NUM = get_device_num(FILE)
SERIAL = f'{YEAR:02d}{VERSION:01x}{NUM:04d}'
logger.info(f"Configuring device: {DEVICE}, serial: {SERIAL}")

with open(FILE, 'a') as f:
    f.write(f'{DT.isoformat()},{DEVICE},{SERIAL}\n')

# args for ftconf
sys.argv.extend(['-d', DEVICE, '-i' './pyftdi-minnow.ini', '-s', SERIAL, '-u'])

ftconf.main()

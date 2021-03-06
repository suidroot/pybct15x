#!/usr/bin/which python3
# Group 2 enable/disable Uniden BCT15X Scanner 
#
# Author: Ben Mason
# Version: 0.1
#
import pyuniden

__author__ = "Ben Mason"
__version__ = "0.1"
__email__ = "locutus@the-collective.net"

PORT = '/dev/ttyACM0'
SPEED = 115200

scanner = pyuniden.Unidenrc()
scanner.openserial(PORT, SPEED)
scanner.pushbutton("2","P",function=True)
scanner.closeserial()


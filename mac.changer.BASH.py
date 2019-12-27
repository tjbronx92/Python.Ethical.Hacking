#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

(options, arguments) = parser.parse_args()

interface = options.interface
mac_addr = options.new_mac

interface = input("Enter Interface ==>")
mac_addr = input("Enter New MAC Address ==>")

print("[+] Changing MAC address for" + interface + " to " + mac_addr)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw ether", mac_addr])
subprocess.call(["ifconfig", interface, "up"])

#! /bin/bash/python3
# Save current config to a file for support
import time
import os
from netmiko import ConnectHandler

ipaddress = "10.199.199.250"  # example
print("I'll attempt to ping: " + ipaddress)
response = os.system("ping -c 1 " + ipaddress)

#and then check the response...
if response == 0:
    print(ipaddress, 'is up!')
    print("The current time is:", time.asctime())
else:
    print(ipaddress, 'is down!')

SW1 = {
    'device_type': 'cisco_ios',
    'host':   ipaddress,
    'username': 'admin',
    'password': 'cisco',
    'port': 22,          # optional, defaults to 22
    'secret': 'cisco',     # optional, defaults to ''
}

net_connect = ConnectHandler(**SW1)
output = net_connect.send_command('show version')
print(output)

#! /bin/bash/python3
# Save current config to a file for support
import time
import os
ipaddress = "10.199.199.250"  # example
print("I'll attempt to ping: " + ipaddress)
response = os.system("ping -c 1 " + ipaddress)

#and then check the response...
if response == 0:
    print(ipaddress, 'is up!')
    print("The current time is:", time.asctime())
else:
    print(ipaddress, 'is down!')

#! /bin/bash/python3
# Telnetexample connecting to a switch and configuring vlans
import getpass
import telnetlib
import time
import os

ipaddress = input("Enter the IP Address of Device: ")  # example
print("I'll attempt to ping: " + ipaddress)
response = os.system("ping -c 3 " + ipaddress)

#and then check the response...
if response == 0:
    print(ipaddress, 'is up!')
    print("The current time is:", time.asctime())

    user = input("Enter your cisco username: ")
    password = getpass.getpass()

    tn = telnetlib.Telnet(ipaddress)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")

    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"terminal len 0\n")
    tn.write(b"configure terminal\n")
    for x in range(10, 31):  # VLAN10 -> VLAN30
        tn.write("vlan {}\n".format(x).encode())
        tn.write("name VLAN{}\n".format(x).encode())

        tn.write(b"exit\n")
        tn.write(b"exit\n")
        tn.write(b"write memory\n")
        tn.write(b"exit\n")
        tn.write(b"exit\n")

        str_object = ("VLAN{} was added to the switch".format(x).encode())
        #str_object = str_object.decode()
        print(str_object.decode())
        print(tn.read_all().decode('ascii'))
    print("The loop ended here")

else:
    print(ipaddress, 'is down!')

print("\n")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("The script ended.")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

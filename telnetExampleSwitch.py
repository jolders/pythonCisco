#! /bin/bash/python3
# Telnetexample connecting to a switch and configuring vlans
import getpass
import telnetlib

HOST = input("Enter the IP Address of Device: ")
user = input("Enter your cisco username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"terminal len 0\n")
tn.write(b"configure terminal\n")
# VLAN 10
tn.write(b"vlan 10\n")
tn.write(b"name SALES\n")
tn.write(b"exit\n")
# VLAN 20
tn.write(b"vlan 20\n")
tn.write(b"name ACCOUNTS\n")
tn.write(b"exit\n")
# VLAN 30
tn.write(b"vlan 30\n")
tn.write(b"name DISTRIBUTION\n")
tn.write(b"exit\n")

tn.write(b"exit\n")
tn.write(b"write memory\n")

print(tn.read_all().decode('ascii'))
print("Addition of VLANS to a switch has completed")

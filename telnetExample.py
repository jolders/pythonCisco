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
tn.write(b"hostname RTR1\n")
# tn.write(b"router eigrp 100\n")
# tn.write(b"no auto-summary\n")
# tn.write(b"network 0.0.0.0\n")
tn.write(b"exit\n")
# tn.write(b"exit\n")
tn.write(b"show ip protocol\n")
tn.write(b"show version\n")
tn.write(b"show ip interface brief\n")
tn.write(b"write memory\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))

#! /bin/bash/python3
# Telnetexample connecting to a switch saving the 'show run'
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
tn.write(b"show running-config\n")
tn.write(b"show ip interface brief\n")
tn.write(b"show vlan\n")

tn.write(b"exit\n")
tn.write(b"exit\n")

readoutput = tn.read_all()
saveoutput = open("Device " + HOST + ".txt", "w")
saveoutput.write(readoutput.decode('ascii'))
saveoutput.close()

print(tn.read_all().decode('ascii'))
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("<-- Script has completed --->")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

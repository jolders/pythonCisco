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
for x in range(10, 30):  # VLAN10 -> VLAN30
    tn.write("vlan {}\n".format(x).encode())
    tn.write("name VLAN{}\n".format(x).encode())


tn.write(b"exit\n")
tn.write(b"exit\n")
tn.write(b"write memory\n")
tn.write(b"exit\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("Addition of VLANS to a switch has completed.")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

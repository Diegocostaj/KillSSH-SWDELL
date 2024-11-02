import getpass
import telnetlib
import socket
import time
import subprocess
import os
from pynput.keyboard import Key, Controller
keyb = Controller()

Password = "gftr21b;"
login = "admin"
enable = "enable"
HOST = input("Digite IP Avocent: ")
PORT = input("insira o numero da port: ")

tn = telnetlib.Telnet(HOST, PORT)
tn.set_debuglevel(1)

#Pressionar enter para ir para o Login
from pynput.keyboard import Key, Controller
keyb = Controller()
keyb.press(Key.enter)
#time.sleep(2)

#Lê o login e digita a senha
tn.read_until(b"login: ")
tn.write(login.encode('ascii') + b"\n")
#time.sleep(2)
tn.read_until(b"Password: ")
tn.write(Password.encode('ascii') + b"\n")

#Pressiona enter para ir par aenable
from pynput.keyboard import Key, Controller
keyb = Controller()
keyb.press(Key.enter)

#digita enable para ir para password
tn.write(enable.encode('ascii') + b"\n")
#time.sleep(2)

#DIGITA PASSWORD para modo previlegiado
tn.read_until(b"Password: ")
tn.write(Password.encode('ascii') + b"\n")

tn.write(b"remote-exec cp ps -aux | grep ssh | grep -v grep | awk '{print $2}' | xargs kill -9\n")
#time.sleep(1)
tn.write(b"configure terminal\n")
#time.sleep(1)
tn.write(b"no ip ssh server enable\n")
#time.sleep(1)
tn.write(b"ip ssh server enable\n")

#tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))

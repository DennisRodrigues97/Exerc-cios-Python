import os

name = input("DEVICE NAME: ")
ip = input("IP: ")
os.system(f'adb -s {name} tcpip 5555 ')
os.system(f'adb connect {ip}:5555')
#!/usr/bin/env python
import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet VPN KONTROL")
print("""
VPN KONTROL ARACINA HOS GELDIN 

""")

hedefip = input("Hedef Ip Girin : ")
os.system("ike-scan " + hedefip)
#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet GUVENLIK DUVARI TESPIT")
print("""
Güvenlik duvarı tespit programına hoş geldin.

""")

site = input("Site adresi giriniz : ")
os.system("wafw00f " +site)

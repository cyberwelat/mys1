#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet ZAFIYET ANALIZI")
print("""
Hos Geldiniz Arac Baslatiliyor.

""")

os.system("lynis audit system")

print("""
      
ACIKLAMA BOLUMU
      
""")
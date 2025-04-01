#!/usr/bin/env python
import os
os.system("sudo apt update")
os.system("apt-get install figlet")
os.system("apt install crunch")
os.system("clear")
os.system("figlet WORDLIST OLUSTURMA ARACI")
print("""
Wordlist olusturma aracina hos geldin.

""")

minimum = input("Minimum Karakter Giriniz : ")
maxsimum = input("Maxsimum Karakter Giriniz : ")
karakter = input("Istediginiz Karakteri Giriniz : ")
os.system("crunch " + minimum +  " " + maxsimum + " " + karakter)

print("Basariyla Tamamlandi.")  

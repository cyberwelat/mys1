#!/usr/bin/env/ python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet ZAFIYET ANALIZI")
print("""
Zafiyet analizi programına hoş geldiniz.

""")
hedefip = input("Hedef Ip Giriniz: ")
os.system("nikto -h " +hedefip)

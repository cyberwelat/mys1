#!/usr/bin/env python
import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Cyber Mysorfilox P.TARAMA")
print("""
Port tarama aracına hoş geldin :)    

1) Hızlı Tarama
2) Servis ve Versiyon Bilgisi
3) İsletim sistemi Bilgisi

""")

islemno = input("İslem Numarasını Girin: ")

if(islemno=="1"):
          hedefip = input("Hedef Ip Girin: ")
          os.system("nmap " +hedefip)
elif(islemno=="2"):
          hedefip = input("Hedef Ip Girin: ")
          os.system("nmap -sS -sV " + hedefip)
elif(islemno=="3"):
          hedefip = input("Hedef Ip Girin:" )
          os.system("nmap -O " + hedefip)
else:
         print("Hatalı Seçim Yaptın!")

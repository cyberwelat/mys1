#!/usr/bin/env python
import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet  MAC DEGISTIRME ")
print("""
MAC DEGISTIRME ARACINA HOS GELDIN 

1) Random MAC Belirle
2) Elle belirle
3) Orjinal MAC adresine Don

""")

islemno = input("Islem Numarasini Giriniz : ")

if(islemno=="1"):
    os.system("ifconfig wlan0 down")
    os.system("macchanger -r wlan0")
    os.system("ifconfig wlan0 up")
    print("Yeni MAC Adresi Random Belirlendi!")
elif(islemno=="2"):
    macadres = input("Yeni MAC Adresi Girin : ")
    os.system("ifconfig wlan0 down")
    os.system("macchanger --mac " + macadres + " wlan0")
    os.system("ifconfig wlan0 up")
    print("Yeni MAC Adresi Elle Belirlendi!")
elif(islemno=="3"):
    os.system("ifconfig wlan0 down")
    os.system("macchanger -p wlan0")
    os.system("ifconfig wlan0 up")
    print("MAC Adresi Orjinale Dondu!")

else:
    print("Hatali Tuslama Yaptiniz!")
    os.system("python mac.py")

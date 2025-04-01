#!/usr/bin/env python
import os
os.system("sudo apt update")
os.system("sudo apt upgrade")
os.system("sudo apt-get install figlet")
os.system("clear")
os.system("sudo figlet MYS OTURUMU")

print("""
Mys Oturumuna Hos Geldin!
""")
print("""
1)Lynis Zafiyet Analizi
2)Trojen Olusturma
3)Veri Tabanı Çalmak
4)Trojen Dinleyici
5)Güvenlik Duvarı Tespiti
6)Zafiyet Analizi Nikto
7)Exploit Arama
8)Port Tarama
9)VPN Kontrol
10)WORDPRESS Tarama
11)MAC Değiştirme
12)Açık Port Taraması
13)Wordlist Oluşturma
14)Cupp (Wordlis Oluşturucu)
15)Ağ Tarayıcı
""")
secim = input("Program No Giriniz : ")
if(secim=="1"):
    os.system("python zafiyet-analizi-lynis.py")
elif(secim=="2"):
    os.system("python trojen-olusturma.py")
elif(secim=="3"):
    os.system("python veri-tabani-calma.py")
elif(secim=="4"):
    os.system("python3 dinleyici.py")
elif(secim=="5"):
    os.system("python güvenlik-duvari-tespit.py")
if(secim=="6"):
    os.system("python zafiyet-analizi.py")
elif(secim=="7"):
    os.system("python exploit-arama.py")
elif(secim=="8"):
    os.system("python porttarama.py")
elif(secim=="9"):
    os.system("python3 vpn-kontrol.py")
elif(secim=="10"):
    os.system("python3 wordpress.py")
if(secim=="11"):
    os.system("python mac.py")
elif(secim=="12"):
    os.system("python3 port.py")
elif(secim=="13"):
    os.system("python wordlist.py")
elif(secim=="14"):
    os.system("python3 cupp.py -i")
elif(secim=="15"):
    os.system("python ag-tarayici.py")

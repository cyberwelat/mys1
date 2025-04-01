import scapy.all as scapy
import optparse
import os

os.system("figlet MYS AG TARAYICI")

def giris():
    karsvegas = optparse.OptionParser()
    karsvegas.add_options("-i","--ipadres",dest="ip_adresi",help="-i veya --ipadres yazarak ip adresi giriniz.")
    
    (user_giris,arguments)= karsvegas.parse_args()
    if not user_giris.ip_adresi:
        print("ip adresini duzgun giriniz.")
        
    return user_giri
def tarayici(ip):
    istek_paket = scapy.ARP(pdst="192.168.1.1/24")
    #scapy.ls(scapy.ARP())
    yayin_paket = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")#burasimacicin
    #scapy.ls(scapy.Ether())
    paket = yayin_paket/istek_paket
    (asilpaket,gecersizpaket)= scapy.srp(paket,timeout=1)
    asilpaket.summary()
    
ipadresim = giris
tarayici(ipadresim)

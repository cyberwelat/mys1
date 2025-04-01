
import pywhatkit as kit
import time
from tqdm import tqdm
from colorama import init, Fore, Style

# Renkli çıktılar için Colorama'yı başlat
init(autoreset=True)

def send_whatsapp_message(phone_number, message, delay=10):
    """
    WhatsApp üzerinden belirli bir numaraya mesaj gönderir.
    :param phone_number: Hedef telefon numarası (ülke kodu ile birlikte, örneğin "+901234567890")
    :param message: Gönderilecek mesaj
    :param delay: WhatsApp Web'in açılması için bekleme süresi (saniye cinsinden)
    """
    try:
        kit.sendwhatmsg_instantly(phone_number, message, wait_time=delay)
        print(Fore.GREEN + f"✅ {phone_number} numarasına mesaj gönderildi: {message}")
    except Exception as e:
        print(Fore.RED + f"❌ Hata oluştu: {e}")

def main():
    print(Fore.BLUE + Style.BRIGHT + "\n🌟 WhatsApp Mesaj Gönderme Aracı 🌟")
    print(Fore.CYAN + "Bu araç, belirttiğiniz numaraya istediğiniz sayıda mesaj göndermenize yardımcı olur.\n")

    # Kullanıcıdan girişleri al
    phone_number = input(Fore.YELLOW + "Hedef telefon numarasını girin (ülke kodu ile birlikte, örneğin +901234567890): ")
    message = input(Fore.YELLOW + "Göndermek istediğiniz mesajı yazın: ")
    total_messages = int(input(Fore.YELLOW + "Kaç kere göndermek istiyorsunuz? "))

    print(Fore.MAGENTA + f"\nToplam {total_messages} adet mesaj gönderilecek...")
    print(Fore.CYAN + "Lütfen WhatsApp Web'in açılmasını bekleyin.\n")

    # Mesajları gönder
    for i in tqdm(range(total_messages), desc="Mesajlar gönderiliyor", unit=" mesaj"):
        send_whatsapp_message(phone_number, message)
        time.sleep(2)  # WhatsApp Web'in hız sınırını aşmamak için bekleme süresi

    print(Fore.GREEN + Style.BRIGHT + "\n🎉 Mesaj gönderme işlemi tamamlandı!")

if __name__ == "__main__":
    main()


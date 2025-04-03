from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import os

# AES ile şifreleme fonksiyonu
def encrypt_file(file_name, password):
    key = password.encode('utf-8')[:16]  # AES için 16 byte'lık anahtar
    cipher = AES.new(key, AES.MODE_CBC)
    with open(file_name, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher.encrypt(pad(file_data, AES.block_size))

    # Şifreli dosyayı kaydetme
    with open(file_name + '.enc', 'wb') as file:
        file.write(cipher.iv)  # IV'yi dosyaya ekle
        file.write(encrypted_data)

# AES ile şifre çözme fonksiyonu
def decrypt_file(encrypted_file_name, password):
    key = password.encode('utf-8')[:16]  # AES için 16 byte'lık anahtar
    with open(encrypted_file_name, 'rb') as file:
        iv = file.read(16)  # IV dosyadan al
        encrypted_data = file.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    # Çözülmüş dosyayı kaydetme
    with open('decrypted_' + encrypted_file_name[:-4], 'wb') as file:
        file.write(decrypted_data)

# Kullanıcıdan dosya ve şifre almak
file_name = input("Şifrelenecek dosyanın adını girin: ")
password = input("Şifreyi girin: ")

# Şifreleme
encrypt_file(file_name, password)
print(f"{file_name} başarıyla şifrelendi.")

# Dosya çözme işlemi
encrypted_file_name = file_name + '.enc'
decrypt_file(encrypted_file_name, password)
print(f"{encrypted_file_name} başarıyla çözüldü.")

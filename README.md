
# File Encryptor & Decryptor - AES Encryption Tool

Bu Python tabanlı araç, dosyalarınızı **AES (Advanced Encryption Standard)** şifreleme algoritması ile şifrelemenizi ve şifresini çözmenizi sağlar. Kullanıcılar, dosyalarını seçip güvenli bir şekilde şifreleyebilir ve yalnızca doğru şifre ile çözülebilir hale getirebilir.

## Özellikler
- Dosya şifreleme ve şifre çözme
- AES şifreleme algoritması kullanarak yüksek güvenlik
- Şifreli dosyaların otomatik olarak `.enc` uzantısı ile kaydedilmesi
- Kolay kullanım için basit komut satırı arayüzü

## Kullanım

### Gereksinimler
- Python 3.x
- PyCryptodome kütüphanesi

### Adım 1: Gereksinimleri Yükleyin
Bu projeyi kullanabilmek için `PyCryptodome` kütüphanesini yüklemeniz gerekmektedir. Bunu aşağıdaki komut ile yükleyebilirsiniz:

```bash
pip install pycryptodome
```

### Adım 2: Dosya Şifreleme
Dosyanızı şifrelemek için, şifrelemek istediğiniz dosyanın adı ve bir şifre girmeniz gerekecek. Aşağıdaki komutları izleyerek şifreleme işlemi yapabilirsiniz:

1. `encrypt_file` fonksiyonu ile dosyanızı şifreleyin.
2. Şifreli dosya `.enc` uzantısı ile kaydedilecektir.

```bash
python encrypt_decrypt.py
```

### Adım 3: Dosya Şifre Çözme
Şifreli dosyayı çözmek için doğru şifreyi girmeniz yeterli olacak. Şifreli dosyanın adı `.enc` uzantılı olacaktır.

```bash
python encrypt_decrypt.py
```

### Adım 4: Çıktılar
- Şifreli dosya: `filename.enc`
- Çözülen dosya: `decrypted_filename`

## Kullandığınız Şifreleme Algoritması

Bu araç, dosyaları **AES (Advanced Encryption Standard)** şifreleme algoritması kullanarak şifreler. AES, güvenliği ve hızını kanıtlamış bir simetrik anahtar şifreleme algoritmasıdır.

## Katkıda Bulunma

Eğer bu projeye katkıda bulunmak isterseniz, lütfen aşağıdaki adımları takip edin:
1. Bu projeyi forklayın.
2. Yeni bir özellik ekleyin veya hatayı düzeltin.
3. Pull request oluşturun.

## Lisans
Bu proje **MIT Lisansı** ile lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

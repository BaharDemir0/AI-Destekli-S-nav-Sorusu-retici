# AI Destekli Sınav Sorusu Üretici - Kurulum ve Kullanım

Bu Proje **İskenderun Teknik Üniversitesi Mühendislikte Bilgisayar Uygulamaları I** dersi için geliştirilmiştir.

## 📦 Gerekli Kütüphaneler

### requirements.txt
```
customtkinter>=5.2.0
anthropic>=0.18.0
pillow>=10.0.0
```

**Opsiyonel (Streamlit versiyonu için):**
```
streamlit>=1.31.0
```

## 🚀 Kurulum

### 1. Python Kurulumu
Python 3.8+ gereklidir. [Python İndir](https://www.python.org/downloads/)

### 2. Kütüphaneleri Yükle
```bash
pip install -r requirements.txt
```

veya tek tek:
```bash
pip install customtkinter anthropic pillow
```

**Streamlit versiyonu için ek:**
```bash
pip install streamlit
```

## 🎮 Kullanım

### Modern CustomTkinter Versiyonu (Masaüstü) - ÖNERİLEN
```bash
python main.py
```
✨ **Özellikler:**
- Ultra modern arayüz
- Dark/Light mode
- Animasyonlu butonlar
- Progress bar
- Tab view
- Demo mod (API key olmadan çalışır)

### Streamlit Versiyonu (Web Arayüzü)
```bash
streamlit run sinav_uretici_streamlit.py
```
Tarayıcınızda otomatik açılacaktır: `http://localhost:8501`

## 🔑 API Key Nasıl Alınır?

### Anthropic Claude API (Gerçek AI İçin)
1. [console.anthropic.com](https://console.anthropic.com/) adresine git
2. Hesap oluştur (ücretsiz $5 kredi)
3. API Keys bölümünden yeni key oluştur
4. Ortam değişkenine ekle

**Önemli:** API key'i kimseyle paylaşma!

### Ortam Değişkeni Kurulumu (Önerilen)
```bash
# Windows
set ANTHROPIC_API_KEY=your-api-key-here

# Mac/Linux
export ANTHROPIC_API_KEY=your-api-key-here
```

### Demo Mod (API Key Olmadan)
⚠️ Modern versiyonda **DEMO MODU** bulunur!
- API key olmadan çalışır
- Örnek sorular gösterir
- Tüm özellikleri test edebilirsiniz

## 📁 Proje Yapısı

```
ai-sinav-sorusu-uretici/
│
├── main.py                        # Modern CustomTkinter (Demo Mod)
├── requirements.txt               # Gerekli kütüphaneler
├── README.md                      # Bu dosya
├── sorular/                       # Oluşturulan sorular (otomatik)
└── ayarlar.json                   # Uygulama ayarları (otomatik)
```

## 🎯 Özellikler

### ✅ Modern CustomTkinter Versiyonu
- 🎨 **Ultra Modern Tasarım**: Gradient header, badge'ler, kartlar
- 🌙 **Dark/Light Mode**: Otomatik tema desteği
- ✨ **Animasyonlar**: Buton hover, progress bar, typing effect
- 📊 **3 Sekme**: Sorular, Cevaplar, İstatistikler
- 💾 **4 Buton**: Kaydet, Kopyala, Yazdır, Temizle
- 🔄 **Hızlı Eylemler**: Yeni set, örnek konular
- 📈 **Progress Bar**: Gerçek zamanlı ilerleme
- 🎯 **Demo Mod**: API key olmadan çalışır
- 🇹🇷 **Türkçe Karakter Desteği**: UTF-8 encoding
- 💾 **Otomatik Kayıt**: JSON ayarlar + TXT export
- 📊 **İstatistik Takibi**: Toplam üretilen, son konu vb.

### ✅ Genel Özellikler
- 10 farklı ders (Matematik, Fen, Türkçe, İngilizce, vb.)
- 5-12. sınıf arası destek
- 3 zorluk seviyesi (Kolay, Orta, Zor)
- 3 soru tipi (Çoktan Seçmeli, Açık Uçlu, Karışık)
- 3-15 arası soru sayısı (slider ile)
- Cevap anahtarı otomatik
- Dosya olarak indirme (TXT)
- Panoya kopyalama

### 🔮 Gelecek Özellikler (İsteğe Bağlı)
- [ ] PDF export (ReportLab)
- [ ] Gerçek AI entegrasyonu (Claude API)
- [ ] Veritabanı (SQLite)
- [ ] Öğrenci performans takibi
- [ ] Grafik/görsel içeren sorular
- [ ] Çoklu dil desteği

## 🛠️ Teknik Detaylar

### Kullanılan Teknolojiler
- **Python 3.8+**
- **CustomTkinter**: Modern GUI framework
- **Pillow**: Görsel işleme
- **Anthropic API**: Claude 4 AI (opsiyonel)
- **Threading**: Asenkron işlemler
- **JSON**: Ayar kaydetme

### CustomTkinter Avantajları
- ✨ Modern, flat design
- 🌙 Built-in dark mode
- 🎨 Özelleştirilebilir temalar
- 📱 Cross-platform (Windows, Mac, Linux)
- 🚀 Hızlı ve hafif

### API Kullanımı (Gerçek AI İçin)
Model: `claude-sonnet-4-20250514`
- Her soru üretimi ~1000-4000 token
- Ortalama süre: 3-10 saniye
- Demo mod: Anında (API gerektirmez)

## 📊 Proje Raporu İçin

### Problem
Öğretmenlerin özelleştirilmiş sınav soruları hazırlamak için harcadıkları zaman ve öğrencilerin konuya uygun soru bulmakta çektikleri zorluk.

### Çözüm
Modern masaüstü uygulama ile yapay zeka destekli otomatik soru üretimi sistemi:
- Saniyeler içinde soru oluşturma
- Sınıf seviyesine göre otomatik zorluk ayarı
- Türk eğitim müfredatına uygun içerik
- Öğretmenlere zaman kazandırma
- Öğrencilere sınırsız pratik imkanı
- Demo mod ile API key olmadan test

### Teknolojik Katkılar
- 🎨 Modern UI/UX tasarımı
- 🤖 AI entegrasyonu (opsiyonel)
- 💾 Otomatik dosya yönetimi
- 📊 İstatistik ve raporlama
- 🇹🇷 Tam Türkçe destek

### Katkılar
- ⏰ Zaman tasarrufu (manuel ~2 saat → AI ile ~1 dakika)
- 🎯 Kişiselleştirilmiş öğrenme
- 📚 Müfredata uygun içerik
- 🚀 Eğitimde AI farkındalığı
- 💻 Modern yazılım geliştirme

## 🐛 Hata Giderme

### "ModuleNotFoundError: No module named 'customtkinter'"
```bash
pip install customtkinter
```

### "ModuleNotFoundError: No module named 'anthropic'"
```bash
pip install anthropic
```

### CustomTkinter Tema Hatası
```bash
pip install --upgrade customtkinter
```

### API key not found (Gerçek AI için)
API key'inizi ortam değişkenine ekleyin veya Demo Mod'u kullanın.

### Streamlit açılmıyor
```bash
streamlit --version  # Kurulu olduğunu kontrol et
streamlit run sinav_uretici_streamlit.py --server.port 8502
```

### Windows'ta Türkçe Karakter Sorunu
UTF-8 encoding kullanılır, sorun olmamalı. Eğer sorun yaşarsanız:
```bash
chcp 65001  # Console encoding'i UTF-8 yap
```

### Linux'ta CustomTkinter Çalışmıyor
```bash
sudo apt-get install python3-tk
sudo apt-get install python3-pil python3-pil.imagetk
```

## 📝 Örnek Kullanım

### Girdi (Demo Mod)
```
Ders: Matematik
Sınıf: 7
Konu: Oran Orantı
Soru Sayısı: 5
Zorluk: Orta
Soru Tipi: Çoktan Seçmeli
```

### Çıktı (Demo)
```
╔══════════════════════════════════════════════════════════╗
║                    DEMO SORU KAĞIDI                       ║
╚══════════════════════════════════════════════════════════╝

SORU 1:
7. sınıf Matematik dersinde "Oran Orantı" konusuna ait örnek soru.
Zorluk seviyesi: Orta

A) Örnek şık A
B) Örnek şık B
C) Örnek şık C (Doğru Cevap)
D) Örnek şık D

✓ CEVAP: C - Bu demo için örnek cevaptır.
```

## 🎓 Proje Geliştirme Fikirleri

1. **PDF Export** ⭐
   - ReportLab ile PDF oluşturma
   - Profesyonel sınav formatı
   - Logo ve başlık ekleme

2. **Veritabanı Entegrasyonu**
   - SQLite ile soru havuzu
   - Geçmiş sorular ve performans
   - Favoriler sistemi

3. **Gerçek AI Entegrasyonu**
   - Claude API ile üretim
   - GPT-4 alternatifi
   - Özel prompt şablonları

4. **Kullanıcı Sistemi**
   - Öğretmen/Öğrenci rolleri
   - Sınıf yönetimi
   - Soru paylaşımı

5. **Mobil Uygulama**
   - Kivy ile cross-platform
   - Flutter alternatifi
   - React Native web view

6. **İleri Özellikler**
   - Görsel soru üretimi
   - QR kod ile paylaşım
   - Online quiz sistemi
   - Öğrenci cevaplarını değerlendirme

## 🎨 CustomTkinter Temaları

### Mevcut Temalar
- **blue** (Varsayılan - Mavi)
- **green** (Yeşil)
- **dark-blue** (Koyu Mavi)

### Tema Değiştirme
`sinav_uretici_modern.py` dosyasında:
```python
ctk.set_default_color_theme("blue")  # green veya dark-blue yapın
```

### Appearance Mode
- **dark** (Koyu - Varsayılan)
- **light** (Açık)
- **system** (Sistem ayarına göre)

## 📄 Lisans
Bu proje eğitim amaçlıdır ve MIT LICENSE ile korunmuştur.

## 🤝 Katkıda Bulunma
Bahar DEMİR - Mert İsa CANIMOĞLU

## 📧 İletişim
Sorularınız için: bahardemir270@gmail.com / mert.cnmoglu@gmail.com

---

**🎓 Yapay Zeka Destekli Eğitim**
**💻 Python • CustomTkinter • Claude 4**
**✨ Modern • Animasyonlu • Türkçe Destek

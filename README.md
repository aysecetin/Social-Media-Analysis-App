# ✨📊 NewMind - Sosyal Medya Görüş Analizi

NewMind, sosyal medya platformlarında yapılan yorumları analiz eden, sınıflandıran ve konu bazlı çıkarımlar yapan bir yapay zekâ destekli analiz sistemidir. Bu proje; argüman madenciliği, konu eşleştirmesi, özetleme ve görselleştirme süreçlerini entegre ederek güçlü bir analiz deneyimi sunmayı hedefler.

## 🎯 Projenin Amacı

1. **Konu Eşleştirmesi:** Yorumları önceden tanımlanmış konularla eşleştirmek.
2. **Yorum Sınıflandırması:** Yapay zekâ ile her yorumu Claim, Evidence, Counterclaim veya Rebuttal olarak etiketlemek.
3. **Konu Özeti Üretimi:** Girilen konuya dair tüm yorumlardan akıllı bir özet çıkarmak.
4. **Görsel Analiz:** Yorum türlerinin dağılımını grafikle sunmak.
5. **Gerçek Zamanlı Veri Güncelleme:** Yeni yorumları anında CSV dosyasına kaydetmek.



## 🗂️ Proje Yapısı

```bash
NewMind/
├── app.py                      # Ana uygulama dosyası (Gradio arayüzü)
├── requirements.txt            # Gerekli Python kütüphaneleri
├── README.md                   # Proje tanıtımı ve kullanım rehberi
├── data/
│   ├── opinions.csv            # Kullanıcı yorumlarının bulunduğu veri dosyası
│   ├── topics.csv              # Tanımlı konular
│   ├── conclusions.csv         # Oluşturulan özetler
│   └── classified_opinions.csv# Sınıflandırılmış yorumlar
├── assets/
│   ├── konu analizi.png        # Arayüz görseli
│   └── yorum ekle.png          # Arayüz görseli
```

---

## 🚀 Özellikler

### 🔍 Yorum Sınıflandırması

* Gelişmiş **BART-MNLI modeli** ile kullanıcı yorumları otomatik olarak **Claim, Evidence, Counterclaim veya Rebuttal** olarak etiketlenir.
* Akademik düzeyde argüman madenciliği, tek bir tıkla kullanımda!

### 🧠 Konu Eşleştirmesi (Semantic Matching)

* **SentenceTransformer** kullanılarak her yorum, en uygun konuyla eşleştirilir.
* Sıradan embedding’ler yerine yüksek doğruluk sağlayan cümle benzerliği yaklaşımı.

### ✨ Otomatik Özetleme

* **Flan-T5** modeli ile analiz edilen konu hakkında otomatik bir özet oluşturulur.
* Konu başlıklarına göre anlamlı, bağlamlı ve özlü metinler üretir.

### 📊 Grafik Gösterimi

* Matplotlib ile oluşturulan interaktif grafikler, yorum türlerinin dağılımını anında gösterir.
* Görsellik + içgörü bir arada!

### 💾 Gerçek Zamanlı CSV Güncelleme

* Kullanıcı tarafından girilen her yorum, otomatik olarak `user_comments.csv` dosyasına yazılır.
* Hem analiz yapılır hem de veri kalıcılığı sağlanır.



## 🌟 Kullanım Rehberi

### 1. Depoyu Klonla

```bash
git clone https://github.com/aysecetin/Social-Media-Analysis-App.git
cd Social-Media-Analyzer-App
```

### 2. Gerekli Paketleri Yükle

```bash
pip install -r requirements.txt
```

### 3. Uygulamayı Başlat

```bash
python app.py
```



## 🖼️ Arayüz Görselleri

### 1. Yorum Ekleme Paneli

![Yorum Ekle](assets/yorum-ekle.png)

### 2. Konu Analizi Paneli

![Konu Analizi](assets/konu-analizi.png)



## 📄 Lisans

Bu proje MIT Lisansı altında sunulmaktadır.

## 🤝 Katkı Sağlama

Projeye katkıda bulunmak için:

1. Fork'la.
2. Yeni bir branch oluştur: `git checkout -b feature/HarikaOzellik`
3. Commit yap: `git commit -m "Harika bir özellik eklendi"`
4. Pushla: `git push origin feature/HarikaOzellik`
5. Pull request gönder.



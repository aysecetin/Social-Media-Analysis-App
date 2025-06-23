# 🧠 Social Media Analyzer

Gradio tabanlı web uygulamasıyla sosyal medya yorumlarını analiz et, sınıflandır ve konu özetleri üret!

## 📂Klasör Yapısı

```
socialmedia_analyzer/
├── app.py
├── requirements.txt
├── README.md
├── assets/
│   ├── konu analizi.png
│   └── yorum ekle.png
├── data/
│   ├── classified_opinions.csv
│   ├── conclusions.csv
│   ├── opinions.csv
│   └── topics.csv
```

## 🚀 Özellikler

- **Yorum Sınıflandırması:** Claim, Evidence, Counterclaim, Rebuttal (BART-MNLI ile)
- **Konu Eşleştirmesi:** Yorumun en yakın konuyla eşleşmesi (SentenceTransformer)
- **Otomatik Özetleme:** Flan-T5 ile konu bazlı akıllı özet üretimi
- **Grafik Gösterimi:** Yorum türlerine göre dağılım grafiği (Matplotlib)
- **CSV Güncelleme:** Kullanıcı yorumları `user_comments.csv` dosyasına yazılır


## 🖥 Arayüz Ekranı

Uygulamanın arayüzü aşağıdaki bileşenleri içerir:

- Yorum Ekle sekmesi
- Konu Analizi sekmesi
- Otomatik konu özeti
- Yorum türü dağılım grafiği

Görseller için: `docs/` klasörüne göz atabilirsin.


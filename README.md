# 🧠 Social Media Analyzer

Gradio tabanlı web uygulamasıyla sosyal medya yorumlarını analiz et, sınıflandır ve konu özetleri üret!

## 📂Klasör Yapısı
```
socialmedia-analyzer/
├── app.py
├── requirements.txt
├── README.md
├── classified_opinions.csv
├── conclusions.csv
├── user_comments.csv
└── docs/
    └── screenshot.png
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


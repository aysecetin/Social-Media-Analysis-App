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

### 🔍 Yorum Sınıflandırması:
  Kullanıcı yorumları, gelişmiş BART-MNLI modeli ile otomatik olarak dört kategoriye ayrılır:
  Claim, Evidence, Counterclaim ve Rebuttal.
  Bu sayede argümantatif analizler akademik doğrulukla yapılabilir.

### 🧠 Konu Eşleştirmesi (Semantic Matching):
  Girilen her yorum, SentenceTransformer tabanlı bir embedding modeli ile analiz edilir ve en uygun konuyla eşleştirilir.
  Bu, basit anahtar kelime eşleşmesinin ötesinde, bağlamsal anlamı yakalayan semantik bir eşleştirmedir.


### ✨ Otomatik Özetleme:
  Yorumlara ait içerikler, kullanıcı odaklı Flan-T5 dil modeli ile özetlenir.
  Sonuç: İlgili konu başlığına dair kısa, anlamlı ve bağlama uygun otomatik bir özet.

### 📊 Grafik Gösterimi:
  Yorumların sınıflandırma sonuçları, Matplotlib ile kategorilere göre anlık olarak görselleştirilir.
  Kullanıcı dostu ve bilgilendirici grafikler ile analiz sonuçları kolayca yorumlanabilir.


### 💾 Gerçek Zamanlı CSV Güncelleme: 
  Kullanıcı tarafından girilen her yorum, user_comments.csv dosyasına otomatik olarak kaydedilir.
  Sistem, hem analiz yapar hem de sürekli güncellenen bir veri kümesi oluşturur.




## 🖥 Arayüz Ekranı

Uygulamanın arayüzü aşağıdaki bileşenleri içerir:

- Yorum Ekle sekmesi

![Yorum Ekle Ekranı](assets/yorum-ekle.png)
- Konu Analizi sekmesi

![Konu Analizi Ekranı](assets/konu-analizi.png)

- Otomatik konu özeti
- Yorum türü dağılım grafiği



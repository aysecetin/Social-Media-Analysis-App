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

- 🔍 **Yorum Sınıflandırması:**  
  Gelişmiş BART-MNLI modeliyle her yorumu otomatik olarak **Claim**, **Evidence**, **Counterclaim** veya **Rebuttal** olarak etiketler.  
  Akademik düzeyde argüman madenciliği, sadece bir tık uzağında!

- 🧠 **Konu Eşleştirmesi (Semantic Matching):**  
  Kullanıcının yorumunu, önceden tanımlı konularla yüksek doğrulukla eşleştirir.  
  Bunu da SentenceTransformer ile yapar — çünkü sıradan embedding’ler bize göre değil. 😌

- ✨ **Otomatik Özetleme:**  
  Flan-T5 modeliyle, kullanıcıların ilgilendiği konu hakkında anlamlı ve özlü bir **otomatik konu özeti** oluşturur.  
  Evet, kendi kendine yazıyor resmen!

- 📊 **Grafik Gösterimi:**  
  Yapay zekâ tarafından sınıflandırılan yorumların dağılımını **anında** görselleştir.  
  Şık, renkli ve bilgilendirici matplotlib grafikler ile insight'lar gözünün önünde.

- 💾 **Gerçek Zamanlı CSV Güncelleme:**  
  Girilen her yeni yorum, `user_comments.csv` dosyasına anlık olarak yazılır.  
  Yani sadece analiz değil, aynı zamanda veri kaydı da full otomatik!


## 🖥 Arayüz Ekranı

Uygulamanın arayüzü aşağıdaki bileşenleri içerir:

- Yorum Ekle sekmesi

![Yorum Ekle Ekranı](assets/yorum-ekle.png)
- Konu Analizi sekmesi

![Konu Analizi Ekranı](assets/konu-analizi.png)

- Otomatik konu özeti
- Yorum türü dağılım grafiği



# POS Tagging Test Uygulaması

Bu proje, Türkçe doğal dil işleme (NLP) kapsamında **Part-of-Speech (POS) Tagging** işlemini test etmek amacıyla geliştirilmiştir. Kullanıcıdan alınan cümlelerin morfolojik ve sözdizimsel analizini yaparak kelime türlerini belirlemektedir.

## 📌 Özellikler
- **Türkçe UD Treebank** veri kümesi kullanılarak POS etiketleme yapılmaktadır.
- **CoNLL-U formatı**ndaki veri dosyası işlenerek kelimelerin türleri ve morfolojik özellikleri analiz edilmektedir.
- Kullanıcıdan alınan cümledeki kelimelerin POS etiketleri ve diğer dilbilgisel özellikleri görüntülenmektedir.

## 🔍 Kullanım
Örnek bir kullanım aşağıdaki gibidir:

**Girdi:**
```
Güzel Bir Kitap
```
**Çıktı:**
```
Kelime: Güzel | Tür: ADJ
Kelime: Bir | Tür: DET
Kelime: Kitap | Tür: NOUN

```

## 🛠 Kod Açıklaması
- CoNLL-U formatındaki veri dosyasını okuyarak kelimeleri ve türlerini işler.
- **Fonksiyon Tanımlamaları:**
  - **Dosya İşleme:** Veri kümesini okuyarak kelimeleri ve morfolojik bilgileri küçük harfe çevirerek diziye ekler.
  - **Kullanıcı Girişi Analizi:** Kullanıcıdan alınan cümleyi parçalar ve kelimelerin türlerini belirler.
  - **Kontroller:** Boş satırlar ve geçersiz veriler işleme alınmaz.

## 📚 Kaynaklar
- [Turkish UD Treebank](https://nlp.itu.edu.tr/araclarkaynaklar)
- Türkçe BOUN UD Derlemi

## 📜 Lisans
Bu proje açık kaynak olarak paylaşılmaktadır. Katkıda bulunmak isterseniz lütfen bir **pull request** oluşturun!


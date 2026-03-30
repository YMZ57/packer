# 📌 Packer Bypass & Manual Unpacking Projesi

## 🎯 Proje Amacı
Bu projenin amacı, UPX ve ASPack gibi packer’lar ile paketlenmiş PE (Portable Executable) dosyalarının manuel olarak analiz edilmesi ve gerçek (orijinal) kodun ortaya çıkarılmasıdır.

Çalışma kapsamında:
- Runtime sırasında açılan kodun analiz edilmesi
- Original Entry Point (OEP) tespiti
- Bellekten dump alınması
- Import Address Table (IAT) yeniden oluşturulması

hedeflenmektedir.

---

## 🧠 Temel Kavramlar

Bu projede aşağıdaki teknik kavramlar kullanılacaktır:

- PE (Portable Executable) yapısı
- Packer ve runtime unpacking mantığı
- Entry Point (EP) ve Original Entry Point (OEP)
- Memory dumping
- Import Address Table (IAT)
- Debugger kullanımı

---

## 🧰 Kullanılacak Araçlar

- x64dbg → Debugging ve breakpoint yönetimi
- PE-bear → PE header analizi
- Scylla → IAT rebuild işlemleri
- Detect It Easy (DIE) → Packer tespiti
- UPX → Test amaçlı paketleme

---

## 🗺️ Teknik Yol Haritası

### 1. 🔍 Packer Tespiti
- Hedef dosya analiz edilir
- Detect It Easy kullanılarak packer türü belirlenir
- Section yapısı incelenir

**Beklenen çıktı:**
- Dosyanın hangi packer ile paketlendiğinin tespiti

---

### 2. ⚙️ Statik Analiz
- PE header incelenir
- Entry Point adresi belirlenir
- Section entropy kontrol edilir

**Beklenen çıktı:**
- Packed yapı doğrulanır

---

### 3. 🐞 Debugging Başlatma
- Dosya x64dbg ile açılır
- Entry Point’e breakpoint konur
- Step-by-step execution yapılır

**Amaç:**
- Runtime unpacking sürecini gözlemlemek

---

### 4. 🎯 OEP (Original Entry Point) Tespiti

OEP tespiti için:
- JMP ve CALL akışı takip edilir
- PUSHAD / POPAD pattern analiz edilir
- Kodun normal programa döndüğü an yakalanır

**Beklenen çıktı:**
- Gerçek program başlangıç noktası (OEP)

---

### 5. 💾 Memory Dump Alma
- OEP’e ulaşıldığında:
  - Process memory dump edilir
  - Dump edilen veri dosya olarak kaydedilir

**Amaç:**
- Gerçek executable elde etmek

---

### 6. 🔧 Import Table (IAT) Rebuild
- Dump edilen dosyada importlar eksik olur
- Scylla ile:
  - IAT taranır
  - Eksik importlar yeniden oluşturulur

**Beklenen çıktı:**
- Çalıştırılabilir düzgün PE dosyası

---

### 7. 🧪 Doğrulama (Validation)
- Dump edilen dosya çalıştırılır
- Orijinal dosya ile davranış karşılaştırılır

**Amaç:**
- Unpacking işleminin doğrulanması

---

## 📊 Beklenen Çıktılar

- Paketlenmiş ve unpack edilmiş dosya karşılaştırması
- OEP adresi
- Dump edilmiş çalışır binary
- IAT fix edilmiş final executable

---

## ⚠️ Zorluklar

- Anti-debug teknikleri
- Obfuscation
- Yanlış OEP tespiti
- Self-modifying code

---

## 🚀 Gelişmiş Çalışmalar (Opsiyonel)

- Otomatik unpack script geliştirme
- Farklı packer analizleri (Themida, VMProtect)
- Anti-debug bypass teknikleri

---

## 📌 Sonuç

Bu proje, manuel unpacking sürecini pratik olarak uygulamayı hedeflemektedir. Reverse engineering alanında önemli bir deneyim kazandırır.

---

## 🔥 Kısa Özet

Bu çalışmada, UPX ve ASPack ile paketlenmiş PE dosyalarının runtime analiz ile OEP tespiti yapılarak bellekten dump edilmesi ve IAT rebuild işlemleri ile tekrar çalıştırılabilir hale getirilmesi amaçlanmaktadır.
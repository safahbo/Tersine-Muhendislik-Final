# ROADMAP — Static String Extractor & Classifier
# ROADMAP — Statik String Çıkarıcı ve Sınıflandırıcı

> Course / Ders: Reverse Engineering (BGT210) · Istinye University
> Instructor / Danışman: Keyvan Arasteh

---

## Phase 0 / Faz 0: Understand Before You Build / Yazmadan Önce Anla

Tek satır kod yazmadan önce şu soruları yanıtladım:

- What is the project? / Proje nedir? -> Binary dosyalarındaki gömülü metinleri çıkaran bir araç.
- How does it work? / Nasıl çalışır? -> Dosyayı byte düzeyinde okur, regex ile anlamlı dizeleri bulur ve sınıflandırır.
- What are the inputs/outputs? / Girdiler/çıktılar neler? -> Girdi: Binary dosya. Çıktı: Sınıflandırılmış JSON raporu.
- What tools will I use and why? / Hangi araçları kullanacağım ve neden? -> Dış bağımlılık olmadan saf Python ve `re` kütüphanesi.

---

## Phase 1 / Faz 1: Research & Investigation / Araştırma ve Keşif

> Folder / Klasör: `docs/research/`

| Topic / Konu | Status / Durum | Notes / Notlar |
|--------------|----------------|----------------|
| Regex Pattern'leri | ✅ Tamamlandı | IP, URL ve Email tespiti için patternler belirlendi. |
| Byte/String Çevrimi | ✅ Tamamlandı | Binary veriyi decode etme test edildi. |
| JSON Raporlama | ✅ Tamamlandı | Çıktıların düzenlenmesi sağlandı. |

---

## Phase 2 / Faz 2: Environment Setup / Ortam Kurulumu

- [x] Isolated lab environment (Docker / VM) / İzole lab ortamı
- [x] Tools installed and verified / Araçlar kuruldu ve test edildi
- [x] `.env.example` created / oluşturuldu

---

## Phase 3 / Faz 3: Implementation / Uygulama

### Module / Modül: Core Extractor

1. Step 1 / Adım 1 — Binary dosyanın okunması
2. Step 2 / Adım 2 — Regex filtrelerinin uygulanması
3. Step 3 / Adım 3 — JSON çıktısının üretilmesi

---

## Phase 4 / Faz 4: Testing & Reporting / Test ve Raporlama

- [x] Ran tests against target/sample / Hedef/örnek üzerinde testler çalıştırıldı
- [x] Documented all findings with evidence / Tüm bulgular kanıtlarıyla belgelendi
- [x] Wrote final report (Markdown) / Final raporu yazıldı

---

## Phase 5 / Faz 5: Delivery / Teslim

- [x] GitHub repository is clean and organized / Repo temiz ve düzenli
- [x] README.md complete / eksiksiz
- [x] Docker verified (`docker-compose up`) / doğrulandı
- [x] Instructor invited as collaborator / Danışman collaborator olarak eklendi → **keyvanarasteh**

---

## What I Learned / Öğrendiklerim

Regex yazarken false-positive'leri (yanlış pozitifleri) engellemenin ne kadar zor olduğunu gördüm. Özellikle Base64 pattern'leri rastgele byte dizileriyle çok sık karışabiliyor, bu yüzden uzunluk limiti eklemek zorunda kaldım.

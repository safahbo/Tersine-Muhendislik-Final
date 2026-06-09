# Static String Extractor & Classifier

<div align="center">
  <a href="https://istinye.edu.tr">
    <img src="docs/assets/istinye-university-logo.webp" alt="Istinye University" width="180"/>
  </a>

  <h1>Static String Extractor & Classifier</h1>

  <img src="https://img.shields.io/badge/GitHub-Private-red?style=flat-square&logo=github" alt="GitHub">
  <img src="https://img.shields.io/badge/Language-Python-blue?style=flat-square" alt="Language">
  <img src="https://img.shields.io/badge/Status-In%20Progress-yellow?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Course-BGT210-purple?style=flat-square" alt="Course">
  <img src="https://img.shields.io/badge/License-Educational-green?style=flat-square" alt="License">
</div>

---

# 🎓 Instructor / Danışman

| Field         | Information                                                           |
| ------------- | --------------------------------------------------------------------- |
| **Name / Ad** | Keyvan Arasteh                                                        |
| **GitHub**    | @keyvanarasteh                                                        |
| **Email**     | [keyvan.arasteh@istinye.edu.tr](mailto:keyvan.arasteh@istinye.edu.tr) |
| **LinkedIn**  | keyvanarasteh                                                         |
| **Website**   | qline.tech                                                            |

---

# 👤 Student / Öğrenci

| Field                       | Information         |
| --------------------------- | ------------------- |
| **Name / Ad Soyad**         | Safa Hacıbayramoğlu |
| **Student ID / Öğrenci No** | `2420191014`        |

---

# 📚 Course Information / Ders Bilgileri

| Field                        | Information                               |
| ---------------------------- | ----------------------------------------- |
| **Course Name / Ders Adı**   | Reverse Engineering / Tersine Mühendislik |
| **Course Code / Ders Kodu**  | BGT210                                    |
| **Credits / Kredi**          | 3 ECTS                                    |
| **Semester / Dönem**         | 2025-2026 Spring / 2025-2026 Bahar        |
| **Institution / Üniversite** | Istinye University                        |

---

# 📋 Project Overview / Proje Özeti

Bu proje, verilen herhangi bir binary dosyasından (APK, EXE, ELF vb.) statik olarak string ifadeleri çıkaran ve bunları düzenli ifadeler (regex) kullanarak aşağıdaki kategorilere ayıran bir CLI aracıdır:

* URL
* IP Address
* E-mail Address
* Base64 Encoded Data

Araç ayrıca yüksek riskli verileri otomatik olarak tespit ederek JSON formatında rapor üretir.

---

# 🗂 Repository Structure / Repo Yapısı

```text
.
├── README.md
├── ROADMAP.md
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── .gitignore
├── docs/
│   ├── modules/
│   ├── research/
│   └── references/
└── src/
    └── main.py
```

---

# 🚀 Getting Started / Kurulum

## Clone Repository

```bash
git clone https://github.com/safahbo/Tersine-Muhendislik-Final.git
cd Tersine-Muhendislik-Final
```

## Run Analysis

```bash
python src/main.py \
  -f <analiz_edilecek_dosya> \
  -o reports/output.json
```

Örnek:

```bash
python src/main.py \
  -f sample.exe \
  -o reports/result.json
```

---

# 📊 Deliverables / Teslimler

| Deliverable                     | Status |
| ------------------------------- | ------ |
| CLI Aracının Geliştirilmesi     | ✅      |
| Regex Sınıflandırma Mantığı     | ✅      |
| Rapor Çıktısı (JSON Formatında) | ✅      |

---

# 📚 Documentation / Belgeleme

* Module Documentation → `docs/modules/`
* Research Notes → `docs/research/`
* References → `docs/references/`

---

# 🔗 References / Kaynaklar

* Python Regular Expressions Documentation
* OWASP Reverse Engineering Resources
* Python `re` Module Documentation
* Binary Analysis Fundamentals
* Static Malware Analysis Techniques

---

# ⚠️ Educational Notice

Bu proje yalnızca eğitim ve akademik amaçlarla geliştirilmiştir. Analiz edilen dosyaların yasal kullanımından kullanıcı sorumludur.


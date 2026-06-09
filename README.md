<div align="center">
  <a href="https://istinye.edu.tr">
    <img src="docs/assets/istinye-university-logo.webp" alt="Istinye University" width="180"/>
  </a>

# Advanced Binary String Extraction & Heuristic Analysis Engine

![GitHub](https://img.shields.io/badge/GitHub-Private-red?style=flat-square\&logo=github)
![Language](https://img.shields.io/badge/Language-Python-blue?style=flat-square)
![Status](https://img.shields.io/badge/Status-Completed-success?style=flat-square)
![Course](https://img.shields.io/badge/Course-BGT210-purple?style=flat-square)
![License](https://img.shields.io/badge/License-Educational-green?style=flat-square)

</div>

---

# 🎓 Instructor / Danışman

| Field         | Information                                                           |
| ------------- | --------------------------------------------------------------------- |
| **Name / Ad** | Keyvan Arasteh                                                        |
| **GitHub**    | [@keyvanarasteh](https://github.com/keyvanarasteh)                    |
| **Email**     | [keyvan.arasteh@istinye.edu.tr](mailto:keyvan.arasteh@istinye.edu.tr) |
| **LinkedIn**  | [keyvanarasteh](https://www.linkedin.com/in/keyvanarasteh/)           |
| **Website**   | https://qline.tech                                                    |

---

# 👤 Student / Öğrenci

| Field                       | Information         |
| --------------------------- | ------------------- |
| **Name / Ad Soyad**         | Safa Hacıbayramoğlu |
| **Student ID / Öğrenci No** | `2420191014`        |

---

# 📚 Course Information / Ders Bilgileri

| Field                        | Information                                  |
| ---------------------------- | -------------------------------------------- |
| **Course Name / Ders Adı**   | Reverse Engineering / Tersine Mühendislik    |
| **Course Code / Ders Kodu**  | BGT210                                       |
| **Credits / Kredi**          | 3 ECTS                                       |
| **Semester / Dönem**         | 2025–2026 Spring / 2025–2026 Bahar           |
| **Institution / Üniversite** | [Istinye University](https://istinye.edu.tr) |

---

# 📋 Project Overview / Proje Özeti

Bu proje, derlenmiş binary dosyalarını (**APK, ELF, PE, DEX**) doğrudan bellek haritalama (**mmap**) yöntemiyle analiz eden gelişmiş bir statik analiz motorudur.

Sistem, klasik regex tabanlı string çıkarımının ötesine geçerek:

* Shannon Entropisi hesaplaması gerçekleştirir.
* Kriptografik anahtarları ve API token'larını sezgisel (heuristic) yöntemlerle tespit eder.
* Şüpheli API çağrılarını analiz eder.
* ASCII ve UTF-16LE formatındaki stringleri ayıklayabilir.
* Binary dosya yapıları üzerinde düşük seviyeli inceleme yapabilir.

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
│   │   └── heuristic-engine.md
│   ├── research/
│   │   └── research-notes.md
│   └── references/
├── reports/
│   └── final-report.md
└── src/
    └── main.py
```

---

# 🚀 Getting Started / Kurulum

```bash
git clone https://github.com/safahbo/Tersine-Muhendislik-Final.git

cd Tersine-Muhendislik-Final

python src/main.py \
    -f <analiz_edilecek_binary> \
    -o reports/analysis.json
```

---

# 📊 Deliverables / Teslimler

| Feature                                           | Status |
| ------------------------------------------------- | ------ |
| Magic Byte Tabanlı Dosya Tespiti                  | ✅      |
| mmap ile Düşük Seviye Bellek Yönetimi             | ✅      |
| Shannon Entropisi ile Sezgisel Analiz (Heuristic) | ✅      |
| Şüpheli API Çağrısı Tespiti                       | ✅      |

---

# 📚 Documentation / Belgeleme

| Documentation        | Location                  |
| -------------------- | ------------------------- |
| Module Documentation | `docs/modules/`           |
| Research Notes       | `docs/research/`          |
| References           | `docs/references/`        |
| Final Report         | `reports/final-report.md` |

---

# 🔬 Technical Capabilities

* Binary string extraction
* UTF-16LE string recovery
* Entropy-based secret detection
* API endpoint identification
* Magic byte file classification
* Memory-mapped file analysis (`mmap`)
* Static reverse engineering support

---

# ⚠️ Educational Purpose

Bu proje yalnızca eğitim ve akademik araştırma amacıyla geliştirilmiştir. Elde edilen sonuçların güvenlik testleri veya adli analiz süreçlerinde kullanılması durumunda ek doğrulama mekanizmaları uygulanmalıdır.

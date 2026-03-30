# 🛡️ Advanced PDF Protector & Integrity Vault

Ek professional Command-Line Interface (CLI) tool jo aapki PDFs aur Images ko high-level encryption (AES-128) ke saath secure karta hai aur unki integrity (SHA-256) verify karta hai.

## ✨ Features
- **Multi-Format Support:** Direct PDF ya Images (.jpg, .png, .jpeg) ko secure PDF mein convert aur lock karein.
- **Strong Password Policy:** Base-level security ke liye 8+ characters, numbers aur symbols ka hona zaroori hai.
- **Integrity Verification:** Har secured file ka ek unique SHA-256 hash generate hota hai taaki file tamper-proof rahe.
- **Smart CLI Flags:** `-o` flag se custom output name dein, varna ye automatically `output/` folder bana kar file save kar dega.
- **Timestamping:** Har transaction ka exact time record hota hai.

## 📁 Project Structure
```text
PDF_Protector/
├── pdf_protector.py       # Main Logic & CLI Interface
├── requirements.txt       # Dependencies (PyPDF2, img2pdf)
└── README.md              # Project Documentation
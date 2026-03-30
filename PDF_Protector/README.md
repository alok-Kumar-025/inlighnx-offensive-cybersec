# 🛡️ Advanced PDF Protector & Integrity Vault

🛡️ PDF Security Vault & Integrity Tool (v2.0)
A professional Command-Line Interface (CLI) tool designed to secure your documents using AES-128 encryption and verify file integrity with SHA-256 hashing.

✨ Key Features
Multi-Format Support: Seamlessly convert and lock both PDF documents and images (.jpg, .png, .jpeg) into a single secured PDF.

Robust Password Policy: Enforces high-level security requiring a minimum of 8+ characters, including numbers and special symbols.

Integrity Verification: Generates a unique SHA-256 digital fingerprint for every secured file to ensure it remains tamper-proof.

Smart CLI Flags: Supports the -o flag for custom output naming; otherwise, it automatically organizes files into an output/ directory.

Audit Logging: Every operation is recorded with an exact timestamp for forensic tracking.

## 📁 Project Structure
```text
PDF_Protector/
├── pdf_protector.py       # Main Logic & CLI Interface
├── requirements.txt       # Dependencies (PyPDF2, img2pdf)
└── README.md              # Project Documentation

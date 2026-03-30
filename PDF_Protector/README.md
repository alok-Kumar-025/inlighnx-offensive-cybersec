# 𝓟𝓓𝓕 𝓟𝓡𝓞𝓣𝓔𝓒𝓣𝓞𝓡 v2.0
> **Advanced PDF Security Vault & Integrity Verification Tool**

A professional Command-Line Interface (CLI) tool designed to secure your documents using **AES-128 encryption** and verify file integrity with **SHA-256 hashing**. Developed as part of the Offensive Cybersecurity Internship at InLighnX Global.

---

## ✨ Key Features

* **🛡️ High-Level Encryption:** Uses AES-128 bit encryption to password-protect sensitive documents.
* **🖼️ Multi-Format Support:** Convert and secure images (`.jpg`, `.png`, `.jpeg`) or existing PDFs seamlessly.
* **🔑 Integrity Verification:** Generates a unique **SHA-256 Digital Fingerprint** for every secured file to ensure it remains tamper-proof.
* **⚙️ Smart CLI Flags:** Support for `-o` (custom output) and `-p` (direct password) for automated workflows.
* **📂 Auto-Directory Management:** Automatically creates an `output/` folder if no custom path is specified.
* **⏰ Audit Logging:** Every operation is recorded with an exact timestamp for forensic tracking.

---

## 🚀 Getting Started (Installation)

Follow these steps to set up the tool on your local machine:

### 1. Prerequisites
Ensure you have **Python 3.8+** installed. Check your version:
```bash
python --version
```
2. Clone & Setup

# Clone the repository
git clone [https://github.com/alok-Kumar-025/inlighnx-offensive-cybersec.git](https://github.com/alok-Kumar-025/inlighnx-offensive-cybersec.git)

# Navigate to the project directory
cd inlighnx-offensive-cybersec/PDF_Protector

# Install required dependencies
pip install -r requirements.txt


🛠️ Usage & CLI Flags

The tool is designed to be used directly from the terminal.

Basic Command Structure:
python pdf_protector.py [input_file] [flags]


Flag,Full Form,Description
-h,--help,Show professional help menu and examples.
-o,--output,Specify a custom name for the secured file.
-p,--password,"Set a password via CLI (Enforces 8+ chars, 1 Num, 1 Symbol)."


Practical Examples:
1. Default Protection (Saves to 'output/' folder):
```bash
python pdf_protector.py my_resume.pdf
```
2. Convert Image to Secured PDF with Custom Name:
```bash
python pdf_protector.py ID_card.jpg -o secure_vault.pdf
```
3. Full Automation (Password provided via flag):
```bash
python pdf_protector.py data_report.pdf -p Secure@2026!
```
**🛡️ Security Architecture**

**Input Parsing:** Validates file existence and extension via argparse.

**Conversion:** Converts image buffers to PDF using img2pdf without losing quality.

**Encryption:** Applies AES-128 encryption layers using PyPDF2.

**Hashing:** Implements a post-processing SHA-256 check for forensic integrity.

Author

**Alok Kumar** Cybersecurity Practitioner & MScIS Student

**Disclaimer: This tool is intended for educational and professional security use cases. Ensure you follow organizational policies when handling sensitive data**.

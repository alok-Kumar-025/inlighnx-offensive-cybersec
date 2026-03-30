import PyPDF2
import img2pdf
import os
import hashlib
import argparse
import re
from datetime import datetime

# --- Logic: Integrity Hash ---
def get_file_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# --- Logic: Password Strength ---
def is_strong_password(password):
    if len(password) < 8: return False
    if not re.search("[0-9]", password): return False
    if not re.search("[_@$!%*#?&]", password): return False
    return True

# --- Professional Banner ---
def show_banner():
    # 'r' prefix zaroori hai (Raw String) taaki backslashes error na dein
    banner = r"""
            
██████╗░██████╗░███████╗  ██████╗░██████╗░░█████╗░████████╗███████╗░█████╗░████████╗░█████╗░██████╗░
██╔══██╗██╔══██╗██╔════╝  ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██████╔╝██║░░██║█████╗░░  ██████╔╝██████╔╝██║░░██║░░░██║░░░█████╗░░██║░░╚═╝░░░██║░░░██║░░██║██████╔╝
██╔═══╝░██║░░██║██╔══╝░░  ██╔═══╝░██╔══██╗██║░░██║░░░██║░░░██╔══╝░░██║░░██╗░░░██║░░░██║░░██║██╔══██╗
██║░░░░░██████╔╝██║░░░░░  ██║░░░░░██║░░██║╚█████╔╝░░░██║░░░███████╗╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║
╚═╝░░░░░╚═════╝░╚═╝░░░░░  ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚══════╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝

                                                                            Author  : Alok Kumar
                                                                            Version : 2.0 
--------------------------------------------------------------------------------------------------------------------
    [*] SECURITY POLICY: Password must be 8+ chars with at least 1 Number and 1 Symbol.
    """
    print(banner)

def run_protector():
    show_banner() # Starting mein hi banner dikhega

    parser = argparse.ArgumentParser(
        description="🛡️ PDF Protector CLI: Secure your documents with AES-128 & SHA-256.",
        epilog="Examples:\n  python pdf_protector.py doc.pdf\n  python pdf_protector.py image.jpg -o secure.pdf",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("input", help="Path to the input file (PDF/JPG/PNG)")
    parser.add_argument("-o", "--output", help="Custom output filename")
    parser.add_argument("-p", "--password", help="Set password via CLI")
    
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"[-] Error: '{args.input}' not found.")
        return

    # Password Logic with Strength Check
    password = args.password
    if not password or not is_strong_password(password):
        if password: print("[-] Warning: Provided password is weak!")
        while True:
            password = input("[?] Set Strong Password: ")
            if is_strong_password(password): break
            print("[-] Error: Password must be 8+ chars with 1 Number and 1 Symbol.")

    # Output Logic
    if args.output:
        final_output = args.output
    else:
        if not os.path.exists("output"):
            os.makedirs("output")
        final_output = os.path.join("output", "SECURED_" + os.path.basename(args.input))
        if not final_output.lower().endswith(".pdf"): final_output += ".pdf"

    try:
        working_file = args.input
        if args.input.lower().endswith(('.png', '.jpg', '.jpeg')):
            print("[+] Converting image to PDF...")
            with open("temp.pdf", "wb") as f:
                f.write(img2pdf.convert(args.input))
            working_file = "temp.pdf"

        reader = PyPDF2.PdfReader(working_file)
        writer = PyPDF2.PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        
        writer.encrypt(user_password=password, use_128bit=True)

        with open(final_output, "wb") as f:
            writer.write(f)

        print("\n" + "-"*40)
        print(f"✅ STATUS      : SUCCESS")
        print(f"🔒 FILE        : {final_output}")
        print(f"🔑 SHA-256 HASH: {get_file_hash(final_output)}")
        print(f"⏰ TIMESTAMP   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-"*40)

        if os.path.exists("temp.pdf"): os.remove("temp.pdf")

    except Exception as e:
        print(f"[-] Critical Error: {e}")

if __name__ == "__main__":
    run_protector()
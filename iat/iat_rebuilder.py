import subprocess
import os

# 🔥 SENİN MAKİNEYE GÖRE DOĞRU PATH
SCYLLA_PATH = r"C:\Users\ahmet\Downloads\Scylla_v0.9.8\Scylla_x64.exe"


def rebuild_iat(dump_file):
    print("[*] Starting IAT rebuild...")

    # 📁 Dump dosyası kontrol
    if not os.path.exists(dump_file):
        print(f"[!] Dump file not found: {dump_file}")
        return

    # 📁 Scylla kontrol
    if not os.path.exists(SCYLLA_PATH):
        print(f"[!] Scylla not found at: {SCYLLA_PATH}")
        print("[!] Check path!")
        return

    try:
        print("[*] Launching Scylla...")

        # 🚀 Scylla çalıştır
        subprocess.Popen(SCYLLA_PATH)

        print("\n[+] Scylla launched successfully")
        print("[!] NOW DO THIS:")
        print("    1. Click 'Attach'")
        print("    2. Select your process (packed.exe)")
        print("    3. Click 'IAT Autosearch'")
        print("    4. Click 'Get Imports'")
        print("    5. Click 'Fix Dump'")
        print("    6. Save as final.exe\n")

    except Exception as e:
        print(f"[!] Error launching Scylla: {e}")
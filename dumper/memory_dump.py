import shutil
import os
import subprocess


# 🔹 1) BASİT (SIMULATION)
def simulate_dump(input_file, output_file="dumped.exe"):
    """
    Gerçek memory dump yerine simülasyon (dosya kopyalama)
    """
    if not os.path.exists(input_file):
        print("[!] File not found")
        return None

    shutil.copy(input_file, output_file)
    print(f"[+] Dump created (simulated): {output_file}")

    return output_file


# 🔥 2) GERÇEK (x64dbg ÜZERİNDEN)
def real_dump_with_x64dbg(target_file):
    """
    x64dbg ile gerçek memory dump yönlendirmesi
    """

    # 🔥 SENİN DOĞRU PATH (fixlenmiş)
    X64DBG_PATH = r"C:\Users\ahmet\Downloads\snapshot_2025-08-19_19-40\release\x64\x64dbg.exe"

    print("[*] Starting REAL dump process...")

    # 📁 x64dbg kontrol
    if not os.path.exists(X64DBG_PATH):
        print(f"[!] x64dbg not found at: {X64DBG_PATH}")
        return None

    # 📁 target kontrol
    if not os.path.exists(target_file):
        print(f"[!] Target file not found: {target_file}")
        return None

    try:
        # 🚀 x64dbg ile aç
        subprocess.Popen([X64DBG_PATH, target_file])

        print("\n[+] x64dbg launched successfully")
        print("[!] FOLLOW THESE STEPS:")
        print("    1. Press F9 (run)")
        print("    2. Reach OEP")
        print("    3. Open Memory Map")
        print("    4. Right click code section → Dump memory to file")
        print("    5. Save as dumped_real.exe\n")

        return "dumped_real.exe"

    except Exception as e:
        print(f"[!] Error launching x64dbg: {e}")
        return None
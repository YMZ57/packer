import sys
from core.analyzer import analyze_pe
from debugger.oep_finder import find_oep
from dumper.memory_dump import real_dump_with_x64dbg
from iat.iat_rebuilder import rebuild_iat


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <file>")
        return

    file = sys.argv[1]

    try:
        # 🔍 PE ANALİZ
        result = analyze_pe(file)

        print(f"[+] File: {file}")
        print(f"[+] Entry Point: {result['entry_point']}")
        print(f"[+] Packer: {result['packer']}")
        print(f"[+] Risk: {result['risk']}")

        print("\n[+] Sections:")
        for sec in result["sections"]:
            print(f" - {sec['name']} | Entropy: {sec['entropy']:.2f}")

        # 🔥 OEP HESAPLAMA (statik)
        oep = find_oep(file)
        print(f"\n[+] Calculated OEP: {oep}")

        # 🔥 GERÇEK OEP GİRİŞİ
        real_oep = input("[?] Enter REAL OEP from debugger (hex): ")
        print(f"[+] REAL OEP (debugger): {real_oep}")

        # 💾 REAL DUMP (x64dbg ile)
        dumped_file = real_dump_with_x64dbg(file)

        if dumped_file:
            print(f"[+] Dump ready (expected): {dumped_file}")

            # 🔧 IAT REBUILD (SCYLLA)
            rebuild_iat(dumped_file)

    except Exception as e:
        print(f"[!] Error: {e}")


if __name__ == "__main__":
    main()
import pefile
import math

def calculate_entropy(data):
    if not data:
        return 0

    entropy = 0
    for x in range(256):
        p_x = data.count(bytes([x])) / len(data)
        if p_x > 0:
            entropy -= p_x * math.log2(p_x)

    return entropy


def detect_packer(pe):
    for section in pe.sections:
        name = section.Name.decode(errors="ignore").strip('\x00')

        if "UPX" in name:
            return "UPX"

        if "ASPack" in name:
            return "ASPack"

    return None


def analyze_pe(file_path):
    pe = pefile.PE(file_path)

    result = {
        "entry_point": hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint),
        "sections": [],
        "packer": None,
        "risk": "LOW"
    }

    suspicious_text = False
    unknown_high_entropy = False

    known_sections = [".text", ".rdata", ".data", ".rsrc", ".reloc", ".pdata"]

    for section in pe.sections:
        name = section.Name.decode(errors="ignore").strip('\x00')
        entropy = calculate_entropy(section.get_data())

        result["sections"].append({
            "name": name,
            "entropy": entropy
        })

        # ?? kritik kontrol
        if name == ".text" and entropy > 6.5:
            suspicious_text = True

        if name not in known_sections and entropy > 6.5:
            unknown_high_entropy = True

    packer = detect_packer(pe)
    result["packer"] = packer

    # ?? yeni risk logic
    if packer:
        result["risk"] = "HIGH"
    elif suspicious_text:
        result["risk"] = "HIGH"
    elif unknown_high_entropy:
        result["risk"] = "MEDIUM"
    else:
        result["risk"] = "LOW"

    return result

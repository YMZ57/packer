import pefile

def find_oep(file_path):
    pe = pefile.PE(file_path)

    ep = pe.OPTIONAL_HEADER.AddressOfEntryPoint
    image_base = pe.OPTIONAL_HEADER.ImageBase

    oep = image_base + ep

    return hex(oep)
 

def manual_oep_input():
    oep = input("[?] Enter REAL OEP from debugger (hex): ")
    return oep
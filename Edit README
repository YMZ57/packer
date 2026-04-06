# 🔥 Packer Unwrapper Framework

A manual reverse engineering project for analyzing and unpacking PE (Portable Executable) files packed with packers such as UPX.

---

## 🎯 Project Purpose

This project demonstrates how packed executables can be analyzed and restored to their original state using manual reverse engineering techniques.

### Main Goals

- Detect packers (UPX, ASPack)
- Analyze PE structure
- Identify Original Entry Point (OEP)
- Dump process memory
- Rebuild Import Address Table (IAT)
- Restore executable functionality

---

## 🧠 Concepts Covered

- PE File Structure
- Runtime Unpacking
- Entry Point vs OEP
- Memory Dumping
- IAT Reconstruction
- Debugging Techniques

---

## 🧰 Tools Used

- x64dbg → Debugging & execution tracing  
- PE-bear → PE header analysis  
- Scylla → IAT rebuilding  
- Detect It Easy (DIE) → Packer detection  
- UPX → Test packer  

---

## 🏗️ Project Structure


core/ → PE analysis & entropy
debugger/ → OEP detection logic
dumper/ → Dump simulation & debugger integration
iat/ → IAT rebuild (Scylla)
utils/ → Logging utilities
main.py → Main execution pipeline


---

## ⚙️ How It Works

### 1. Packer Detection
Detects if the file is packed and identifies packer type (UPX).

### 2. Static Analysis
- Extracts Entry Point  
- Calculates entropy  
- Confirms packed structure  

### 3. Debugging Phase
- Launches x64dbg  
- User steps through execution  

### 4. OEP Detection
- Calculates estimated OEP  
- User confirms real OEP  

### 5. Memory Dump
- Manual debugger-assisted dump  
- Extracts unpacked binary  

### 6. IAT Rebuild
- Uses Scylla manually  
- Restores imports  

---

## 🚀 Quick Start

```bash
git clone https://github.com/YMZ57/packer.git
cd packer
pip install -r requirements.txt
python main.py samples/packed.exe
⚠️ Requirements
Python 3.x
x64dbg
Scylla
PE-bear (optional)
Detect It Easy (optional)
🧠 Design Decisions

This project uses a modular architecture to separate static and dynamic analysis.

Each module is responsible for a specific stage of the unpacking pipeline.

🔐 Security Implications

Packed executables can hide malicious payloads.

Manual unpacking helps reveal:

hidden runtime behavior
obfuscated code
malware logic
🚀 Future Work
Automatic OEP detection
Memory dumping via Windows API
Anti-debug bypass techniques
Advanced packer support (Themida, VMProtect)
📊 Output
Detected packer type
Entry Point & OEP
Dumped executable
Rebuilt working binary
📌 Conclusion

This project demonstrates a real-world manual unpacking workflow used in reverse engineering and malware analysis.

👨‍💻 Author

YMZ57

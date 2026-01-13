# TryHackMe – Wormhole Automation Scripting 🌀

A **Python-based security automation tool** developed to automate the exploitation phase of the **Wormhole** laboratory on **TryHackMe**.  
This script demonstrates how to automate **Endpoint Discovery**, **Credential Brute-forcing**, and **Authorized API Interaction** in a controlled CTF environment.

---

## 📖 How It Works

The script follows a **4-step logical flow** to gain control of the target system:

### 1️⃣ Endpoint Discovery
The script iterates through a list of common API patterns such as:
- `/api/auth`
- `/admin/token`
- `/action/login`

to discover the **active authentication endpoint**.

---

### 2️⃣ Brute Force Attack
Using the `requests` library, the script performs a **dictionary attack** with the **rockyou.txt** wordlist against the discovered login endpoint.

---

### 3️⃣ Token Extraction
Once authentication succeeds, the script:
- Parses the server response (JSON / text)
- Uses **Regular Expressions (`re`)**
- Extracts the **Operator Token**

---

### 4️⃣ PIN Exhaustion
With the valid operator token:
- Sends an authorized **Close** command
- Brute-forces a **4-digit PIN** in the range `4000–5000`
- Successfully completes the challenge

---

## 🛠️ Prerequisites

Ensure the following are installed before running the script:

### 🔹 System Requirements
- Python **3.x**
- Linux environment (recommended)

### 🔹 Wordlist
- **RockYou Wordlist**


> Update the path in the script if necessary.

### 🔹 Python Library
Install the required dependency:
```bash
pip install requests

target_url = 'http://10.10.xx.xx/terminal.php'


python3 thm_wormhole_auto.py


[*] Discovering endpoints...
[+] Found endpoint: http://10.10.xx.xx/action/login
[*] Starting brute force attack...
[+] Authentication successful with password: password123
[*] Obtaining operator token...
[+] Operator token obtained: eyJhbGciOiJIUzI1...
[*] Calling close operation...
[+] Successfully closed wormhole with PIN: 4082


├── thm_wormhole_auto.py   # Main automation logic
├── README.md            # Documentation & usage
├── .gitignore           # Excludes wordlists & local logs

# TryHackMe: Wormhole Automation Script

This repository contains a Python-based automation tool designed to solve challenges involving endpoint discovery, credential brute-forcing, and API manipulation. This script was specifically developed for educational purposes within the context of TryHackMe (THM) labs.

## 🚀 Features
* **Endpoint Discovery:** Scans for common authentication and API endpoints.
* **Automated Brute Force:** Interfaces with standard wordlists (like `rockyou.txt`) to identify valid credentials.
* **Token Extraction:** Automatically parses responses to capture session/operator tokens.
* **PIN Exhaustion:** Brute-forces a specific PIN range (4000-5000) to execute a "Close Operation" command.

## 🛠️ Requirements
* Python 3.x
* `requests` library
* A copy of the `rockyou.txt` wordlist (standard in Kali Linux at `/usr/share/wordlists/`)

Install dependencies:
```bash
pip install requests

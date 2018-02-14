def xor(h1, h2):
    return "".join(chr(ord(c1) ^ ord(c2)) for c1,c2 in zip(h1, h2))

def decrypt_aes128(key, text):
    from Crypto.Cipher import AES
    decryptor = AES.new(key, AES.MODE_ECB)
    return decryptor.decrypt(text)

def encrypt_aes128(key, text):
    from Crypto.Cipher import AES
    encryptor = AES.new(key, AES.MODE_ECB)
    return encryptor.encrypt(text)

def encrypt_cbc(key, txt):
    iv = "\00" * 16
    res = []
    for i in range(0, len(txt), 16):
        val = xor(iv, txt[i:i+16])
        enc = encrypt_aes128(key, val)
        res.append(enc)
        iv = enc
    return "".join(res)

def decrypt_cbc(key, txt):
    iv = "\00" * 16
    res = []
    for i in range(0, len(txt), 16):
        dec = decrypt_aes128(key, txt[i:i+16])
        val = xor(iv, dec)
        res.append(val)
        iv = txt[i:i+16]
    return "".join(res)

if __name__ == '__main__':
    data = None
    with open("10.txt") as f:
        data = f.read().decode('base64')

    key = "YELLOW SUBMARINE"

    print(decrypt_cbc("YELLOW SUBMARINE", data))


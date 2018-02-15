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

def little_endian(count):
    res = []
    while count:
        res.append(chr(count % 256))
        count //= 256
    left = 8 - len(res)
    res += [chr(0)] * left
    return "".join(res)

def encrypt_ctr(key, nonce, txt):
    length = len(txt) // 16 + 1
    key = "".join(encrypt_aes128(key, little_endian(nonce) + little_endian(count)) for count in range(length))
    return xor(key, txt)

def decrypt_ctr(key, nonce, txt):
    length = len(txt) // 16 + 1
    key = "".join(encrypt_aes128(key, little_endian(nonce) + little_endian(count)) for count in range(length))
    return xor(key, txt)

if __name__ == '__main__':
    data = "L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==".decode('base64')
    print(decrypt_ctr("YELLOW SUBMARINE", 0, data))


lines = []
with open("data17") as f:
    for line in f.readlines():
        lines.append(line)

def padded(text):
    l = len(text) % 16
    l = 16 - l if l else 0

    return text + chr(l) * l

from random import choice
from string import ascii_lowercase
line = padded(choice(lines).decode('base64'))
key = "".join(choice(ascii_lowercase) for _ in range(16))

from cbc import encrypt_cbc, decrypt_cbc
from pkcs7_validate import validate

print(validate(decrypt_cbc(key, encrypt_cbc(key, line))))

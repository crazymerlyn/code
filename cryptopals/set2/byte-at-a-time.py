a = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK".decode('base64')

from random import choice
from string import ascii_lowercase as ascii_lower

key = "".join(choice(ascii_lower) for _ in range(16))

from cbc import encrypt_aes128

def myencrypt(text):
    text += a
    return encrypt_aes128(key, text[:len(text)//16*16])


s = "A" * 16

l = len(myencrypt(""))
for j in range(l):
    block = j // 16
    index = j % 16 + 1
    table = {}
    for i in range(256):
        c = chr(i)
        text = s[-15:] + c
        cipher = myencrypt(text)
        table[cipher[:16]] = c

    c = myencrypt("A" * (16 - index))
    s += table[c[block*16:block*16+16]]
print(s)

import base64

def hex_to_base64(h):
    return base64.b64encode(h.decode("hex"))


h = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
encoded = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

assert(hex_to_base64(h) == encoded)


def xor(h1, h2):
    return "".join(chr(ord(c1) ^ ord(c2)) for c1,c2 in zip(h1, h2))


h1 = "1c0111001f010100061a024b53535009181c".decode("hex")
h2 = "686974207468652062756c6c277320657965".decode("hex")
xorred = "746865206b696420646f6e277420706c6179".decode("hex")

assert(xor(h1, h2) == xorred)


from english import score
from string import ascii_lowercase

def solve_single_char_xor(cipher):
    possibs = []
    for c in range(0, 256):
        c = chr(c)
        possib = xor(cipher, c * len(cipher))
        possibs.append((c, possib))
    return max(possibs, key=lambda (c,t): score(t))

cipher = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736".decode("hex")

print `solve_single_char_xor(cipher)`

"""
with open("lines.txt") as f:
    solutions = []
    for line in f:
        line = line.strip().decode("hex")
        solution = solve_single_char_xor(line)
        solutions.append(solution)
    print `max(solutions, key=score)`
"""

def repeat_key_xor(key, text):
    from itertools import cycle
    for k, t in zip(cycle(key), text):
        yield chr(ord(k) ^ ord(t))

key = "ICE"
text = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
print "".join(repeat_key_xor(key, text)).encode("hex")


def edit_distance(text_a, text_b):
    assert(len(text_a) == len(text_b))
    result = 0
    for c1, c2 in zip(text_a, text_b):
        result += sum(b1 != b2 for b1, b2 in zip(bin(ord(c1))[2:].zfill(8), bin(ord(c2))[2:].zfill(8)))

    return result

print edit_distance("this is a test", "wokka wokka!!!")

def solve_repeat_key_xor(text):
    possibs = []
    for size in range(2, min(40, len(text) // 4)):
        dist1 = edit_distance(text[:size], text[size:2*size])
        dist2 = edit_distance(text[size:2*size], text[2*size:3*size])
        dist3 = edit_distance(text[2*size:3*size], text[3*size:4*size])
        possibs.append((float(dist1 + dist2 + dist3)/size/3, size))

    possibs = sorted(possibs)

    all_solutions = []

    for _, size in possibs[:3]:
        singles = [text[i::size] for i in range(size)]
        solutions = [solve_single_char_xor(x) for x in singles]

        solution = ("".join(c for c,_ in solutions), "".join("".join(x) for x in zip(*(t for _, t in solutions))))
        all_solutions.append(solution)

    return max(all_solutions, key=lambda (_,t): score(t))



#text = open("repeat_key.txt").read().decode("base64")
#print solve_repeat_key_xor(text)


def decrypt_aes128(key, text):
    from Crypto.Cipher import AES
    decryptor = AES.new(key, AES.MODE_ECB)
    return decryptor.decrypt(text)

#text = open("aes128.txt").read().decode("base64")
#print decrypt_aes128("YELLOW SUBMARINE", text)


texts = open("./aes_multiple.txt").readlines()
solutions = [decrypt_aes128("YELLOW SUBMARINE", text.strip().decode("hex")) for text in texts]
print max(solutions, key=score)


def pad(text, n):
    rest = len(text) % n
    padding_len = n - rest if rest else 0
    return text + chr(padding_len) * padding_len

print(repr(pad("Yellow Submarine", 20)))

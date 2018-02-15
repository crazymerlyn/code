class InvalidPadding(ValueError):
    pass

def validate(text):
    if not text or ord(text[-1]) > 15: return True
    l = ord(text[-1])

    if text[-l:] == chr(l) * l: return True
    raise InvalidPadding(repr(text[-l:]) + " is not valid")

if __name__ == "__main__":
    print(validate("abcdefghijklmno\02"))

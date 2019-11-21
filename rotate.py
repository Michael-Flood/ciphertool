# rotate.py

def cipher_rotate(char, rotation):
    """
    Function to cipher individual characters of strings. Takes individual characters as input and returns shifted characters
    """
    digit = ord(char)
    cipherdigit = None
    ciphrange = range(32,127)
    if (digit + rotation) not in ciphrange:
        if (digit + rotation) > 126:
            difference = (digit + rotation) - 126
            adjustment = difference - 1
            cipherdigit = 32 + adjustment
        elif (digit + rotation) < 32:
            difference = digit + rotation
            adjustment = (difference - 32) + 1
            cipherdigit = 126 + adjustment
    else:
        cipherdigit = (digit + rotation)

    cipherchar = chr(cipherdigit)
    distance = cipherdigit - digit
    return cipherchar

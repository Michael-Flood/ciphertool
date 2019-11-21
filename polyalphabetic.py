# polyalphabetic ciphers

from rotate import cipher_rotate

def key_fill(key_text, message_len):
    """
    Returns a filled key.
    Example:
    key_fill("LEMON", 14) -> "LEMONLEMONLEMO"
    """
    filled_key = []
    key_len = len(key_text)
    key_pos = 0
    for i in range(0, message_len):
        if key_pos < key_len:
            c = key_text[key_pos]
            filled_key.append(c)
            key_pos += 1
        elif key_pos >= key_len:
            key_pos = 0
            c = key_text[key_pos]
            filled_key.append(c)
            key_pos += 1

    return filled_key

def polycipher(input_text, key_text, action):
    """
    Implements Polyalphabetic Vigenere cipher.
    'action' paramater defines whether ciphering or deciphering
    """
    filled_key = key_fill(key_text, len(input_text))
    filled_key_vals = [ord(x) for x in filled_key]
    offsets = []
    for i in range(0,len(filled_key_vals)):
        offset = filled_key_vals[i] - 32
        if action == 'cipher':
            pass
        elif action == 'decipher':
            offset = offset * -1
        offsets.append(offset)
    cipher_chars = []
    for i in range(0,len(input_text)):
        char = input_text[i]
        rotate = offsets[i]
        ciph = cipher_rotate(char, rotate)
        cipher_chars.append(ciph)
    separator = ''
    cipher_text = separator.join(cipher_chars)
    return cipher_text

if __name__ == "__main__":
    # quick test of the cipher and decipher functions
    print( polycipher('ABCDEF', 'A', 'cipher') )
    print( polycipher('bcdefg', 'A', 'decipher'))

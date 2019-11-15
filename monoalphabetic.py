# monoalphabetic.py - implements a monoalphabetic (Caesar) cipher.

def rotate(char, rotation):
    """
    Function to cipher individual characters of strings. Takes individual characters as input and returns shifted
    """
    digit = ord(char)
    cipherdigit = None
    if (digit + rotation) <= 32:
        diff = -((digit + rotation) - 32)
        cipherdigit = 127 - diff
    elif (digit + rotation) >= 126:
        diff = ((digit + rotation)) - 126
        cipherdigit = 32 + diff
    elif (digit + rotation) >= 33 and ((digit + rotation) < 126):
        cipherdigit = digit + rotation
    cipherchar = chr(cipherdigit)
    return cipherchar

def caesar(inputtext, rotation):
    """
    Implements monoalphabetic substitution (i.e. Caesar) cipher, moving characters forwards
    or backwards through the alphabet based on the rotation integer.
    Example:
    'abc' (rotation 3) -> 'def'
    'def' (rotation -3) -> 'abc'
    """
    charlist = list(inputtext)
    output = []
    for char in charlist:
        print(char)
        cipherchar = rotate(char, rotation)
        output.append(cipherchar)
    separator = ''
    outputtext = separator.join(output)
    outputtext = outputtext.replace(u'\x7f', u' ')
    return outputtext

if __name__ == "__main__":
    print(caesar('abcdefghi', 3))

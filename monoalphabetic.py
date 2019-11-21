# monoalphabetic.py - implements a monoalphabetic (Caesar) cipher.

from rotate import cipher_rotate

# def rotate(char, rotation):
#     """
#     Function to cipher individual characters of strings. Takes individual characters as input and returns shifted characters
#     """
#     digit = ord(char)
#     cipherdigit = None
#     ciphrange = range(32,127)
#     if (digit + rotation) not in ciphrange:
#         if (digit + rotation) > 126:
#             difference = (digit + rotation) - 126
#             adjustment = difference - 1
#             cipherdigit = 32 + adjustment
#         elif (digit + rotation) < 32:
#             difference = digit + rotation
#             adjustment = (difference - 32) + 1
#             cipherdigit = 126 + adjustment
#     else:
#         cipherdigit = (digit + rotation)
#
#     cipherchar = chr(cipherdigit)
#     distance = cipherdigit - digit
#     print(char, digit, cipherdigit, cipherchar, distance)
#     return cipherchar

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
        cipherchar = cipher_rotate(char, rotation)
        output.append(cipherchar)
    separator = ''
    outputtext = separator.join(output)
    outputtext = outputtext.replace(u'\x7f', u' ')
    return outputtext

if __name__ == "__main__":
    print(caesar('abcdefghi', 20))
    print(caesar(' ', -1))

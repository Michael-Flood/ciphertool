def cipherrotate(character, rot):
    # rotates cipher digits through the ASCII table from 37 to 126, then returns to start if it is beyond that.
    # ('a', 1) -> 'b' or 97->98
    # ('!' 2) -> '#' or 33->35
    # ('Z', 13) -> ')' or ->41
    # can work backwards when using negative numbers, enabling encryption and decryption with a single function
    digit = ord(character)
    cipherdigit = None
    if rot == 0:
        print("Cipher rotation must be greater or less than 0. Please use a positive or negative integer")
    if (digit + rot) <= 32:
        diff = -((digit + rot) - 32)
        cipherdigit = 127 - diff
    elif (digit + rot) >= 126:
        diff = ((digit + rot) - 126)
        cipherdigit = 31 + diff
    elif (digit + rot) >= 33 and ((digit + rot) <= 126):
        cipherdigit = digit + rot
    # check if cipherdigit still = None
    cipherchar = chr(cipherdigit)
    return cipherchar

def caesarcipher(text, rot):
    # Caesar Cipher using settable rotation
    # Str -> Str
    # 'aaa' -> caesarcipher('aaa', 1) -> 'bbb'

    # split string into list of chars, ciphers (with positive integer rot) or deciphers (with negative integer rot)
    charlist = list(text)
    output = []
    for char in charlist:
        cipherchar = cipherrotate(char, rot)
        output.append(cipherchar)
    separator = ''
    outputtext = separator.join(output)
    return outputtext

def caesarbruteforce(text):
    # Brute force solves an ASCII-based Caesar/rotation cipher. Advances the digits through each of the 126 ASCII character positions and returns their values.
    for i in [x for x in range(-46,46) if x != 0]:
        attempt = caesarcipher(text, i)
        print(str(i) + " : " + attempt)
    return 0

def vigenerecipher(text, key, **kwargs):
    kwargs = kwargs
    textlen = len(text)
    keylen = len(text)
    textlist = list(text)
    keylist = list(key)
    keystream = []
    keyposition = 0
    while len(keystream) < textlen:
        try:
            keystream.append(keylist[keyposition])
            keyposition += 1
        except IndexError:
            keyposition = 0
    textlist_ord = [( ord(x)) for x in textlist]
    keystream_ord = [ (ord(x)) for x in keystream]
    cipherstream = [] # empty list to receive the chars after encipherment
    # if the keyword argument 'decipher' is set to True, reverse the encipherment. If not, encipher as normal.
    if kwargs['decipher'] == True:
        pass # decipher
    elif kwargs['decipher'] == False or kwargs['decipher'] == None:
        pass # encipher
    else:
        pass # encipher
    # check that ordinals fall within specified range (32-126), reset them if they are not
    for i in range(0,len(textlist_ord)):
        if textlist_ord[i] < 32:
            charposition = 32 - textlist_ord[i]
            newposition = 126 - charposition
    for i in range(0,len(keystream_ord)):
        if textlist_ord[i] < 32:
            charposition = 32 - textlist_ord[i]
            newposition = 126 - charposition
    cipherstream = []
    print(textlist_ord)
    print(keystream_ord)

vigenerecipher('This is a secret message', 'Avocado', decipher=True)

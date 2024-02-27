characters = [
    # lowercase characters
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    # uppercase characters
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    # space and symbols
    ' ',',','.','?','!','@','#','$','&','*','(',')'
]

# use this method to encode an alphabet character into a binary string
def encode(character):
    charIndex = characters.index(character)
    return '{0:06b}'.format(charIndex)

# use this method to decode a binary string into an alphabet character
def decode(binary):
    charIndex = int(binary, 2)
    return characters[charIndex]

def XOR(bit1,bit2):
    if bit1 == bit2:
        return "0"
    else:
        return "1"

def XORonbyte(byte, key):
    byte = str(byte)
    key = str(key)
    ebyte = ""
    for i in range(len(byte)):
        ebyte += XOR(byte[i], key[(i % len(key))])
    return ebyte

def XORonchar(char, keychar):
    bchar = encode(char)
    bkeychar = encode(keychar)
    ebchar = XORonbyte(bchar, bkeychar)
    return decode(ebchar)

def XORonstring(string, keystring):
    estring = ""
    for i in range(len(string)):
        estring += XORonchar(string[i], keystring[(i % len(keystring))])
    return estring

print(XORonstring("Ej&AN&s&nNFDLaEY,&mBEmZ", "no it aint"))
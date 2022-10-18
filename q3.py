


def make_block(lst):
    return (ord(lst[0])<<24) + (ord(lst[1])<<16) + (ord(lst[2])<<8) + ord(lst[3])

def encrypt(message, key):
    rv = ""
    l = list(message)
    n = len(message)
    blocks = []
    for i in range(0,n,4):  # break message into 4-character blocks
        if i+4 <= n:
            blocks.append(make_block(l[i: i+4]))
        else: #pad end of message with white-space if the length is not divisible by 4
            end = l[i:n]
            end.extend((i+4-n)*[' '])
            blocks.append(make_block(end))
    extended_key = (key << 24) + (key << 16) + (key << 8) + (key)
    for block in blocks:   #encrypt each  block separately
        encrypted = str(hex(block ^ extended_key))[2:]
        for i in range(8 - len(encrypted)):
            rv += '0'
        rv += encrypted
    return rv



def decrypt(cipher, key):

    extended_key = (key << 24) + (key << 16) + (key << 8) + (key)
    msg = ""
    for i in range(0, len(cipher), 8):
        j = int(cipher[i:i + 8], 16) ^ extended_key

        character1 = chr(j // 2 ** 24)
        j -= ord(character1) << 24
        character2 = chr(j // 2 ** 16)
        j -= ord(character2) << 16
        character3 = chr(j // 2 ** 8)
        j -= ord(character3) << 8
        character4 = chr(j)

        msg += character1 + character2 + character3 + character4

    return msg

for i in range(0,256):
    print(decrypt("10170d1c0b17180d10161718151003180d101617",i),i)
from Crypto.Cipher import AES
from itertools import chain
import random
import base64

BLOCK_SIZE = 16

def encrypt():
    charset = "".join(chr(i) for i in chain(range(ord('a'), ord('z') + 1), range(ord('A'), ord('Z') + 1), range(ord('1'), ord('9') + 1)))
    key = ''.join(random.choice(charset) for x in range(BLOCK_SIZE * 2))
    iv = ''.join(random.choice(charset) for x in range(BLOCK_SIZE))

    print("key " + key)
    print("iv " + iv)

    encr = AES.new(key, AES.MODE_CFB, iv)
    flag = "t0r0nt0_ch4ll{aes_34zy_t0_d3crypt}"
    cipher = base64.b64encode(encr.encrypt(flag)).hex()
    print(cipher)

def decrypt():
    key = b"iJ6yXU8Chxc1KDSOySKqlwwII8qRsIeU"
    iv = b"9SMZqL8LyeKEPc9S"
    decr = AES.new(key, AES.MODE_CFB, iv)
    plain = decr.decrypt(base64.b64decode(bytearray.fromhex("6f4d34726b5436342f5a4352725a49483670776f6731532b3241554c6e45587857714d774b544e70547171666a773d3d").decode())).decode("utf-8") 
    print(plain)

encrypt()
decrypt()

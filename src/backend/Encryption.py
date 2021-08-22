from Crypto.Hash import SHA3_512, SHA256
from Crypto.Cipher import AES
from Crypto import Random
import base64

bs = AES.block_size

#
# @param key: key to hash
# @return: hashed output in string format
#
def hash(key):
    sah512 = SHA3_512.new(key.encode())
    return sah512.hexdigest()

#
# @param key: key to hash
# @return: hashed output in byte string format..
#
def hashEnc(key):
    sha256 = SHA256.new(key.encode())
    return sha256.digest()

def pad(s):
    return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]


#
# @param key: SHA-256 hashed key
# @param data: Data to be encrypted
# @return: AES encrypted data
#
def encrypt(raw, key):
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw.encode()))

#
# @param key: SHA-256 hashed key
# @pram enc: AES encrypted data
# @return: Decrypted data
#
def decrypt(enc, key):
    enc = base64.b64decode(enc)
    iv = enc[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from matplotlib import cm
from random import getrandbits
from time import time
from Crypto.Cipher import AES


def cipher_params(cipher, mode):
    if mode in [AES.MODE_CBC]:
        return dict(iv=cipher.iv)
    if mode in [AES.MODE_CTR]:
        return dict(nonce=cipher.nonce)
    return {}


def join_tables(a, b):
    df = pd.concat([a, b], axis=1)
    df.columns = [x + ' - encrypt' for x in modenames] + [x + ' - decrypt' for x in modenames]
    return df[flatten([(x + ' - encrypt', x + ' - decrypt') for x in modenames])]


def pad(x):
    return x + b'\0' * (AES.block_size - len(x) % AES.block_size)


def strip(x):
    return x.rstrip(b'\0')


def hexdump(x):
    return ' '.join(f'{b:02X}' for b in x)


def flatten(a):
    return [x for b in a for x in b]


def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))


def My_CBC(plain, key, initial_value = "qwertyuiopasdfgh", block_len = 32):
    c = AES.new(key, AES.MODE_ECB)
    res = ""
    for chunk in chunkstring(plain, block_len):
        # print(chunk)
        bitchunk = bytes(chunk, 'utf-8')
        bitinit = bytes(initial_value, 'utf-8')
        bitxored = bytes(a ^ b for a, b in zip(bitchunk, bitinit))
        crypted = c.encrypt(pad(bitxored))
        res += crypted.decode('utf-8')
        initial_value = crypted
    print("Encrypted: ")
    print(res)
    return res


def My_CBC_decrypt(encrypted, key, initial_value = "qwertyuiopasdfgh", block_len = 32):
    c = AES.new(key, AES.MODE_ECB)
    res = ""
    for chunk in chunkstring(encrypted, block_len):
        # print(chunk)
        c.decrypt(chunk)
        bitchunk = bytes(chunk, 'utf-8')
        bitinit = bytes(initial_value, 'utf-8')
        bitxored = bytes(a ^ b for a, b in zip(bitchunk, bitinit))
        initial_value = chunk
        ch_res = bitxored.decode('utf-8')
        res += ch_res
    print('Decrypted: ')
    print(res)
    return res

def xor(in1, in2):
    ret = []
    for i in range(0, max(len(in1), len(in2))):
        ret.append(in1[i % len(in1)] ^ in2[i % len(in2)])
    return bytes(ret)

def decrypt_aes_ecb(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(data)

def encrypt_aes_ecb(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(data)

def pkcs7(val, block_size=16):
    padding_length = block_size - (len(val) % block_size)
    if padding_length == block_size:
        padding_length = block_size
    padding = bytes([padding_length]) * padding_length
    if isinstance(val, str):
        val = val.encode()
    return val + padding


def unpkcs7(val, block_size=16):
    pad_amount = val[-1]
    if pad_amount == 0:
        raise Exception
    for i in range(len(val) - 1, len(val) - (pad_amount + 1), -1):
        if val[i] != pad_amount:
            raise Exception
    return val[:-pad_amount]

def decrypt_aes_cbc(data, key, iv = b'\x00' * 16, pad=True):
    prev_chunk = iv

    decrypted = []

    for i in range(0, len(data), 16):
        chunk = data[i : i + 16]
        decrypted += xor(decrypt_aes_ecb(chunk, key), prev_chunk)
        prev_chunk = chunk

    if pad:
        return unpkcs7(bytes(decrypted))
    return bytes(decrypted)

def encrypt_aes_cbc(data, key, iv = b'\x00' * 16, pad=True):
    if pad:
        padded = pkcs7(data)
    else:
        padded = data
    prev_chunk = iv
    encrypted = []
    for i in range(0, len(padded), 16):
        chunk = padded[i : i + 16]
        encrypted_block = encrypt_aes_ecb(xor(chunk, prev_chunk), key)
        encrypted += encrypted_block
        prev_chunk = encrypted_block
    return bytes(encrypted)


sns.set_style('darkgrid')
plt.rc('figure', figsize=(10, 6), dpi=200)
# pad = lambda x: x + b'\0' * (AES.block_size - len(x) % AES.block_size)
# strip = lambda x: x.rstrip(b'\0')
# hexdump = lambda x: ' '.join(f'{b:02X}' for b in x)
# flatten = lambda a: [x for b in a for x in b]

key = getrandbits(16 * 8).to_bytes(16, byteorder='little')

modenames = 'ECB CBC CTR'.split()
files = 'test_txt.txt test_pdf.pdf test_zip.zip test_mov.MP4'.split()
sizes = [0.0015, 0.722, 7.55, 761]
size_labels = ["1.59KB", "722KB", "7.55MB", "761MB"]  # todo Check czy stringi są ok
modes = [AES.MODE_ECB, AES.MODE_CBC, AES.MODE_CTR]

decr_time = pd.DataFrame(index=files, columns=modenames)
encr_time = pd.DataFrame(index=files, columns=modenames)
print('key =', hexdump(key))

# Zebranie czasów
for file in files:
    with open(file, 'rb') as f:
        original = f.read()

    for mode, name in zip(modes, modenames):
        c1 = AES.new(key, mode)
        t1 = time()
        encrypted = c1.encrypt(pad(original))
        t1 = time() - t1

        c2 = AES.new(key, mode, **cipher_params(c1, mode))
        t2 = time()
        decrypted = c2.decrypt(encrypted)
        t2 = time() - t2

        decrypted = strip(decrypted)
        encr_time.loc[file, name] = t1
        decr_time.loc[file, name] = t2

print("Czasy szyfrowania i deszyfrowania konkretnych plików ")
time_all = join_tables(encr_time, decr_time)
print(time_all)

# Test propagacji błędu

with open('test_txt.txt', 'rb') as f:
    test = f.read()

print('--- ORIGINAL ---')
print(test)
print()

for mode, name in zip(modes, modenames):
    c1 = AES.new(key, mode)
    encrypted = c1.encrypt(pad(test))

    encrypted = bytearray(encrypted)
    encrypted[120] = 0

    c2 = AES.new(key, mode, **cipher_params(c1, mode))
    decrypted = strip(c2.decrypt(encrypted))
    print('---', name, '---')
    print(decrypted)
    print()


test_txt = "Ala ma kota Ala ma kota Ala ma kota Ala ma kota Ala ma kota Ala ma kota Ala ma kota Ala ma kota i poprawke"
# enc = My_CBC(test_txt, key)
# dec = My_CBC_decrypt(enc, key)

enc = encrypt_aes_cbc(test_txt, key)
print(enc)
dec = decrypt_aes_cbc(enc, key)
print(dec)

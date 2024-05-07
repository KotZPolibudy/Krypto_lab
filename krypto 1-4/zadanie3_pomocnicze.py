import hashlib
import time
import sys


def MD5(jawny):
    return hashlib.md5(jawny.encode('utf-8'))


def SH_1(jawny):
    return hashlib.sha1(jawny.encode('utf-8'))


def SH_2(jawny):
    # return hashlib.sha256(jawny.encode('utf-8'))
    # return hashlib.sha384(jawny.encode('utf-8'))
    # return hashlib.sha224(jawny.encode('utf-8'))
    return hashlib.sha512(jawny.encode('utf-8'))


def SH_3(jawny):
    # return hashlib.sha3_224(jawny.encode('utf-8'))
    # return hashlib.sha3_256(jawny.encode('utf-8'))
    # return hashlib.sha3_384(jawny.encode('utf-8'))
    return hashlib.sha3_512(jawny.encode('utf-8'))


def main():
    if len(sys.argv) < 1:
        return "Tak nie można, podaj jakieś słowo do zakodowania!"

if __name__ == '__main__':
    wyn = main()
    print(wyn)






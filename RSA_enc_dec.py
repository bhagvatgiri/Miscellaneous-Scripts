# -*- coding: utf-8 -*-

# installing the pycryptodome library
# !pip install pycryptodome



from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import binascii

def rsa_enc_public(inputblock, keypair):
    # inputblock is a plaintext defined as a byte sequence
    # ciphertext is the encrypted data as byte sequence encrypted using the public key
    pubKey = keypair.publickey()
    encryptor = PKCS1_v1_5.new(pubKey)  #The variable pubKey was derived from the keyPair variable in the above code cell.
    encrypted = encryptor.encrypt(inputblock)  
    return encrypted

def rsa_dec_private(cipherblock, keypair):
    # cipherblock is a given ciphertext defined as a byte sequence
    # plaintext is the decrypted data as byte sequence decrypted using the private key
    decryptor = PKCS1_v1_5.new(keypair)
    plaintext = decryptor.decrypt(cipherblock, None)
    return plaintext


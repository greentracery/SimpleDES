# Simple wrapper for pyDES library
# Homepage: https://github.com/greentracery/SimpleDES
# Requirements:
# - pyDES
# Usage:
#   from . simpledes import Des, TripleDes
#
#   c1 = Des("passphrase" [, bias=[0..n])
#   encrypted_data = c1.encrypt(source_data [, b64=True|False])
#   source_data = c1.decrypt(encrypted_data [, b64=True|False])
#
#   c2 = TripleDes("passphrase" [, bias=0..n])
#   encrypted_data = c2.encrypt(source_data [, b64=True|False])
#   source_data = c2.decrypt(encrypted_data [, b64=True|False])
#
# See also pyDEC documentation on https://github.com/twhiteman/pyDes
#

import pyDes
import hashlib
import base64
from typing import Union

class Crypton():
    __k__ = None
    __IV__ = "\0\0\0\0\0\0\0\0" # Initial Value for CBC mode
    
    def encrypt(self, src_data, b64: bool = False):
        enc_data = self.__k__.encrypt(src_data)
        if b64:
            return base64.b64encode(enc_data)
        return enc_data

    def decrypt(self, enc_data, b64: bool = False, encoding: Union[str, None] = 'UTF-8'):
        if b64:
            enc_data = base64.b64decode(enc_data)
        data = self.__k__.decrypt(enc_data) 
        return data.decode(encoding) # bytearray -> string

class Des(Crypton):
    
    def __init__(self, passphrase: str, bias: Union[int, None] = 0):
        if len(passphrase) == 0:
            raise Exception ("Passphrase can't be empty")
        # create a hash to obtain a key phrase of maximum length for generating a key, regardless of the original one:
        keyphrase = hashlib.sha512(passphrase.encode().strip()).hexdigest()
        keylenght = 8 # Key must be exactly 8 bytes long. See pyDES documentation;
        # use the bias value to randomize the creation of the key from the passphrase:
        if bias > (len(keyphrase) - keylenght):
            bias = bias % (len(keyphrase) - keylenght)
        key = keyphrase.encode()[bias:(keylenght + bias)] 
        self.__k__ = pyDes.des(key, pyDes.CBC, self.__IV__, pad=None, padmode=pyDes.PAD_PKCS5)

class TripleDes(Crypton):
    
    def __init__(self, passphrase: str, bias: Union[int, None] = 0):
        if len(passphrase) == 0:
            raise Exception ("Passphrase can't be empty")
        # create a hash to obtain a key phrase of maximum length for generating a key, regardless of the original one:
        keyphrase = hashlib.sha512(passphrase.encode().strip()).hexdigest()
        keylenght = 24 # Use DES-EDE3 method when a 24 byte key is supplied.
        # use the bias value to randomize the creation of the key from the passphrase:
        if bias > (len(keyphrase) - keylenght):
            bias = bias % (len(keyphrase) - keylenght)
        key = keyphrase.encode()[bias:(keylenght + bias)] 
        self.__k__ = pyDes.triple_des(key, pyDes.CBC, self.__IV__, pad=None, padmode=pyDes.PAD_PKCS5)
    

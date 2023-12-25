# SimpleDES - the simplest wrapper wrapper for pyDES library
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
from abc import ABC, abstractmethod

class Crypton(ABC): #Prohibits the creation of the class object directly
    """ 
        Abstract class for SimpleDES encoder-decoder.
        SimpleDES is the simplest wrapper for pyDES library
        
        method: encrypt(scr_data, b64=False): returns encrypted data
        method: decrypt(enc_data, b64=False, encoding='UTF-8'): returns decrypted data
    """
    k = None
    IV = "\0\0\0\0\0\0\0\0" # Initial Value for CBC mode
    
    @classmethod
    @abstractmethod
    def __init__(self): 
        pass
    
    def encrypt(self, src_data, b64: bool = False):
        """
            This method return encryptrd data.
            
            :param src_data: Original data that must be encrypted 
            :param b64: Return encrypted result encoded in base64 (optional, default False)
            :returns: Encrypted data
        """
        enc_data = self.k.encrypt(src_data)
        if b64:
            return base64.b64encode(enc_data)
        return enc_data

    def decrypt(self, enc_data, b64: bool = False, encoding: Union[str, None] = 'UTF-8'):
        """
            This method returns the decrypted data
            
            :param enc_data: Encrypted data that must be decrypted 
            :param b64: Encrypted data encoded in base64 (optional, default False)
            :param encodind: Encoding of decrypted data (optional, default UTF-8)
            :returns: Decrypted data
        """
        if b64:
            enc_data = base64.b64decode(enc_data)
        data = self.k.decrypt(enc_data) 
        return data.decode(encoding) # bytearray -> string

class Des(Crypton):
    """ Implementation for DES encoder-decoder """
    def __init__(self, passphrase: str, bias: Union[int, None] = 0):
        """
            Creates an instance of an object 
            
            :param passphrase: Text string to generate the key 
            :param bias: Starting offset to randomize key generation from a text string (optional, default 0)
            :raises Exception: raises an exception
        """
        if len(passphrase) == 0:
            raise Exception ("Passphrase can't be empty")
        # create a hash to obtain a key phrase of maximum length for generating a key, regardless of the original one:
        keyphrase = hashlib.sha512(passphrase.encode().strip()).hexdigest()
        keylenght = 8 # Key must be exactly 8 bytes long. See pyDES documentation;
        # use the bias value to randomize the creation of the key from the passphrase:
        if bias > (len(keyphrase) - keylenght):
            bias = bias % (len(keyphrase) - keylenght)
        key = keyphrase.encode()[bias:(keylenght + bias)] 
        self.k = pyDes.des(key, pyDes.CBC, self.IV, pad=None, padmode=pyDes.PAD_PKCS5)

class TripleDes(Crypton):
    """ Implementation for TripleDES encoder-decoder """
    def __init__(self, passphrase: str, bias: Union[int, None] = 0):
        """
            Creates an instance of an object 
            
            :param passphrase: Text string to generate the key 
            :param bias: Starting offset to randomize key generation from a text string (optional, default 0)
            :raises Exception: raises an exception
        """
        if len(passphrase) == 0:
            raise Exception ("Passphrase can't be empty")
        # create a hash to obtain a key phrase of maximum length for generating a key, regardless of the original one:
        keyphrase = hashlib.sha512(passphrase.encode().strip()).hexdigest()
        keylenght = 24 # Use DES-EDE3 method when a 24 byte key is supplied.
        # use the bias value to randomize the creation of the key from the passphrase:
        if bias > (len(keyphrase) - keylenght):
            bias = bias % (len(keyphrase) - keylenght)
        key = keyphrase.encode()[bias:(keylenght + bias)] 
        self.k = pyDes.triple_des(key, pyDes.CBC, self.IV, pad=None, padmode=pyDes.PAD_PKCS5)
    

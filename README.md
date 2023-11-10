# SimpleDES

Simple wrapper for pyDES library

Homepage: https://github.com/greentracery/SimpleDES
    
## Requirements:

    - pyDES
    
## Usage:

```python
    
    from . simpledes import Des, TripleDes
    
    c1 = Des("passphrase" [, bias=[0..n])
    
    encrypted_data = c1.encrypt(source_data [, b64=True|False])
    
    source_data = c1.decrypt(encrypted_data [, b64=True|False])

    c2 = TripleDes("passphrase" [, bias=0..n])
    
    encrypted_data = c2.encrypt(source_data [, b64=True|False])
    
    source_data = c2.decrypt(encrypted_data [, b64=True|False])
    
```

See also pyDEC documentation on https://github.com/twhiteman/pyDes

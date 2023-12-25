# SimpleDES - the simplest wrapper for pyDES library

Homepage: https://github.com/greentracery/SimpleDES
    
## Requirements:

    - pyDES

## Usage:

### Preparing:
    
    1. Install package: pip install dist/SimpleDES-_version_.tar.gz
    
    2. Or copy required files manually in your project folder & install requirements
    
### Code:

```python
    
    from simpledes.simpledes import Des, TripleDes
    
    c1 = Des("passphrase" [, bias=[0..n]) 
    
    encrypted_data = c1.encrypt(source_data [, b64=True|False])
    
    source_data = c1.decrypt(encrypted_data [, b64=True|False])

    c2 = TripleDes("passphrase" [, bias=0..n])
    
    encrypted_data = c2.encrypt(source_data [, b64=True|False])
    
    source_data = c2.decrypt(encrypted_data [, b64=True|False])
    
```

See also [pyDEC documentation](https://github.com/twhiteman/pyDes)


## P.S:

If you get some error like this:

```
    def encrypt(self, src_data, b64: bool = False):
                                   ^
    SyntaxError: invalid syntax

```
- it means that you are using Python 2.x. SimpleDES doesn't works with Python 2.x

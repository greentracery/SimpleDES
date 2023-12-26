# SimpleDES - the simplest wrapper for pyDES library

Homepage: https://github.com/greentracery/SimpleDES
    
## Requirements:
    
    - Python >= 3.5

    - pyDES

## Preparing:
    
    1. Install package: pip install dist/SimpleDES-*version*.tar.gz
    
    2. Or copy required files manually in your project folder & install requirements
    
## Usage:

```python
    
    from simpledes.simpledes import Des, TripleDes
    
    c1 = Des("passphrase" [, bias=[0..n]) 
    
    encrypted_data = c1.encrypt(source_data [, b64=True|False])
    
    source_data = c1.decrypt(encrypted_data [, b64=True|False])

    c2 = TripleDes("passphrase" [, bias=0..n])
    
    encrypted_data = c2.encrypt(source_data [, b64=True|False])
    
    source_data = c2.decrypt(encrypted_data [, b64=True|False])
    
```

See also [sample.py]

## Ext.documentation:

See also [pyDEC documentation](https://github.com/twhiteman/pyDes)

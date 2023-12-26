# Usage of SimpleDES module:

from simpledes.simpledes import Des, TripleDes

def getBias():
    while True:
        bias = input("Bias value : ")
        if bias.isdigit() : return bias 

source_data = input("Source Data: ")
passphrase = input("PassPhrase: ")
bias = int(getBias())

print("Source data: ", source_data)
print("PassPhrase: ", passphrase)
print("Bias value: ", bias)

c1 = Des(passphrase, bias)

des_enc_data = c1.encrypt(source_data)
des_enc_data_b64 = c1.encrypt(source_data, True)
des_dec_data = c1.decrypt(des_enc_data)
des_dec_data_b64 = c1.decrypt(des_enc_data_b64, True)

print("DES Encrypted data: ", des_enc_data)
print("DES Decrypted data: ", des_dec_data)
print("DES Encrypted data in base64: ", des_enc_data_b64)
print("DES Encrypted data from base64: ", des_dec_data_b64)

c2 = TripleDes(passphrase, bias)

tdes_enc_data = c2.encrypt(source_data)
tdes_enc_data_b64 = c2.encrypt(source_data, True)
tdes_dec_data = c2.decrypt(tdes_enc_data)
tdes_dec_data_b64 = c2.decrypt(tdes_enc_data_b64, True)

print("TripleDES Encrypted data: ", tdes_enc_data)
print("TripleDES Decrypted data: ", tdes_dec_data)
print("TripleDES Encrypted data in base64: ", tdes_enc_data_b64)
print("TripleDES Encrypted data from base64: ", tdes_dec_data_b64)


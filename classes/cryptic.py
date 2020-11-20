class Cryptic:
    def __init__(self):
        from cryptography.fernet import Fernet
#        with open('classes\encryption_key.bin', 'rb') as keyfile:
#            print(type(keyfile))
#            for line in keyfile:
#                print(type(line))
#                print(line)
        self.key = b'hxpEoBIhD4iHF8UVBoiG4N_42dXFAjQDgC4KkDUDFNA='
        self.cipher_suite = Fernet(self.key)

    def encrypt(self, password):
        # Convert password to byte and then returns cyphered text as a string
        ciphered_text = bytes(self.cipher_suite.encrypt(bytes(password, 'utf-8'))).decode("utf-8")
        # Returns cyphered password as string
        return ciphered_text

    def decrypt(self, ciphered_text):
        text_password = bytes(self.cipher_suite.decrypt(bytes(ciphered_text,"utf-8"))).decode("utf-8") # decode text
        # Returns the original password as a string
        return text_password

if __name__ == "__main__":
    pass
    #Cryptic()
    #from cryptography.fernet import Fernet
    #key = b'hxpEoBIhD4iHF8UVBoiG4N_42dXFAjQDgC4KkDUDFNA='
    #with open("\encryption_key.bin","wb") as keyfile:
    #    newFileByteArray = bytearray(key)
    #    keyfile.write(newFileByteArray)

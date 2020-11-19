class Cryptic:
    def __init__(self):
        from cryptography.fernet import Fernet
        with open('\encryption_key.bin', 'rb') as keyfile:
            for line in keyfile:
                self.key = line
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

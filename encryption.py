from cryptography.fernet import Fernet
import base64

class Crypt:
    def GenerateKey():
        key = Fernet.generate_key()
        return key
    
    def Encrypt(line, key):
        pass
    def Decrypt(line, key):
        pass
    def Encrypt64(line):
        line_bytes = bytes(line, "ascii")
        base64_bytes = base64.b64encode(line_bytes)
        base64_line = base64_bytes.decode("ascii")
        return base64_line
    
    def Decrypt64(line):
        base64_bytes = bytes(line, "ascii")
        line_bytes = base64.b64decode(base64_bytes)
        dec_line = line_bytes.decode("ascii")
        return dec_line
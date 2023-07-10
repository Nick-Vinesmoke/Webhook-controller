from cryptography.fernet import Fernet
import base64

class Crypt:
    def GenerateKey():
        key = Fernet.generate_key()
        return key
    
    def Encrypt(line, key):
        fernet = Fernet(key)
        enc_line = fernet.encrypt(line.encode())
        return enc_line

    def Decrypt(line, key):
        fernet = Fernet(key)
        dec_line = fernet.decrypt(line).decode()
        return dec_line
        
    def Encrypt64(line):
        base64_bytes = base64.b64encode(line)
        base64_line = base64_bytes.decode("ascii")
        return base64_line
    
    def Decrypt64(line):
        base64_bytes = bytes(line, "ascii")
        line_bytes = base64.b64decode(base64_bytes)
        return line_bytes
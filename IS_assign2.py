import os
import base64
import getpass
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.backends import default_backend

# --- Parameters ---
SALT_SIZE = 16
NONCE_SIZE = 12
KEY_SIZE = 32
PBKDF2_ITER = 200_000

def derive_key(password: str, salt: bytes, iterations: int = PBKDF2_ITER) -> bytes:
    """Derive a symmetric key from a password and salt using PBKDF2-HMAC-SHA256."""
    password_bytes = password.encode('utf-8')
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_SIZE,
        salt=salt,
        iterations=iterations,
        backend=default_backend()
    )
    return kdf.derive(password_bytes)

def encrypt(plaintext: str, password: str) -> str:
    """Encrypt plaintext using AES-GCM. Returns Base64 string."""
    salt = os.urandom(SALT_SIZE)
    key = derive_key(password, salt)
    aesgcm = AESGCM(key)
    nonce = os.urandom(NONCE_SIZE)
    ct = aesgcm.encrypt(nonce, plaintext.encode('utf-8'), associated_data=None)
    package = salt + nonce + ct
    return base64.b64encode(package).decode('utf-8')

def decrypt(b64_package: str, password: str) -> str:
    """Decrypt a Base64 package produced by encrypt()."""
    package = base64.b64decode(b64_package)
    salt = package[:SALT_SIZE]
    nonce = package[SALT_SIZE:SALT_SIZE + NONCE_SIZE]
    ct = package[SALT_SIZE + NONCE_SIZE:]
    key = derive_key(password, salt)
    aesgcm = AESGCM(key)
    pt_bytes = aesgcm.decrypt(nonce, ct, associated_data=None)
    return pt_bytes.decode('utf-8')

# --- Menu-driven program ---
if __name__ == "__main__":
    while True:
        print("\n=== AES Encryption/Decryption Program ===")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            password = getpass.getpass("Enter password: ")
            plaintext = input("Enter text to encrypt: ")
            encrypted = encrypt(plaintext, password)
            print("\nEncrypted text (Base64):")
            print(encrypted)

        elif choice == "2":
            password = getpass.getpass("Enter password: ")
            ciphertext = input("Enter Base64 encrypted text: ")
            try:
                decrypted = decrypt(ciphertext, password)
                print("\nDecrypted text:")
                print(decrypted)
            except Exception:
                print("\nDecryption failed! Wrong password or corrupted data.")

        elif choice == "3":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

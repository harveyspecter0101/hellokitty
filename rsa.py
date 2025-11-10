from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Global variables to hold keys
private_key = None
public_key = None
ciphertext = None

def generate_keys():
    global private_key, public_key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    print("\nKeys generated successfully!")

def encrypt_message():
    global ciphertext
    if public_key is None:
        print("\nPlease generate keys first!")
        return
    message = input("\nEnter message to encrypt: ").encode()
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("\nEncrypted Message (ciphertext):", ciphertext)

def decrypt_message():
    global ciphertext
    if private_key is None:
        print("\nPlease generate keys first!")
        return
    if ciphertext is None:
        print("\nNo message encrypted yet!")
        return
    decrypted_message = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("\nDecrypted Message:", decrypted_message.decode())

# Main menu
while True:
    print("\n--- RSA Encryption Menu ---")
    print("1. Generate RSA Keys")
    print("2. Encrypt a Message")
    print("3. Decrypt a Message")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        generate_keys()
    elif choice == "2":
        encrypt_message()
    elif choice == "3":
        decrypt_message()
    elif choice == "4":
        print("\nExiting program...")
        break
    else:
        print("\nInvalid choice! Try again.")

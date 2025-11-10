from PIL import Image
from cryptography.fernet import Fernet
import numpy as np
import os

# ------------------ FUNCTION TO GENERATE AND SAVE KEY ------------------
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("\nEncryption key generated and saved as 'secret.key'")

# ------------------ FUNCTION TO LOAD EXISTING KEY ------------------
def load_key():
    if not os.path.exists("secret.key"):
        print("\nKey file not found! Please generate key first.")
        return None
    return open("secret.key", "rb").read()

# ------------------ ENCRYPT AND DECRYPT FUNCTIONS ------------------
def encrypt_watermark(watermark_text, key):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(watermark_text.encode())
    return encrypted

def decrypt_watermark(encrypted_text, key):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_text)
    return decrypted.decode()

# ------------------ EMBED WATERMARK INTO IMAGE ------------------
def embed_watermark(image_path, watermark_text, output_path):
    key = load_key()
    if key is None:
        return

    # Encrypt watermark
    encrypted_watermark = encrypt_watermark(watermark_text, key)
    watermark_bits = ''.join(format(byte, '08b') for byte in encrypted_watermark)
    watermark_length = len(watermark_bits)

    # Open image
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = np.array(img)
    flat_pixels = pixels.flatten()

    if watermark_length > len(flat_pixels):
        print("\nWatermark too large to fit in the image!")
        return

    #SAFER BITWISE OPERATION USING 254 (0b11111110)
    for i in range(watermark_length):
        flat_pixels[i] = (flat_pixels[i] & 254) | int(watermark_bits[i])

    # Save new image
    new_pixels = flat_pixels.reshape(pixels.shape)
    new_img = Image.fromarray(new_pixels.astype('uint8'))
    new_img.save(output_path)

    # Save encrypted length for easy extraction later
    with open("watermark_length.txt", "w") as f:
        f.write(str(len(encrypted_watermark)))

    print(f"\nWatermark embedded successfully in '{output_path}'")
    print(f"Encrypted watermark size: {len(encrypted_watermark)} bytes (saved in 'watermark_length.txt')")

# ------------------ EXTRACT WATERMARK FROM IMAGE ------------------
def extract_watermark(image_path):
    key = load_key()
    if key is None:
        return

    # Load saved watermark length
    if not os.path.exists("watermark_length.txt"):
        print("\nWatermark length info not found! Embed first.")
        return
    with open("watermark_length.txt", "r") as f:
        length_in_bytes = int(f.read())

    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = np.array(img).flatten()

    bits = [str(pixels[i] & 1) for i in range(length_in_bytes * 8)]
    bitstring = ''.join(bits)

    encrypted_bytes = bytes(int(bitstring[i:i+8], 2) for i in range(0, len(bitstring), 8))

    try:
        decrypted_text = decrypt_watermark(encrypted_bytes, key)
        print("\nExtracted and Decrypted Watermark:", decrypted_text)
    except Exception as e:
        print("\nDecryption failed! Ensure correct key and image.")
        print("Error:", e)

# ------------------ MAIN MENU ------------------
def main():
    while True:
        print("\n=== CRYPTOGRAPHIC IMAGE WATERMARKING SYSTEM ===")
        print("1. Generate Encryption Key")
        print("2. Embed Watermark in Image")
        print("3. Extract Watermark from Image")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            generate_key()

        elif choice == '2':
            image_path = input("\nEnter original image path (.png): ")
            watermark_text = input("Enter watermark text: ")
            output_path = input("Enter output watermarked image path: ")
            embed_watermark(image_path, watermark_text, output_path)

        elif choice == '3':
            image_path = input("\nEnter watermarked image path: ")
            extract_watermark(image_path)

        elif choice == '4':
            print("\nExiting program. Goodbye!")
            break

        else:
            print("\nInvalid choice! Please try again.")

# ------------------ RUN PROGRAM ------------------
if __name__ == "__main__":
    main()

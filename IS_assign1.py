import math

# --------------------------- PLAYFAIR CIPHER --------------------------- #
def generate_playfair_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for ch in key:
        if ch.isalpha() and ch not in used:
            matrix.append(ch)
            used.add(ch)

    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in used:
            matrix.append(ch)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]


def find_position(matrix, ch):
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == ch:
                return i, j
    return None


def playfair_encrypt(plaintext, key):
    plaintext = plaintext.upper().replace("J", "I")
    plaintext = "".join([c for c in plaintext if c.isalpha()])

    matrix = generate_playfair_matrix(key)
    pairs = []
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        b = plaintext[i + 1] if i + 1 < len(plaintext) else 'X'
        if a == b:
            b = 'X'
            i += 1
        else:
            i += 2
        pairs.append((a, b))

    ciphertext = ""
    for a, b in pairs:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:
            ciphertext += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            ciphertext += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
        else:
            ciphertext += matrix[r1][c2] + matrix[r2][c1]
    return ciphertext


def playfair_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper().replace("J", "I")
    matrix = generate_playfair_matrix(key)
    pairs = [(ciphertext[i], ciphertext[i + 1]) for i in range(0, len(ciphertext), 2)]

    plaintext = ""
    for a, b in pairs:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:
            plaintext += matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            plaintext += matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
        else:
            plaintext += matrix[r1][c2] + matrix[r2][c1]
    return plaintext


# --------------------------- VIGENERE CIPHER --------------------------- #
def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            p = ord(plaintext[i]) - 65
            k = ord(key[i % len(key)]) - 65
            c = (p + k) % 26
            ciphertext += chr(c + 65)
        else:
            ciphertext += plaintext[i]
    return ciphertext


def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            c = ord(ciphertext[i]) - 65
            k = ord(key[i % len(key)]) - 65
            p = (c - k) % 26
            plaintext += chr(p + 65)
        else:
            plaintext += ciphertext[i]
    return plaintext


# --------------------------- COLUMNAR CIPHER --------------------------- #
def columnar_encrypt(plaintext, key):
    n = len(key)
    order = sorted(range(n), key=lambda k: key[k])
    rows = math.ceil(len(plaintext) / n)
    grid = [['X'] * n for _ in range(rows)]

    idx = 0
    for r in range(rows):
        for c in range(n):
            if idx < len(plaintext):
                grid[r][c] = plaintext[idx]
                idx += 1

    ciphertext = ""
    for c in order:
        for r in range(rows):
            ciphertext += grid[r][c]
    return ciphertext


def columnar_decrypt(ciphertext, key):
    n = len(key)
    order = sorted(range(n), key=lambda k: key[k])
    rows = math.ceil(len(ciphertext) / n)
    grid = [[''] * n for _ in range(rows)]

    col_lengths = [rows] * n
    idx = 0
    for c in order:
        for r in range(rows):
            if idx < len(ciphertext):
                grid[r][c] = ciphertext[idx]
                idx += 1

    plaintext = ''.join([''.join(row) for row in grid]).rstrip('X')
    return plaintext


# --------------------------- RAIL FENCE CIPHER --------------------------- #
def rail_fence_encrypt(text, key):
    fence = [['\n' for _ in range(len(text))] for _ in range(key)]
    dir_down = False
    row, col = 0, 0

    for ch in text:
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        fence[row][col] = ch
        col += 1
        row += 1 if dir_down else -1

    result = ''
    for i in range(key):
        for j in range(len(text)):
            if fence[i][j] != '\n':
                result += fence[i][j]
    return result


def rail_fence_decrypt(cipher, key):
    fence = [['\n' for _ in range(len(cipher))] for _ in range(key)]
    dir_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        fence[row][col] = '*'
        col += 1
        row += 1 if dir_down else -1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if fence[i][j] == '*' and index < len(cipher):
                fence[i][j] = cipher[index]
                index += 1

    result = ''
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        if fence[row][col] != '\n':
            result += fence[row][col]
            col += 1
        row += 1 if dir_down else -1
    return result


# --------------------------- MAIN MENU --------------------------- #
def main():
    while True:
        print("\n==== CIPHER MENU ====")
        print("1. Playfair Cipher")
        print("2. Vigenère Cipher")
        print("3. Simple Columnar Cipher")
        print("4. Rail Fence Cipher")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '5':
            print("Exiting program.")
            break

        text = input("Enter text: ")
        key = input("Enter key: ")
        mode = input("Encrypt or Decrypt (E/D): ").upper()

        if choice == '1':
            if mode == 'E':
                print("Encrypted:", playfair_encrypt(text, key))
            else:
                print("Decrypted:", playfair_decrypt(text, key))

        elif choice == '2':
            if mode == 'E':
                print("Encrypted:", vigenere_encrypt(text, key))
            else:
                print("Decrypted:", vigenere_decrypt(text, key))

        elif choice == '3':
            if mode == 'E':
                print("Encrypted:", columnar_encrypt(text, key))
            else:
                print("Decrypted:", columnar_decrypt(text, key))

        elif choice == '4':
            key = int(key)
            if mode == 'E':
                print("Encrypted:", rail_fence_encrypt(text, key))
            else:
                print("Decrypted:", rail_fence_decrypt(text, key))
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()

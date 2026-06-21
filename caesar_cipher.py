def encrypt(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(message, shift):
    return encrypt(message, -shift)

def main():
    print("===== Caesar Cipher Tool =====")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Choose an option (1 or 2): ")

    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    if choice == "1":
        encrypted = encrypt(message, shift)
        print(f"Encrypted message: {encrypted}")
    elif choice == "2":
        decrypted = decrypt(message, shift)
        print(f"Decrypted message: {decrypted}")
    else:
        print("Invalid choice!")

main()
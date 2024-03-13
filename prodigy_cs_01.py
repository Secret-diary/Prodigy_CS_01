def caesar_cipher(text, shift, mode):
    result = ""
    if mode == 'encrypt':
        for char in text:
            if char.isalpha():
                shifted = ord(char) + shift
                if char.islower():
                    if shifted > ord('z'):
                        shifted -= 26
                elif char.isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                result += chr(shifted)
            else:
                result += char
    elif mode == 'decrypt':
        for char in text:
            if char.isalpha():
                shifted = ord(char) - shift
                if char.islower():
                    if shifted < ord('a'):
                        shifted += 26
                elif char.isupper():
                    if shifted < ord('A'):
                        shifted += 26
                result += chr(shifted)
            else:
                result += char
    return result

def main():
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    action = input("Encrypt or Decrypt? (Type 'encrypt' or 'decrypt'): ").lower()
    save_to_file = input("Do you want to save the output to a file? (yes/no): ").lower()

    if action == 'encrypt' or action == 'decrypt':
        encrypted_text = caesar_cipher(message, shift, action)
        print(f"Result: {encrypted_text}")

        if save_to_file == 'yes':
            with open("output.txt", "w") as file:
                file.write(encrypted_text)
                print("Output saved to 'encrypt.txt' in the current working directory.")
    else:
        print("Invalid input. Please choose either 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()

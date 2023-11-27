import os
from cryptography.fernet import Fernet

### configure variables here ###
## ending is the file extension added to encrypted files ##
ending = ".pycrypt"

def decrypt_directory(encrypted_directory_path, key):
    cipher_suite = Fernet(key)
    for root, _, files in os.walk(encrypted_directory_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            if file_path.endswith(ending):
                with open(file_path, 'rb') as file:
                    encrypted_data = file.read()
                decrypted_data = cipher_suite.decrypt(encrypted_data)
                with open(file_path[:-len(ending)], 'wb') as decrypted_file:
                    decrypted_file.write(decrypted_data)
                os.remove(file_path)  # Remove the encrypted file

def get_user_input():
    encrypted_directory_path = input("Enter the path to the encrypted directory: ")
    key = input("Enter the encryption key: ")
    return encrypted_directory_path, key

if __name__ == "__main__":
    encrypted_directory_path, key = get_user_input()
    decrypt_directory(encrypted_directory_path, key)

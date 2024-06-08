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


# Decrypt data using 'master_key' and store value in 'decrypted_data'. Write 'decrypted_data' to 'target'
with open(target_file, "wb") as target:
    decrypted_data = use.decrypt(data)
    target.write(decrypted_data)

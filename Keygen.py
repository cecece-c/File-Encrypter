# Import 'cryptography' library
from cryptography.fernet import Fernet


# Generate master key and store value in 'master_key' (Bytes)
master_key = Fernet.generate_key()


# Write master key to file 'masterkey.key'
with open("masterkey.key", "wb") as filekey:
    filekey.write(master_key)

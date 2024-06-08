# Import 'cryptography' library
from cryptography.fernet import Fernet


# Generate master key and store value in 'master_key_1' (Bytes)
master_key_1 = Fernet.generate_key()


# Write master key to file 'masterkey1.key'
with open("masterkey1.key", "wb") as filekey:
    filekey.write(master_key_1)

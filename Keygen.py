# Import 'cryptography' and 'time' library
from cryptography.fernet import Fernet
import time


# Generate master key and store value in 'master_key' (Bytes)
master_key = Fernet.generate_key()


# Write master key to file 'masterkey.key'
with open("masterkey.key", "wb") as filekey:
    filekey.write(master_key)


# Exit program
print("\nProgram exiting...")
for delay in range(5):
    time.sleep(1)

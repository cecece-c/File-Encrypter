# Import 'Fernet' class and 'os', 'sys', and 'time' libraries
from cryptography.fernet import Fernet
import os, sys, time


# Encrypt file
def encryption():
    # Encrypt data using 'master_key' and store value in 'encrypted_data'. Write 'encrypted_data' to 'target'
    with open(f"{current_working_directory}{target_file}", "wb") as target:
        encrypted_data = use.encrypt(data)
        target.write(encrypted_data)
        print(f"\n'{target_file}' has been encrypted.")


# Get current working directory of script and store value in 'current_working_directory' (String)
current_working_directory = os.path.dirname(sys.argv[0])
current_working_directory = current_working_directory.replace("c:", "") + "/"


# Open target file as 'target' and read data. Store value in 'data'
while True:
    try:
        target_file = input("\nTarget file:\n")
        with open(f"{current_working_directory}{target_file}", "rb") as target:
            data = target.read()
            break
    except FileNotFoundError:
        print("\nInvalid input. File not found.")


# Get and use master key. Store value in 'master_key'
try:
    with open(f"{current_working_directory}masterkey.key", "rb") as filekey:
        master_key = filekey.read()
        use = Fernet(master_key)
        encryption()
except FileNotFoundError:
    print("\nMaster key not found. Either generate master key or enter master key manually.")
    try:
        master_key = input("\nEnter master key:\n")
        use = Fernet(master_key)
        encryption()
    except TypeError:
        print("\nInvalid input.")


# Exit program
print("\nProgram exiting...")
for delay in range(5):
    time.sleep(1)

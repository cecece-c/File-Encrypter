# Import 'Fernet', 'os', 'sys' and 'time' libraries
from cryptography.fernet import Fernet
import os, sys, time


# Decrypt file
def decryption():
    # Decrypt data using 'master_key' and store value in 'decrypted_data'. Write 'decrypted_data' to 'target'
    with open(f"{current_working_directory}{target_file}", "wb") as target:
        decrypted_data = use.decrypt(data)
        target.write(decrypted_data)
        print(f"\n'{target_file}' has been decrypted.")


# Get current working directory of script and store value in 'current_working_directory' (String)
current_working_directory = os.path.dirname(sys.argv[0])
current_working_directory = current_working_directory.replace("c:", "") + "/"


# Open target file as 'target' and read data. Store value in 'data'
while True:
    try:
        target_file = input("\nTarget file: ")
        with open(f"{current_working_directory}{target_file}", "rb") as target:
            data = target.read()
            break
    except FileNotFoundError:
        print("\nInvalid input. File not found.")


# Get and use master key. Store value in 'master_key'
try:
    master_key = input("\nEnter master key: ")
    use = Fernet(master_key)
    decryption()
except TypeError:
    print("\nInvalid input.")


# Exit program
print("\nProgram exiting...")
for delay in range(5):
    time.sleep(1)

# Import 'Fernet', 'os', 'sys' and 'time' libraries
from cryptography.fernet import Fernet
import os, sys, time


# Generate master key and store value in 'master_key' (Bytes)
master_key = Fernet.generate_key()


# Get current working directory of script and store value in 'current_working_directory' (String)
current_working_directory = os.path.dirname(sys.argv[0])
current_working_directory = current_working_directory.replace("c:", "") + "/"


# Write master key to file 'masterkey.key'
with open(f"{current_working_directory}masterkey.key", "wb") as filekey:
    filekey.write(master_key)
    print(f"\nMaster key has been generated and written to {current_working_directory}masterkey.key.")


# Exit program
print("\nProgram exiting...")
for delay in range(5):
    time.sleep(1)

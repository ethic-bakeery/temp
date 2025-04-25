import os
import time

# Replace with the path to your binary file
file_path = 'procexp.exe'

if os.path.exists(file_path):
    # Get the last modification time
    mod_time = os.path.getmtime(file_path)
    
    # Convert timestamp to human-readable format
    readable_time = time.ctime(mod_time)

    print(f"File: {file_path}")
    print(f"Last modification time (timestamp): {mod_time}")
    print(f"Last modification time (readable): {readable_time}")
else:
    print("File does not exist.")

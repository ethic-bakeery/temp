import os

def disable_internet_windows(interface_name="Wi-Fi"):
    # Disable the specified network adapter
    os.system(f'netsh interface set interface "{interface_name}" admin=disabled')

# Example usage
disable_internet_windows("Wi-Fi") 
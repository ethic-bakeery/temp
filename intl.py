import os

def disable_internet():
    os.system("sudo ip route del default")

disable_internet()


import os

def disable_network_interface(interface='eth0'):
    os.system(f"sudo ifconfig {interface} down")

disable_network_interface('wlan0')  # or 'eth0'

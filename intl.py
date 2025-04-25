import os

def disable_internet():
    os.system("sudo ip route del default")

disable_internet()

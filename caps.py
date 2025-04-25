import keyboard
import time

# install keyboard with root and run script with root

def toggle_caps_lock(repeat=10, interval=0.5):
    for i in range(repeat):
        keyboard.press_and_release('caps lock')
        print(f"Toggled Caps Lock: {i + 1}")
        time.sleep(interval)

# Example: toggle 10 times every 0.5 seconds
toggle_caps_lock(repeat=10, interval=0.5)

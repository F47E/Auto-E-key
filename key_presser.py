import tkinter as tk
from pynput.keyboard import Controller
import threading
import time

class KeyPresser:
    def __init__(self):
        self.pressing = False
        self.keyboard = Controller()

    def start_pressing(self):
        self.pressing = True
        self.press_key()

    def stop_pressing(self):
        self.pressing = False

    def press_key(self):
        while self.pressing:
            self.keyboard.press('e')
            self.keyboard.release('e')
            time.sleep(0.1)  # Adjust the delay as needed

def start_pressing_key():
    if not key_presser.pressing:
        threading.Thread(target=key_presser.start_pressing).start()

def stop_pressing_key():
    key_presser.stop_pressing()

key_presser = KeyPresser()

root = tk.Tk()
root.title("Key Presser")

start_button = tk.Button(root, text="Start", command=start_pressing_key)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop", command=stop_pressing_key)
stop_button.pack(pady=10)

root.mainloop()

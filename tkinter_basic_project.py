import numpy as np
import math
import time
import numpy as np
import time

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter Example")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)

# Create a button widget
def on_button_click():
    label.config(text="Button clicked!")

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

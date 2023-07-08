from rembg import remove 
from PIL import Image
import tkinter as tk
from tkinter import filedialog


def open_file_dialog():
    # Create the file dialog
    file_path = filedialog.askopenfilename()

    # Display the selected file path in the console
    print("Selected file:", file_path)
    # output_path = "output_"+file_path.split(".jpg")[0]+".png"
    name = file_path.split("/")[-1]
    output_path = "output_"+name.split(".jpg")[0]+".png"
    # output_path = "output.png"

    Input = Image.open(file_path)
    output = remove(Input)
    output.save(output_path)



# Create the Tkinter window
window = tk.Tk()

# Create a button to open the file dialog
button = tk.Button(window, text="Open File", command=open_file_dialog)
button.pack()

# Start the Tkinter event loop
window.mainloop()


# input_path = "trex-hardbg.jpg"

# output_path = "output_"+input_path.split(".jpg")[0]+".png"

# Input = Image.open(input_path)
# output = remove(Input)
# output.save(output_path)
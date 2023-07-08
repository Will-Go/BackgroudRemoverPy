from rembg import remove
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog


# Para que el ancho sea proporcional a la altura
def propor_y(x, img):
    return int((x / float(img.width)) * img.height)


def open_file_dialog():
    # Create the file dialog
    file_path = filedialog.askopenfilename()
    if not (file_path == "" or file_path is None):
        # Cambiar el label1 por la ruta elegida
        label1.config(text=file_path)

        # Ajustamos el tamaño de la imagen
        img1 = Image.open(file_path)
        x = 250
        y = propor_y(x, img1)
        resized_img1 = img1.resize((x, y))

        # Ponemos la imagen1 en la Mainwindow
        tk_img1 = ImageTk.PhotoImage(resized_img1)
        image1.config(image=tk_img1)
        image1.image = tk_img1

        # Display the selected file path in the console
        print("Selected file:", file_path)

        name = file_path.split("/")[-1]
        output_path = "output_"+name.split(".jpg")[0]+".png"

        Input = Image.open(file_path)
        output = remove(Input)
        output.save(output_path)

        print("Finalizado")

        resized_img2 = output.resize((x, y))

        # Ponemos la imagen2 en la Mainwindow
        tk_img2 = ImageTk.PhotoImage(resized_img2)

        image2.config(image=tk_img2)
        image2.image = tk_img2


window = tk.Tk()

window.title("Background Romover")
# Boton para ingresar el archivo
button = tk.Button(window, text="Eleguir Archivo", command=open_file_dialog)
button.pack()
label1 = tk.Label(window, text="")
label1.pack()

frame = tk.Frame(window)
frame.pack()

# img1 = Image.open("output_cat.png")
# img2 = Image.open("output_trex-hardbg.png")

# x, y = 150, 150

# resized_img1 = img1.resize((x, y))
# resized_img2 = img2.resize((x, y))

# tk_img1 = ImageTk.PhotoImage(resized_img1)
# tk_img2 = ImageTk.PhotoImage(resized_img2)

image1 = tk.Label(frame)
image1.grid(row=0, column=0)
image2 = tk.Label(frame)
image2.grid(row=0, column=1)

window.mainloop()


# input_path = "trex-hardbg.jpg"

# output_path = "output_"+input_path.split(".jpg")[0]+".png"

# Input = Image.open(input_path)
# output = remove(Input)
# output.save(output_path)

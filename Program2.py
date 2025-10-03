import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog, Button
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ImageApp:
    def __init__(fall, main):
        fall.main = main
        fall.main.title("My Photo")
        fall.frame1 = tk.Frame(main)
        fall.frame1.grid(row=0, column=0, padx=5, pady=5)
        fall.gambar1 = plt.Figure(figsize=(5, 4), dpi=50) 
        fall.sumbu1 = fall.gambar1.add_subplot(111)
        fall.kanvas1 = FigureCanvasTkAgg(fall.gambar1, master=fall.frame1)
        fall.kanvas1.get_tk_widget().pack(side=tk.TOP)

        fall.open_button1 = Button(fall.frame1, text="Open", command=fall.open_image)
        fall.open_button1.pack(side=tk.BOTTOM)

        fall.frame2 = tk.Frame(main)
        fall.frame2.grid(row=0, column=1, padx=5, pady=5)

        fall.gambar2 = plt.Figure(figsize=(5, 4), dpi=50)
        fall.sumbu2 = fall.gambar2.add_subplot(111)
        fall.kanvas2 = FigureCanvasTkAgg(fall.gambar2, master=fall.frame2)
        fall.kanvas2.get_tk_widget().pack(side=tk.TOP)

        fall.process_button = Button(fall.frame2, text="Proses", command=fall.process_image)
        fall.process_button.pack(side=tk.BOTTOM)

        fall.frame3 = tk.Frame(main)
        fall.frame3.grid(row=0, column=2, padx=5, pady=5)

        fall.gambar3 = plt.Figure(figsize=(5, 4), dpi=50)
        fall.sumbu3 = fall.gambar3.add_subplot(111)
        fall.kanvas3 = FigureCanvasTkAgg(fall.gambar3, master=fall.frame3)
        fall.kanvas3.get_tk_widget().pack(side=tk.TOP)

        fall.biner_button = Button(fall.frame3, text="Biner", command=fall.display_binary)
        fall.biner_button.pack(side=tk.BOTTOM)

        fall.frame4 = tk.Frame(main)
        fall.frame4.grid(row=0, column=3, padx=5, pady=5)

        fall.gambar4 = plt.Figure(figsize=(5, 4), dpi=50) 
        fall.sumbu4 = fall.gambar4.add_subplot(111)
        fall.kanvas4 = FigureCanvasTkAgg(fall.gambar4, master=fall.frame4)
        fall.kanvas4.get_tk_widget().pack(side=tk.TOP)

        fall.histogram_button = Button(fall.frame4, text="Histogram", command=fall.display_histogram)
        fall.histogram_button.pack(side=tk.BOTTOM)

    def open_image(fall):
        file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            fall.my_image = Image.open(file_path)
            fall.display_original()

    def display_original(fall):
        fall.sumbu1.imshow(fall.my_image)
        fall.kanvas1.draw()

    def process_image(fall):
        fall.my_image_gray = fall.my_image.convert('L')
        fall.sumbu2.imshow(fall.my_image_gray, cmap='gray')
        fall.kanvas2.draw()

    def display_binary(fall):
        threshold = 128
        fall.gambar_biner = fall.my_image_gray.point(lambda p: 255 if p > threshold else 0)
        fall.sumbu3.imshow(fall.gambar_biner, cmap='gray')
        fall.kanvas3.draw()

    def display_histogram(fall):
        gambar_array = np.array(fall.my_image_gray)
        a, b = gambar_array.shape
        data = gambar_array.reshape(a * b)
        angka, jumlah_angka = np.unique(data, return_counts=True)
        total = a * b
        H1 = jumlah_angka / total

        fall.sumbu4.clear()
        fall.sumbu4.bar(angka, H1, color='gray')
        fall.sumbu4.set_title('Histogram')
        fall.sumbu4.set_xlim([0, 255])
        fall.kanvas4.draw()
if __name__ == "__main__":
    main = tk.Tk()
    app = ImageApp(main)
    main.mainloop()
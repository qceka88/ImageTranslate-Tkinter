import tkinter as tk
from tkinter import filedialog, ttk


class ImageTextTranslator:

    def __init__(self):
        self.interface = tk.Tk()
        self.interface_window_style()
        self.interface.mainloop()

    def interface_window_style(self):
        self.interface.geometry('500x300')
        self.interface.title('Image Text Translation')
        self.interface.maxsize(1920, 1080)
        self.interface.minsize(1024, 768)
        self.interface['bg'] = 'white'
        self.button = ttk.Button(self.interface, text="Upload Image", command=self.file_open)
        self.button.grid(column=1, row=1)
        self.button = ttk.Button(self.interface, text="Save Text", command=self.file_save)
        self.button.grid(column=100, row=100)

    def file_open(self):
        self.file = filedialog.askopenfilename()

    def file_save(self):
        self.file = filedialog.asksaveasfile()



if __name__ == '__main__':
    ImageTextTranslator()

import tkinter as tk
from tkinter import filedialog, ttk

from text_extraction import TextExtractor


# TODO: Implement spaghetti code logic in nice UI/UX

# TODO: Add boxes for source language and target language
# TODO: fix file save function, to save extracted text
# TODO: add option for user to "Straigth" tilt images
# TODO: if user not select "Straight" option, program should directly start extracting of text

class ImageTextTranslator:

    def __init__(self):
        self.interface = tk.Tk()
        self.interface_window()
        self.interface.mainloop()

    def interface_window(self):
        self.interface.geometry('500x300')
        self.interface.title('Image Text Translation')
        self.interface.maxsize(1920, 1080)
        self.interface.minsize(1024, 768)
        self.interface['bg'] = 'white'
        self.original_image = None
        self.button = ttk.Button(self.interface, text="Upload Image", command=self.Upload_image)
        self.button.grid(column=150, row=1)

        self.button = ttk.Button(self.interface, text="Extract Text", command=self.Extract_text)
        self.button.grid(column=150, row=250)

    def Upload_image(self):
        self.original_image = filedialog.askopenfilename()

    def File_save(self):
        self.file = filedialog.asksaveasfile()

    def Extract_text(self):
        extracted_text = TextExtractor(self.original_image)

        def Result_window():
            self.text_window = tk.Toplevel()
            self.text_window.geometry("1024x768")
            self.text_window.title('Extracted Text')
            self.button = ttk.Button(self.text_window, text="Save Text", command=self.File_save)
            self.button.grid(column=1, row=1)

            self.text_window.mainloop()

        Result_window()


if __name__ == '__main__':
    ImageTextTranslator()

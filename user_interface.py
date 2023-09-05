import tkinter as tk
from tkinter import filedialog, ttk
from tkinter import scrolledtext as sk

from text_extraction import TextExtractor
from text_translation import Translate


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
        self.interface.minsize(700, 400)
        self.interface['bg'] = 'white'
        self.original_image = None
        self.text_translated = ''
        self.button = ttk.Button(self.interface, text="Upload Image", command=self.Upload_image)
        self.button.grid(column=1, row=1)

        self.button = ttk.Button(self.interface, text="Extract Text", command=self.Extract_text)
        self.button.grid(column=2, row=1)

    def Upload_image(self):
        self.original_image = filedialog.askopenfilename()

    def file_save(self):
        self.file = filedialog.asksaveasfile()

    def Extract_text(self):
        self.extracted_text = TextExtractor(self.original_image)

        def Result_window():
            def TranslationActivate():
                self.extracted_text = self.text.get('0.1', tk.END)
                self.text_translated = Translate(self.extracted_text, target='bg')

                self.translated_text = sk.ScrolledText(self.result_windows, height=25, width=50, borderwidth=4, relief=tk.SUNKEN,)
                self.translated_text.insert(tk.END, str(self.text_translated))
                self.translated_text.grid(column=4, row=2)

                self.result_windows.mainloop()

            self.result_windows = tk.Toplevel()
            self.result_windows.geometry("1000x600")
            self.result_windows.title('Extracted Text')
            self.result_windows['bg'] = '#FCFCFC'
            self.style_strap1 = tk.Label(self.result_windows, bg='#FCFCFC', height=5, width=10)
            self.style_strap1.grid(column=1, row=1)

            self.button = ttk.Button(self.result_windows, text="SAVE TEXT", command=self.file_save)
            self.button.grid(column=4, row=3)

            self.label_original_text = tk.Label(self.result_windows,
                                                text=f'ORIGINAL TEXT: EN',
                                                font=('verdana', 12, 'bold'),
                                                bg="#FCFCFC",
                                                )
            self.label_original_text.grid(column=2, row=1)

            self.text = sk.ScrolledText(self.result_windows, height=25, width=50, borderwidth=4, relief=tk.SUNKEN,)
            self.text.insert(tk.END, str(self.extracted_text))
            self.text.grid(column=2, row=2)

            self.style_strap2 = tk.Label(self.result_windows, bg='#FCFCFC', height=5, width=5)
            self.style_strap2.grid(column=3, row=1)

            self.label_translated_text = tk.Label(self.result_windows,
                                                  text=f'TRANSLATED TEXT: BG',
                                                  font=('verdana', 12, 'bold'),
                                                  bg="#FCFCFC",
                                                  )
            self.label_translated_text.grid(column=4, row=1)

            self.translated_text = sk.ScrolledText(self.result_windows, height=25, width=50)
            self.translated_text.insert(tk.END, str(self.text_translated))
            self.translated_text.grid(column=4, row=2)

            self.button = ttk.Button(self.result_windows, text="Translate", command=TranslationActivate)
            self.button.grid(column=2, row=3)

            self.interface.mainloop()

        Result_window()


if __name__ == '__main__':
    ImageTextTranslator()

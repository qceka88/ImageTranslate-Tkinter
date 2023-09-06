import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext as sk

import cv2
import imutils
from docx import Document

from text_extraction import TextExtractor
from text_translation import TranslateText


# TODO: Implement spaghetti code logic in nice UI/UX


# TODO: add option for user to "Straigth" tilt images
# TODO: if user not select "Straight" option, program should directly start extracting of text

class ImageTextTranslator:

    def __init__(self):
        self.interface = tk.Tk()
        self.interface_main_window()
        self.original_image = None
        self.text_translated = ''
        self.interface.mainloop()

    def interface_main_window(self):
        self.interface.geometry('500x300')
        self.interface.title('Image Text Translation')
        self.interface.maxsize(1920, 1080)
        self.interface.minsize(740, 700)
        self.interface['bg'] = '#FCFCFC'

        self.header = tk.Label(self.interface, text="TEXT FROM IMAGE TRANSLATOR", font=('verdana', 22, 'bold')
                               , fg="#DC143C", bg="white")
        self.header.grid(column=2, row=1)

        self.style_strap1 = tk.Label(self.interface, bg='#FCFCFC', height=5, width=5)
        self.style_strap1.grid(column=1, row=1)

        def ImageProcessing():
            self.frame_images = tk.LabelFrame(self.interface, text="IMAGE PROCESSING", width=640, height=250,
                                              font=('verdana', 12, 'bold'),
                                              borderwidth=3, relief=tk.SUNKEN, highlightthickness=4, bg="#F5F5F5",
                                              highlightcolor="white", highlightbackground="white", fg="#191970")
            self.frame_images.grid(column=2, row=2)

            self.upload_button = tk.Button(self.frame_images, width=20, fg='red', bg='#CDC9C9',
                                           text="UPLOAD", command=self.UploadImage)
            self.upload_button.place(x=50, y=15)
            self.upload_frame_description = tk.LabelFrame(self.frame_images, width=180, height=40)
            self.upload_frame_description.place(x=30, y=55)
            self.description_upload = tk.Label(self.upload_frame_description,
                                               text='\nYOU CAN UPLOAD.'
                                                    '\nPART OF TEXT AS IMAGE '
                                                    '\nOR PICTURE FORM PHONE ON'
                                                    '\nA WHOLE SHEET AND START'
                                                    '\nEXTRACTING TEXT. IF IMAGE OF'
                                                    '\nSHEET IS NOT STRAIGHT YOU'
                                                    '\nCAN USE TRANSFORM BUTTON.\n',
                                               highlightcolor='white', bg='white')
            self.description_upload.grid(column=1, row=1)

            self.transform_button = tk.Button(self.frame_images, width=20, fg='red', bg='#CDC9C9',
                                              text="TRANSFORM", command=self.TransformImage)
            self.transform_button.place(x=250, y=15)

            self.transform_frame_description = tk.LabelFrame(self.frame_images, width=180, height=40)
            self.transform_frame_description.place(x=230, y=55)
            self.description_transform = tk.Label(self.transform_frame_description,
                                                  text='\nEXPECT POP-UP WINDOW.'
                                                       '\nIF RED DOTS ARE NOT'
                                                       '\n RIGHT IN CORNERS OF SHEET. '
                                                       '\nPLEASE UPLOAD NEW IMAGE'
                                                       '\nFOR BETTER TRANSLATION'
                                                       '\nCORNERS SHOULD BE VISIBLE\n',
                                                  highlightcolor='white', bg='white')
            self.description_transform.grid(column=1, row=1)

            self.check_image_button = tk.Button(self.frame_images, width=20, fg='red', bg='#CDC9C9',
                                                text="CHECK IMAGE", command=self.CheckImage)
            self.check_image_button.place(x=450, y=15)

            self.check_image_frame_description = tk.LabelFrame(self.frame_images, width=180, height=40)
            self.check_image_frame_description.place(x=430, y=55)
            self.description_check_image = tk.Label(self.check_image_frame_description,
                                                    text='\nWITH CHECK IMAGE BUTTON.'
                                                         '\nYOU CAN SEE YOUR IMAGE.'
                                                         '\nBEFORE TRANSFORMATION'
                                                         '\nAND AFTER TRANSFORMATION.'
                                                         '\nIF USE THIS FUNCTION\n',
                                                    highlightcolor='white', bg='white')
            self.description_check_image.grid(column=1, row=1)

        def TextProcessing():
            self.frame_text = tk.LabelFrame(self.interface, text=" TEXT PROCESSING", width=640, height=250,
                                            font=('verdana', 12, 'bold'),
                                            borderwidth=3, relief=tk.SUNKEN, highlightthickness=4, bg="#F5F5F5",
                                            highlightcolor="white", highlightbackground="white", fg="#191970")
            self.frame_text.grid(column=2, row=3)
            # TODO: check for can place a gray text in placeholder
            self.source_language = tk.Entry(self.frame_text, width=25, borderwidth=1, relief=tk.SUNKEN, bg="white")
            self.source_language.insert(0, 'Enter Source Language'.upper())
            self.source_language.place(x=50, y=15)
            # TODO: check for can place a gray text in placeholder
            self.target_language = tk.Entry(self.frame_text, width=25, borderwidth=1, relief=tk.SUNKEN, bg="white")
            self.target_language.insert(0, 'Enter Target Language'.upper())
            self.target_language.place(x=250, y=15)

            self.extract_button = tk.Button(self.frame_text, width=20, fg='red', bg='#CDC9C9',
                                            text="EXTRACT TEXT", command=self.Extract_text)
            self.extract_button.place(x=450, y=15)

        ImageProcessing()
        TextProcessing()

    def UploadImage(self):
        self.original_image = filedialog.askopenfilename()

    def TransformImage(self):
        if self.original_image:
            ...
        else:
            self.message = messagebox.showerror('No Image Uploaded',
                                                'Please upload image!')

    def CheckImage(self):
        if self.original_image:
            read_image = cv2.imread(self.original_image)
            if read_image.shape[0] > 700:
                read_image = imutils.resize(read_image, height=600)
            cv2.imshow('Current Image', read_image)

        else:
            self.message = messagebox.showerror('No Image Uploaded',
                                                'Please upload image!')

    def FileSave(self):
        file_types = (
            ('TextFile', '*.txt'),
            ('Word2003', '*.doc'),
            ('Word2007', '*.docx'),
        )
        self.output_file = filedialog.asksaveasfile(filetypes=file_types,
                                                    defaultextension='*.txt',
                                                    confirmoverwrite=True,
                                                    )

        if self.output_file:
            file_data = self.output_file.name.split('/')
            path = '\\'.join(file_data[0:len(file_data) - 1]) + '\\'
            file_name = file_data[-1]
            file_extension = file_name.split('.')[-1]
            if file_extension in ['doc', 'docx']:
                doc_object = Document()
                doc_object.add_paragraph(self.text_translated)
                doc_object.save(path + file_name)

            else:
                with open(path + file_name, 'w') as file:
                    file.write(self.text_translated)

        self.interface.mainloop()

    def Extract_text(self):
        if self.original_image:
            self.extracted_text = TextExtractor(self.original_image,
                                                source_language='en',
                                                ).__str__()

            def Result_window():
                def TranslationActivate():
                    self.extracted_text = self.original_text_box.get('0.1', tk.END)
                    self.text_translated = TranslateText(
                        self.extracted_text,
                        target_language='en',
                        source_language='en',
                    ).__str__()

                    self.translated_text_box = sk.ScrolledText(
                        self.result_windows,
                        height=25,
                        width=50,
                        borderwidth=4,
                        relief=tk.SUNKEN,
                    )
                    self.translated_text_box.insert(tk.END, self.text_translated)
                    self.translated_text_box.grid(column=4, row=2)

                    self.text_translated = self.translated_text_box.get('0.1', tk.END)
                    self.result_windows.mainloop()

                """" 
                CREATE SECOND WINDOWS SECTION 
                """
                self.result_windows = tk.Toplevel()
                self.result_windows.geometry("1000x600")
                self.result_windows.title('Extracted Text')
                self.result_windows['bg'] = '#F5F5F5'

                self.style_strap3 = tk.Label(self.result_windows, bg='#F5F5F5', height=5, width=10)
                self.style_strap3.grid(column=1, row=1)

                self.style_strap4 = tk.Label(self.result_windows, bg='#F5F5F5', height=5, width=5)
                self.style_strap4.grid(column=3, row=1)

                """" 
                ORIGINAL TEXT SECTION 
                """
                self.label_original_text = tk.Label(
                    self.result_windows,
                    text=f'ORIGINAL TEXT: EN',
                    font=('verdana', 12, 'bold'),
                    bg="#F5F5F5",
                )
                self.label_original_text.grid(column=2, row=1)

                self.original_text_box = sk.ScrolledText(
                    self.result_windows,
                    height=25,
                    width=50,
                    borderwidth=4,
                    relief=tk.SUNKEN,
                )
                self.original_text_box.insert(tk.END, self.extracted_text)
                self.original_text_box.grid(column=2, row=2)

                self.translate_button = tk.Button(self.result_windows, width=20, fg='red', bg='#CDC9C9',
                                                  text="TRANSLATE", command=TranslationActivate)
                self.translate_button.grid(column=2, row=3)

                """" 
                TRANSLATED TEXT SECTION 
                """
                self.label_translated_text = tk.Label(
                    self.result_windows,
                    text=f'TRANSLATED TEXT: BG',
                    font=('verdana', 12, 'bold'),
                    bg="#F5F5F5",
                )
                self.label_translated_text.grid(column=4, row=1)

                self.translated_text_box = sk.ScrolledText(
                    self.result_windows,
                    height=25,
                    width=50,
                    borderwidth=4,
                    relief=tk.SUNKEN,
                )
                self.translated_text_box.insert(tk.END, self.text_translated)
                self.translated_text_box.grid(column=4, row=2)

                self.save_button = tk.Button(self.result_windows, width=20, fg='red', bg='#CDC9C9',
                                             text="SAVE TEXT", command=self.FileSave)
                self.save_button.grid(column=4, row=3)

                self.interface.mainloop()

            Result_window()

        else:
            self.message = messagebox.showerror('No Image Uploaded',
                                                'Please upload image!')


if __name__ == '__main__':
    ImageTextTranslator()

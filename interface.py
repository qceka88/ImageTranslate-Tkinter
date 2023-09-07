import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import scrolledtext as sk

import cv2
import imutils
from docx import Document

from error_messages import error_for_missing_image, error_for_wrong_iso_language_code
from image_transform import ImageTransform
from placeholders import focus_in_input_box, focus_out_input_box
from regex_validation import input_data_regex_validation
from text_extraction import TextExtractor
from text_translation import TranslateText


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

        def ImageProcessingMenu():
            """
                        :return: Buttons for image processing with explanations
            """
            self.frame_images = tk.LabelFrame(self.interface, text="IMAGE PROCESSING", width=640, height=280,
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
                                               highlightcolor='white', bg='#fff3f3')
            self.description_upload.grid(column=1, row=1)

            self.transform_button = tk.Button(self.frame_images, width=20, fg='red', bg='#CDC9C9',
                                              text="TRANSFORM", command=self.TransformImage)
            self.transform_button.place(x=250, y=15)

            self.transform_frame_description = tk.LabelFrame(self.frame_images, width=180, height=40)
            self.transform_frame_description.place(x=230, y=55)
            self.description_transform = tk.Label(self.transform_frame_description,
                                                  text='\n!CORNERS SHOULD BE VISIBLE!\n'
                                                       '\nEXPECT POP-UP WINDOW.'
                                                       '\nIF RED DOTS  NOT MATCH'
                                                       '\n CORNERS OF SHEET. '
                                                       '\nPLEASE UPLOAD NEW IMAGE'
                                                       '\nFOR BETTER TRANSLATION\n'
                                                  ,
                                                  highlightcolor='white', bg='#fff3f3')
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
                                                         '\nIF IMAGE NOT LOOK GOOD'
                                                         '\nAFTER TRANSFORMATION.'
                                                         '\nUPLOAD NEW IMAGE\n',
                                                    highlightcolor='white', bg='#fff3f3')
            self.description_check_image.grid(column=1, row=1)

        def TextProcessingMenu():
            """
                        :return: Button and input fields for text processing
            """
            self.frame_text = tk.LabelFrame(self.interface, text=" TEXT PROCESSING", width=640, height=280,
                                            font=('verdana', 12, 'bold'),
                                            borderwidth=3, relief=tk.SUNKEN, highlightthickness=4, bg="#F5F5F5",
                                            highlightcolor="white", highlightbackground="white", fg="#191970")
            self.frame_text.grid(column=2, row=3)
            self.placeholder_source_language = 'ENTER SOURCE LANGUAGE'
            self.source_language_input = tk.Entry(self.frame_text, width=25, borderwidth=1,
                                                  relief=tk.SUNKEN, bg="white", fg='gray')
            self.source_language_input.insert(0, self.placeholder_source_language)
            self.source_language_input.bind("<FocusIn>",
                                            lambda args: focus_in_input_box(self.source_language_input))
            self.source_language_input.bind("<FocusOut>",
                                            lambda args: focus_out_input_box(self.source_language_input,
                                                                             self.placeholder_source_language))
            self.source_language_input.pack()
            self.source_language_input.place(x=50, y=15)

            self.placeholder_target_language = 'ENTER TARGET LANGUAGE'
            self.target_language_input = tk.Entry(self.frame_text, width=25, borderwidth=1,
                                                  relief=tk.SUNKEN, bg="white", fg='gray')
            self.target_language_input.insert(0, self.placeholder_target_language)
            self.target_language_input.bind("<FocusIn>",
                                            lambda args: focus_in_input_box(self.target_language_input))
            self.target_language_input.bind("<FocusOut>",
                                            lambda args: focus_out_input_box(self.target_language_input,
                                                                             self.placeholder_target_language))
            self.target_language_input.pack()
            self.target_language_input.place(x=250, y=15)

            self.languages_frame_description = tk.LabelFrame(self.frame_text, width=180, height=40)
            self.languages_frame_description.place(x=30, y=55)

            self.description_languages = tk.Label(self.languages_frame_description,
                                                  text='\n---> CASE INSENSITIVE <---'
                                                       '\nFOR SOURCE LANGUAGE AND TARGET LANGUAGE, USER SHOULD USE '
                                                       '\nISO-STANDARD FOR ABBREVIATION FORM:'
                                                       '\nISO 639-1 STANDARD LANGUAGE CODES'
                                                       '\nE.G.'
                                                       '\nFOR BULGARIAN: BG -- FOR ENGLISH: EN -- FOR FRANCE: FR'
                                                       '\n      -----   WARNING    ----'
                                                       '\nIT IS POSSIBLE TO ENTER AN VALID INPUT LANGUAGE FORMAT'
                                                       '\nBUT IT NOT SUPPORTED IN OCR AND TRANSLATION MODULE\n',
                                                  highlightcolor='white', bg='#fff3f3')
            self.description_languages.grid(column=1, row=1)

            self.extract_button = tk.Button(self.frame_text, width=20, fg='red', bg='#CDC9C9',
                                            text="EXTRACT TEXT", command=self.Extract_text)
            self.extract_button.place(x=450, y=15)

            self.extract_text_frame_description = tk.LabelFrame(self.frame_text, width=180, height=40)
            self.extract_text_frame_description.place(x=430, y=55)
            self.description_extract_text = tk.Label(self.extract_text_frame_description,
                                                     text='\nAFTER CLICK EXTRACT TEXT'
                                                          '\nBE PATIENT'
                                                          '\nAFTER FEW MOMENTS'
                                                          '\nSECOND SCREEN WILL APPEAR'
                                                          '\nWITH ORIGINAL AND'
                                                          '\nEXTRACTED TEXT'
                                                          '\nENJOY\n',
                                                     highlightcolor='white', bg='#fff3f3')
            self.description_extract_text.grid(column=1, row=1)

        ImageProcessingMenu()
        TextProcessingMenu()
        self.interface.mainloop()

    def UploadImage(self):
        """
                    :return: This comments is pointless,
                     but this function allow to user to upload image.
        """
        self.original_image = filedialog.askopenfilename()

    def TransformImage(self):
        """
                    :return: Proceed image transformation from tilt image to straight image.
                    The real magic is hidden in image_transformation.py
        """
        if self.original_image is not None:
            try:
                new_image = ImageTransform(self.original_image).return_result()
                self.original_image = new_image
            except TypeError:
                messagebox.showerror('Problem with corners',
                                     'Program cannot detect corners!\n'
                                     'Please upload new image!\n'
                                     'Ensure that the corners are clearly visible!')

        else:
            error_for_missing_image()

    def CheckImage(self):
        """
            :return: Here User can check current status of image
        """
        if self.original_image is not None:
            try:
                read_image = cv2.imread(self.original_image)
            except TypeError:
                read_image = self.original_image

            if read_image.shape[0] > 700:
                read_image = imutils.resize(read_image, height=600)

            cv2.imshow('Current Image', read_image)
        else:
            error_for_missing_image()

    def FileSave(self):
        """
                    :return: Saving of translated text in file. User chan choose
                    from 'file_type' what kind of file to save
        """
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
        """
                    :return: If input data is OK and image is OK, program start
                    extracting text procedure
        """
        source_language = input_data_regex_validation(self.source_language_input.get())
        target_language = input_data_regex_validation(self.target_language_input.get())

        if not source_language:
            error_for_wrong_iso_language_code('Language Source')
        elif not target_language:
            error_for_wrong_iso_language_code('Language Target')
        elif self.original_image is None:
            error_for_missing_image()
        else:
            self.extracted_text = TextExtractor(self.original_image,
                                                source_language=source_language,
                                                ).__str__()

            def Result_window():

                """
                  :return: CREATE SECOND WINDOWS SECTION WITH RESULT
                """

                def TranslationActivate():
                    """
                                :return: User can modify already extracted text.
                                User can modify translated text or,
                                just to continue with file saving.
                    """
                    self.extracted_text = self.original_text_box.get('0.1', tk.END)
                    self.text_translated = TranslateText(
                        self.extracted_text,
                        target_language=target_language,
                        source_language=source_language,
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

                self.result_windows = tk.Toplevel()
                self.result_windows.geometry("1000x600")
                self.result_windows.title('Extracted Text')
                self.result_windows['bg'] = '#F5F5F5'

                self.style_strap3 = tk.Label(self.result_windows, bg='#F5F5F5', height=5, width=10)
                self.style_strap3.grid(column=1, row=1)

                self.style_strap4 = tk.Label(self.result_windows, bg='#F5F5F5', height=5, width=5)
                self.style_strap4.grid(column=3, row=1)

                """
                ORIGINAL TEXT SECTION 
                """
                self.label_original_text = tk.Label(
                    self.result_windows,
                    text=f'ORIGINAL TEXT: {source_language}'.upper(),
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

                """
                TRANSLATED TEXT SECTION 
                """
                self.label_translated_text = tk.Label(
                    self.result_windows,
                    text=f'TRANSLATED TEXT: {target_language}'.upper(),
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


if __name__ == '__main__':
    ImageTextTranslator()

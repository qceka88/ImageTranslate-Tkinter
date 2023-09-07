from tkinter import messagebox


def error_for_missing_image():
    message = messagebox.showerror('No Image Uploaded',
                                   'Please upload image!')
    return message


def error_for_wrong_iso_language_code(field):
    message = messagebox.showerror(f'Error in {field} ',
                                   f'Field {field} is not correct!')
    return message

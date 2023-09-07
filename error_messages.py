from tkinter import messagebox


def error_for_missing_image():
    message = messagebox.showerror('No Image Uploaded',
                                   'Please upload image!')
    return message


def error_for_wrong_iso_language_code(field):
    message = messagebox.showerror(f'Error in {field} ',
                                   f'Field {field} is not correct!')
    return message

def opencv_cant_find_corners_of_paper_sheet():
    messagebox.showerror('Problem with corners',
                         'Program cannot detect corners!\n'
                         'Please upload new image!\n'
                         'Ensure that the corners are clearly visible!')
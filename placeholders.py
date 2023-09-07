import tkinter as tk


def focus_out_input_box(widget, widget_text):
    if widget['fg'] == 'black' and len(widget.get()) == 0:
        widget.delete(0, tk.END)
        widget['fg'] = 'gray'
        widget.insert(0, widget_text)


def focus_in_input_box(widget):
    if widget['fg'] == 'gray':
        widget['fg'] = 'black'
        widget.delete(0, tk.END)

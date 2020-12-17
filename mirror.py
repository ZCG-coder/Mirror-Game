#!python3
#!coding=utf8
"""
mirror.py - the mirror program.
"""
from tkinter import *
from PIL import Image
import sys

while True:
    try:
        file_dir = input('Please specify the file path: [quit to exit]')
        if file_dir == 'quit':
            sys.exit(0)
        img = Image.open(file_dir)  # Open the new image.
        img.thumbnail((900, 900))  # Resize it.
        img.save('temp0.gif')  # Save it.

        w, h = img.size  # Get the size.
        win1 = Tk()
        win1.geometry('%sx%s' % (w * 2, h))  # Set the size to (2w x h)
        win1.title('MainWindow')

        cv1 = Canvas(win1)
        cv1.pack(fill='both', expand=1)
        image = PhotoImage(file='temp0.gif')
        cv1.create_image(0, 0, anchor=NW, image=image)

        img1 = Image.open('temp0.gif')
        img1.transpose(Image.FLIP_LEFT_RIGHT).save('temp1.gif')

        image2 = PhotoImage(file='temp1.gif')
        cv1.create_image(w, 0, anchor=NW, image=image2)

        cv1.create_line(w, 0, w, h, fill='blue')

        mainloop()
    except Exception as e:
        print(f'Exception happened. {str(e).title()}')


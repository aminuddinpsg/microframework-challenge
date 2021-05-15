import os
from os import path

PIC_DIR = os.path.join(os.getcwd(), 'img')

def initApp():
    # create pics dir
    if not path.exists(PIC_DIR):
        os.mkdir(PIC_DIR)


        
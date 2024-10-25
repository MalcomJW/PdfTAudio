import pypdf
import pyttsx3

import os

# * reps importing all
from tkinter.filedialog import *
from pydub import AudioSegment

book = askopenfilename()


pdfreader = pypdf.PdfReader(book)

pages = pdfreader.get_num_pages()



for num in range(0, pages):
    page = pdfreader.get_page(num)
    #extracting text from PDf
    text = page.extract_text()

    player = pyttsx3.init()

    player.say(text)

    player.runAndWait()
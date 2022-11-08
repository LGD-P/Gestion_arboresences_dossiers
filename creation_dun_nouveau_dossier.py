from tkinter import *
from tkinter.filedialog import askdirectory
from pathlib import Path
import shutil



# We initialize paths we will use

path = Path().cwd()
fond_de_dossier = Path().cwd()
fond_de_dossier = Path(fond_de_dossier / "fond de dossier")


def where_to_creat_file():
    """get path where to creat folder then creat floder"""
    filename = askdirectory()
    where = Path(f"{filename}/{first_entry.get()}")
    print(where)
    shutil.copytree(fond_de_dossier, where)


def done():
    """creat green frame 'c'est fait' after creation"""
    label_done = Label(frame, text="C'est Fait",
                       font=("JetBrains Mono", 15), bg="#54f91f",
                       fg="#0c0b0b").pack()


# Window settings
window = Tk()
window.title("Création de Fichiers")
window.geometry("500x400")
window.minsize(500, 400)
window.config(background='#33beff')
window.iconbitmap(Path(path / "test_ico.ico"))
window.attributes("-alpha", 0.80)

# Window Frame

frame = Frame(window, bg='#33beff', bd=1, )


# Text in window


label_title = Label(frame, text="Entrez le nom du dossier \n "
                                "remplacez '/' par '-' \n ",
                    font=("JetBrains Mono", 15), bg="#33beff", fg="#0c0b0b")
label_title.pack()

frame.pack(expand=YES)  # centre frame and text in mddle of the box


first_entry = Entry(frame, font=("JetBrains Mono", 15), bg="#eb3008",
                    fg="#0c0b0b", text="")
first_entry.pack()

# SET BUTTON

button_location = Button(frame, text="Où doit on créer le dossier ?",
                         font=("JetBrains Mono", 12), bg="#33beff",
                         fg="#0c0b0b",
                         command=lambda: (where_to_creat_file(), done()))

button_location.pack()

window.mainloop()



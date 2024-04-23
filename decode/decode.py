# pip install googletrans==3.1.0a0
from googletrans import Translator
from gtts import gTTS
from tkinter import *

window = Tk()
window.title("Decode!Make It Easy")
window.iconbitmap('E:\\365\\decode_logo.ico')
window.geometry('705x400')
window.config(bg="black")
set_bg = PhotoImage(file="E:\\365\\decode_bg.png")

label_1 = Label(window,image=set_bg)
label_1.place(x=0, y=0)


e1 = Entry(window,bg="black",fg="white",font=("Arial",25,"bold"))
e1.place(x=30,y=20)

def convert_language():
    a1 = e1.get()
    t1 = Translator()
    t2 = click_option.get()

    if t2 == "English":
        convert = "en"
    elif t2 == "Hindi":
        convert ="hi"
    elif t2 == "German":
        convert = "de"
    elif t2 =="French":
        convert = "fr"
    elif t2 == "Spanish":
        convert = "es"
    elif t2 == "Russian":
        convert = "ru"
    elif t2 == "Korean":
        convert = "ko"
    elif t2 == "Japanese":
        convert = "ja"
    elif t2 == "Arabic":
        convert = "ar"


    trans_text = t1.translate(a1, dest = convert)
    trans_text = trans_text.text
    ob1 = gTTS(text = trans_text, slow=False, lang = convert)
    label_2.config(text=trans_text)

choices = [
    "Arabic",
    "English",
    "French",
    "German",
    "Hindi",
    "Japanese",
    "Korean",
    "Spanish",
    "Russian",
]

click_option = StringVar()
click_option.set("Select Language")

list_drop = OptionMenu(window, click_option, *choices)
list_drop.configure(background="green", foreground="white", font=('Arial',16,"bold"))
list_drop.place(x=420,y=20)

label_2 = Label(window, text="\t\t\t\t\t   ", bg="black", fg="white", font=("Arial",20,"bold"))
label_2.place(x=30, y=120)
label_2 = Label(window, text="Translated text",bg="black",fg="White",font=("Arial",20,))
label_2.place(x=150,y=120)

Button_1 = Button(window, text="Translate",bg="red",fg="white",font=("Arial",25,"bold"),command=convert_language)
Button_1.place(x=265,y=172)

window.mainloop()


#!/usr/bin/python3
#coding:utf-8

from tkinter import *
#import tkinter as tk
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import os
import shutil

BUTTONPADX = 25
BUTTONPADY = 5
imagePath = "9OPjrDeBWQCEm9XbzAw7TNTXWQHNE4ETLpfYoXTwekg.jpg"
folderPath = "C:\\Users\\ramic\\Pictures\\Saved Pictures"
completePath = "C:\\Users\\ramic\\Pictures\\Saved Pictures\\eden.png"

window = Tk()

window.title("Snow Labeler")

window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)

#configure rows and columns
window.rowconfigure(0, minsize=400, weight=1)
window.rowconfigure(1, minsize=100, weight=1)
window.columnconfigure(0, minsize=300, weight=1)
window.columnconfigure(1, minsize=100, weight=1)



#frames
fr_labelButtons = Frame(window) #frame for labelButtons
fr_navDes = Frame(window) #frame to chose image to display
#image = tk.Frame(window)
image = Image.open(imagePath)
image = image.resize((200,200), Image.NEAREST)
photo = ImageTk.PhotoImage(image)
myListbox = Listbox(fr_navDes)
text_dir = Text(fr_navDes, wrap=WORD, height=1, width = 50)


#function for choosing the dir
def openFolder():
    global folderPath
    folderPath =  filedialog.askdirectory()
    list = os.listdir(folderPath)
    myListbox.delete(1, END)
    for item in list:
        myListbox.insert(END, item)
    updateTextBox(folderPath)

def onselect(event):
    w = event.widget
    idx = int(w.curselection()[0])
    imagePath = w.get(idx)
    global completePath
    completePath = folderPath + "/" + imagePath
    updateImage(completePath)

def moveFile(source, destination):
    #check if source is already there
    print(source, "->", destination )
    #if not (os.path.exists(destination)):
        #print("ok")
    #check if destination exists
    if not (os.path.exists(destination)):
        os.makedirs(destination)
    shutil.move(source, destination)

#updating the layout
def updateTextBox(text):
    text_dir.delete('1.0',END)
    text_dir.insert(END,text)
    text_dir.config(wrap=WORD)

def updateImage(path):
    image = Image.open(path)
    image = image.resize((200,200), Image.NEAREST)
    photo = ImageTk.PhotoImage(image)
    imageLabel = Label(image = photo)
    imageLabel.image = photo
    imageLabel.grid(row=0, column=1, sticky="nsew", padx=25, pady=5)

myListbox.bind('<<ListboxSelect>>', onselect)

#widgets
#for amount of Snow
btn_label_0 = Button(fr_labelButtons, text="0% (X)", command =lambda: moveFile(completePath, (folderPath + "/class0")))
btn_label_10 = Button(fr_labelButtons, text="10% (1)", command =lambda: moveFile(completePath, (folderPath + "/class10")))
btn_label_20 = Button(fr_labelButtons, text="20% (2)", command =lambda: moveFile(completePath, (folderPath + "/class20")))
btn_label_30 = Button(fr_labelButtons, text="30% (3)", command =lambda: moveFile(completePath, (folderPath + "/class30")))
btn_label_40 = Button(fr_labelButtons, text="40% (4)", command =lambda: moveFile(completePath, (folderPath + "/class40")))
btn_label_50 = Button(fr_labelButtons, text="50% (5)", command =lambda: moveFile(completePath, (folderPath + "/class50")))
btn_label_60 = Button(fr_labelButtons, text="60% (6)", command =lambda: moveFile(completePath, (folderPath + "/class60")))
btn_label_70 = Button(fr_labelButtons, text="70% (7)", command =lambda: moveFile(completePath, (folderPath + "/class70")))
btn_label_80 = Button(fr_labelButtons, text="80% (8)", command =lambda: moveFile(completePath, (folderPath + "/class80")))
btn_label_90 = Button(fr_labelButtons, text="90% (9)", command =lambda: moveFile(completePath, (folderPath + "/class90")))
btn_label_100 =Button(fr_labelButtons, text="100% (0)", command =lambda: moveFile(completePath, (folderPath + "/class100")))
#binding keys
window.bind('x', lambda event: moveFile(completePath, (folderPath + "/class0")))
window.bind('1', lambda event: moveFile(completePath, (folderPath + "/class10")))
window.bind('2', lambda event: moveFile(completePath, (folderPath + "/class20")))
window.bind('3', lambda event: moveFile(completePath, (folderPath + "/class30")))
window.bind('4', lambda event: moveFile(completePath, (folderPath + "/class40")))
window.bind('5', lambda event: moveFile(completePath, (folderPath + "/class50")))
window.bind('6', lambda event: moveFile(completePath, (folderPath + "/class60")))
window.bind('7', lambda event: moveFile(completePath, (folderPath + "/class70")))
window.bind('8', lambda event: moveFile(completePath, (folderPath + "/class80")))
window.bind('9', lambda event: moveFile(completePath, (folderPath + "/class90")))
window.bind('0', lambda event: moveFile(completePath, (folderPath + "/class100")))


#for image
imageLabel = Label(image = photo)
imageLabel.image = photo

#for choosing the image
btn_choose_dir = Button(fr_navDes, text = "Choose Folder: (Q)", command=openFolder)
window.bind('q', lambda event: openFolder())



#grid layout
#for labeling the image
fr_labelButtons.grid(row=1, column=1, sticky="ns")
btn_label_0.grid(row=1, column=0, sticky="ew", padx=BUTTONPADX, pady=BUTTONPADY)
btn_label_10.grid(row=1, column=1, sticky="ew", padx=BUTTONPADX, pady=BUTTONPADY)
btn_label_20.grid(row=1, column=2, sticky="ew", padx=BUTTONPADX, pady=BUTTONPADY)
btn_label_30.grid(row=1, column=3, sticky="ew", padx=BUTTONPADX, pady=BUTTONPADY)
btn_label_40.grid(row=1, column=4, sticky="ew", padx=BUTTONPADX, pady=BUTTONPADY)
btn_label_50.grid(row=1, column=5, sticky="ew", padx=BUTTONPADX, pady=BUTTONPADY)
btn_label_60.grid(row=1, column=6, sticky="ew", padx=BUTTONPADX, pady=BUTTONPADY)
btn_label_70.grid(row=1, column=7, sticky="ew", padx=BUTTONPADX, pady=BUTTONPADY)
btn_label_80.grid(row=1, column=8, sticky="ew", padx=BUTTONPADX, pady=BUTTONPADY)
btn_label_90.grid(row=1, column=9, sticky="ew", padx=BUTTONPADX, pady=BUTTONPADY)
btn_label_100.grid(row=1, column=10, sticky="ew", padx=BUTTONPADX, pady=BUTTONPADY)

#for choosing the image
fr_navDes.grid(row=0, column=0, sticky="ns")
btn_choose_dir.grid(row=2,column=0, sticky = "ew", padx=25, pady=5)
myListbox.grid(row=1,column=0, padx=BUTTONPADX, pady=BUTTONPADY)
text_dir.grid(row=0, column=0, padx=BUTTONPADX, pady=BUTTONPADY)

#show the image
imageLabel.grid(row=0, column=1, sticky="nsew", padx=25, pady=5)


window.mainloop()

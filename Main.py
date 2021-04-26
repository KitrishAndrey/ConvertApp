from subprocess import Popen
from tkinter import *
from tkinter import scrolledtext
import os
import time

print("Program Started")

root = Tk()
counter = 0

root.title(u'Convert_app')
root.geometry('700x500+700+400')# ширина=300, высота=150, x=300, y=200
root.iconname("Convert_App")

label = Label(root, text="Folder Path", height=1, width=20)
label2 = Text(root,  height=1, width=30, font='Arial 14', wrap=WORD)
folder_path = Text(root, height=1, width=50, font='Arial 14', wrap=WORD)
conv_button = Button(root, text="Convert", width=30, height=5, bg="white", fg="black")
txtbox = scrolledtext.ScrolledText(width=70, height=10)

class Video_Audio_Convertation:

    def convertation(self, file):
        destination = "Ready_Vidios"
        newfilename = "{}.mp4".format(time.time())
        args = ["ffmpeg", "-i", file, "-vcodec", "copy", "-acodec", "copy", os.path.join(destination, newfilename)]
        process = Popen(args)
        process.wait()

def convertfunc(file):
    video = Video_Audio_Convertation()
    video.convertation(file)

def getnameoffolder():
    name_of_ = folder_path.get(1.0, END)
    return r"{}".format(name_of_)

def create_new_folder():
    os.mkdir("Ready_Vidios")

def main(event):
    try:
        global counter, label2
        if os.path.exists("Ready_Vidios"):
            path1 = getnameoffolder()
            file_list = os.listdir(
                r"{}".format(path1[:-1]))  # список файлов и папок в директории, где запущена программа
            txtbox.insert(INSERT, "\n".join(file_list))
            for f in file_list:
                counter += 1
                convertfunc(os.path.join(r"{}".format(path1[:-1]), f))
            print("Successfully Converted")
            label2.delete('1.0', END)
            label2.insert(INSERT, " Arrage of converted files:{}".format(counter))


        if not os.path.exists("Ready_Vidios"):
            create_new_folder()
            path1 = getnameoffolder()
            file_list = os.listdir(r"{}".format(path1[:-1]))  # список файлов и папок в директории, где запущена программа
            txtbox.insert(INSERT, "\n".join(file_list))
            for f in file_list:
                counter += 1
                convertfunc(os.path.join(r"{}".format(path1[:-1]), f))
            print("Successfully Converted")
            label2.delete('1.0', END)
            label2.insert(INSERT, " Arrage of converted files:{}".format(counter))
    except Exception as e:
        print(repr(e))

conv_button.bind("<Button-1>", main) #при нажатии ЛКМ на кнопку вызывается функция main


label.pack(side=TOP, pady=10)
folder_path.pack(side=TOP, padx=5, pady=50)
label2.pack(padx=5, pady=10)
txtbox.pack()
conv_button.pack(padx=3, pady=30)
root.iconbitmap("Convphoto.ico")
root.mainloop()

from subprocess import Popen
from tkinter import *
import os

print("Program Started")
#path = r"C:\Users\User\Desktop\Files" # path of folder with files to convert for test

root = Tk()

root.title(u'Convert_app')
root.geometry('500x400+700+300')# ширина=300, высота=150, x=300, y=200
root.iconname("Convert_App")

label = Label(root, text="Folder Path", height=1, width=20)
folder_path = Text(root, height=1, width=30, font='Arial 14', wrap=WORD)
conv_button = Button(root, text="Convert", width=30, height=5, bg="white", fg="black")

class Video_Audio_Convertation:

    def convertation(self, file, counter):
        destination = "Ready_Vidios"
        newfilename = "{}.mp4".format(counter)
        args = ["ffmpeg", "-i", file, "-vcodec", "copy", "-acodec", "copy", os.path.join(destination, newfilename)]
        process = Popen(args)
        process.wait()

def convertfunc(file, counter):
    video = Video_Audio_Convertation()
    video.convertation(file, counter)

def getnameoffolder():
    name_of_ = folder_path.get(1.0, END)
    return r"{}".format(name_of_)

def create_new_folder():
    os.mkdir("Ready_Vidios")

counter = 0
def main(event):
    global counter
    if counter != 0 and os.path.exists("Ready_Vidios"):
        counter = counter
        path = getnameoffolder()
        file_list = os.listdir(r"{}".format(path[:-1]))  # список файлов и папок в директории, где запущена программа
        for f in file_list:
            counter += 1
            convertfunc(os.path.join(r"{}".format(path[:-1]), f), counter)
        print("Successfully Converted")
    else:
        create_new_folder()
        path = getnameoffolder()
        file_list = os.listdir(r"{}".format(path[:-1]))  # список файлов и папок в директории, где запущена программа
        for f in file_list:
            counter += 1
            convertfunc(os.path.join(r"{}".format(path[:-1]), f), counter)
            print("Successfully Converted")

conv_button.bind("<Button-1>", main) #при нажатии ЛКМ на кнопку вызывается функция main

label.pack(side=TOP, pady=10)
folder_path.pack(side=TOP, padx=5, pady=50)
conv_button.pack(padx=3, pady=30)
root.iconbitmap("Convphoto.ico")
root.mainloop()

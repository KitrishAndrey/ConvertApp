import eel
from subprocess import Popen
import os
import time

counter = 0

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

def getnameoffolder(folder_path):
    name_of_ = folder_path
    return r"{}".format(name_of_)

def create_new_folder():
    os.mkdir("Ready_Vidios")

@eel.expose
def ConvertMainFunc(folder_path):
    try:
        txtlisttosend = None
        global counter
        if os.path.exists("Ready_Vidios"):
            path1 = getnameoffolder(folder_path)
            filespath = r"{}".format(path1)
            file_list = os.listdir(filespath)# список файлов и папок в директории, где запущена программа
            txtlisttosend = "\n".join(file_list)
            for f in file_list:
                counter += 1
                convertfunc(os.path.join(r"{}".format(path1), f))

        if not os.path.exists("Ready_Vidios"):
            create_new_folder()
            path1 = getnameoffolder(folder_path)
            filespath = r"{}".format(path1)
            file_list = os.listdir(filespath)  # список файлов и папок в директории, где запущена программа
            txtlisttosend = "\n".join(file_list)
            for f in file_list:
                counter += 1
                convertfunc(os.path.join(r"{}".format(path1), f))
        return txtlisttosend
    except Exception as e:
        print(repr(e))

@eel.expose
def GetCounter():
    return counter

eel.init("web")
eel.start("main.html", size=(705, 706))

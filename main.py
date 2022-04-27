import tkinter as tk
from tkinter import filedialog as fd
import youtube_dl
import moviepy as mp


def start():
    urlget = urlentry.get()
    if urlget == "":
        print("Not a valid URL")
        pass
    else:
        urlget = str(urlentry.get())
        formatget = str(selected.get())
        rateget = str(rateselected.get())
        print("Selected URL: ", urlget)
        print("Selected Format: ", formatget)
        print("Selected Rate Limit: ", rateget, "Bytes/s")
        ydl_opts = {
            'outtmpl': 'c:/tmp/%(title)s.%(ext)s',
            'format': formatget,
            'ratelimit': rateget,
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([urlget])

def callback():
    file = fd.askopenfilename()
    print("Selected File:",file)
    clip = mp.VideoFileClip(str(file))
    clip.audio.write_audiofile(file)

mainwindow = tk.Tk()
mainwindow.geometry("475x330")
mainwindow.resizable(0, 0)
mainwindow.title("Jake's Youtube Downloader")
# mainwindow.iconbitmap("icon.ico")   # BROKEN WHEN CONVERTED TO EXE FOR SOME REASON

formats = [
    "mp4",
    "webm",
    "mkv",
    "mov",
    "m4a",
    "avi",
    "wmf",
    "flv",
    "mp3",
    "ogg",
    "aac",
    "wav",
]

rateoptions = [
    "5000000000",
    "2000000000",
    "1000000000",
    "500000000",
    "250000000",
    "100000000",
    "10000000",
    "1000000",
]


selected = tk.StringVar(mainwindow)
selected.set("Format")

converterselected = tk.StringVar(mainwindow)
converterselected.set("Format")

rateselected = tk.StringVar(mainwindow)
rateselected.set("Ratelimit")

# Downloader GUI

downloaderlabelframe = tk.LabelFrame(mainwindow, text="Downloader", bg="grey94", width=465, height=140)
urllabel = tk.Label(mainwindow, fg="black", text="Url:")
urlentry = tk.Entry(mainwindow, fg="black", bg="white", width=50)
startbutton = tk.Button(mainwindow, text="Start", width=10, height=3, bg="grey94", fg="black", command=start)
formatselection = tk.OptionMenu(mainwindow, selected, *formats,)
rateselection = tk.OptionMenu(mainwindow, rateselected, *rateoptions,)

# Converter GUI

converterlabelframe = tk.LabelFrame(mainwindow, text="Converter", bg="grey94", width=250, height=180)
openfilebutton = tk.Button(mainwindow, text="select file", bg="grey94", fg="black",width=10, height=2, command=callback)
converterformatselection = tk.OptionMenu(mainwindow, converterselected, *formats,)


# Other GUI

pluglabel = tk.Label(mainwindow, text="I Have A Twitch Channel And\n Dontation Link At linktr.ee/britishspuds")

downloaderlabelframe.place(x=5, y=5)
converterlabelframe.place(x=5, y=145)
pluglabel.place(x=260, y=155)
urllabel.place(x=15, y=25)
urlentry.place(x=50, y=25)
startbutton.place(x=375, y=25)
formatselection.place(x=15, y=55)
rateselection.place(x=100, y=55)
openfilebutton.place(x=15, y=165)
converterformatselection.place(x=13, y=210)


mainwindow.mainloop()

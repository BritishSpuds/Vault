import tkinter as tk
from tkinter import filedialog as fd
import youtube_dl


def start():
    urlget = urlentry.get()
    if urlget == "":
        print("Not a valid URL")
        pass
    else:
        urlget = str(urlentry.get())
        formatget = str(selected.get())
        rateget = str(rateselected.get())
        ratemb = 10000000
        if rateget == "1gb/s":
            ratemb = 1000000000
        elif rateget == "500mb/s":
            ratemb = 500000000
        elif rateget == "250mb/s":
            ratemb = 250000000
        elif rateget == "100mb/s":
            ratemb = 100000000
        elif rateget == "10mb/s":
            ratemb = 10000000
        elif rateget == "1mb/s":
            ratemb = 1000000
        else:
            print("Shorten Error")
        print("Selected URL: ", urlget)
        print("Selected Format: ", formatget)
        print("Selected Rate Limit: ", ratemb, "(", rateget, ")", "Bytes/s")
        ydl_opts = {
                    'outtmpl': 'c:/tmp/%(title)s.%(ext)s',
                    'format': formatget,
                    'limitrate': ratemb,
                    }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([urlget])


def callback():
    file = str(fd.askopenfilename())
    print("Selected File:", file)
    directoryentry.delete(0, "end")
    directoryentry.insert(string=file, index=0)


def formathelpwindow():
    tkhelpwindow = tk.Tk()
    tkhelpwindow.geometry("375x140")
    tkhelpwindow.resizable(0, 0)
    tkhelpwindow.title("Help")
    tkhelpwindow.iconbitmap("icon.ico")   # BROKEN WHEN CONVERTED TO EXE FOR SOME REASON

    downloaderhelplabelframe = tk.LabelFrame(tkhelpwindow, text="Formats",  bg="grey94", width=365, height=130)

    downloaderhelp = tk.Label(tkhelpwindow, text="Format is the extention on the end of the file. This converter\n"
                                                 "supports: Mp4, Webp and M4a. Mp4 can be used if you want your\n"
                                                 "file to be downloaded with video and audio included. Webp can\n"
                                                 "be used if you want your file to be downloaded with video but\n"
                                                 "without audio. M4a can be used if you just want to download\n"
                                                 "your file with audio. Any can be used.\n")
    downloaderhelp.place(x=10, y=20)
    downloaderhelplabelframe.place(x=5, y=5)


mainwindow = tk.Tk()
mainwindow.geometry("475x330")
mainwindow.resizable(0, 0)
mainwindow.title("Jake's Youtube Downloader")
mainwindow.iconbitmap("icon.ico")   # BROKEN WHEN CONVERTED TO EXE FOR SOME REASON


formats = [
    "mp4",
    "webm",
    "m4a",
]

rateoptions = [
    "1gb/s",
    "500mb/s",
    "250mb/s",
    "100mb/s",
    "10mb/s",
    "1mb/s",
]


selected = tk.StringVar(mainwindow)
selected.set(formats[0])

converterselected = tk.StringVar(mainwindow)
converterselected.set(formats[0])

rateselected = tk.StringVar(mainwindow)
rateselected.set(rateoptions[4])

# - MAIN WINDOW - #

# Downloader GUI

downloaderlabelframe = tk.LabelFrame(mainwindow, text="Downloader", bg="grey94", width=465, height=140)
urllabel = tk.Label(mainwindow, fg="black", text="Url:")
urlentry = tk.Entry(mainwindow, fg="black", bg="white", width=50)
startbutton = tk.Button(mainwindow, text="Start", width=10, height=3, bg="grey94", fg="black", command=start)
helpbutton = tk.Button(mainwindow, text="Help", width=8, height=1, bg="grey94", fg="black", command=formathelpwindow)
formatselection = tk.OptionMenu(mainwindow, selected, *formats,)
rateselection = tk.OptionMenu(mainwindow, rateselected, *rateoptions,)

# Converter GUI

converterlabelframe = tk.LabelFrame(mainwindow, text="Converter", bg="grey94", width=250, height=180)
openfilebutton = tk.Button(mainwindow, text="select file", bg="grey94", fg="black", width=10, height=2,
                           command=callback)
converterformatselection = tk.OptionMenu(mainwindow, converterselected, *formats,)
directoryentry = tk.Entry(mainwindow, fg="black", bg="white", width=22)

# Other GUI

pluglabel = tk.Label(mainwindow, text="I Have A Twitch Channel And\n"
                                      "Dontation Link At\n"
                                      "linktr.ee/britishspuds\n"
                                      "if you're feeling generous.")

# - HELP WINDOW - #

# Downloader Help

downloaderlabelframe.place(x=5, y=5)
converterlabelframe.place(x=5, y=145)
pluglabel.place(x=280, y=155)
urllabel.place(x=15, y=25)
urlentry.place(x=50, y=25)
startbutton.place(x=375, y=25)
helpbutton.place(x=15, y=95)
formatselection.place(x=15, y=55)
rateselection.place(x=100, y=55)
openfilebutton.place(x=15, y=165)
converterformatselection.place(x=13, y=210)
directoryentry.place(x=105, y=165)


mainwindow.mainloop()

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import youtube_dl
import pyautogui

size = pyautogui.size() # Get screen size
screenwidthx = size[0] # Give the variable "screenwidthx" the horizontal pixel count
screenwidthy = size[1] # Give the variable "screenwidthy" the verical pixel count

print(screenwidthx,"x",screenwidthy) # prints the horizontal and vertical pixel count seperated by an x

def startdownloader():
    urlget = urlentry.get()
    if urlget == "":
        print("Not a valid URL")
        pass
    else:
        urlget = str(urlentry.get())
        formatget = str(selected.get())
        rateget = str(rateselected.get())
        ratemb = 10000000
        if rateget == "1gb/s": # converts values like '1gb/s' into 1000000000, whch is 1gb in singular bytes.
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
        print("Selected URL: ", urlget) # print useful info into the console
        print("Selected Format: ", formatget)
        print("Selected Rate Limit: ", ratemb, "(", rateget, ")", "Bytes/s")
        ydl_opts = { # options for downloading the video
                    'outtmpl': 'c:/tmp/%(title)s.%(ext)s',
                    'format': formatget,
                    'limitrate': ratemb,
                    }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl: # with the options in "ydl_opts"...
            ydl.download([urlget]) # download the url in "urlget"


def openfile(): # opens the file manager to select a file when called
    file = str(filedialog.askopenfilename()) # opens file manager and waits for a file to be selected before putting the directory into the variable "file"
    print("Selected File:", file)
    directoryentry.delete(0, "end") # deletes whats currently in the "directoryentry"
    directoryentry.insert(string=file, index=0) # adds the new directory into "directoryentry"


def startconverter(): # converts the file when called
    pass # not finished


mainwindow = tk.Tk()
mainwindow.geometry("475x330")
mainwindow.resizable(0, 0)
mainwindow.title("Jake's Youtube Downloader")
# mainwindow.iconbitmap("icon.ico")   # BROKEN WHEN CONVERTED TO EXE FOR SOME REASON
tabControl = ttk.Notebook(mainwindow)

DownloaderTab = ttk.Frame(tabControl)
ConverterTab = ttk.Frame(tabControl)
CalculatorTab = ttk.Frame(tabControl)
AutoclickerTab = ttk.Frame(tabControl)
AutoDownloaderTab = ttk.Frame(tabControl)
FileArchiverTab = ttk.Frame(tabControl)
VideoPlayerTab = ttk.Frame(tabControl)
MusicPlayerTab = ttk.Frame(tabControl)
HelpTab = ttk.Frame(tabControl)
CreditsTab = ttk.Frame(tabControl)

tabControl.add(DownloaderTab, text="Downloader")
tabControl.add(ConverterTab, text="Converter")
tabControl.add(CalculatorTab, text="Calculator")
tabControl.add(AutoclickerTab, text="Autoclicker")
tabControl.add(AutoDownloaderTab, text="Auto Downloader")
tabControl.add(FileArchiverTab, text="File Archiver")
tabControl.add(VideoPlayerTab, text="Video Player")
tabControl.add(MusicPlayerTab, text="Music Player")
tabControl.add(HelpTab, text="Help")
tabControl.add(CreditsTab, text="Credits")


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

# Downloader Tab

downloaderlabelframe = tk.LabelFrame(DownloaderTab, text="Downloader", bg="grey94", width=460, height=300)
urllabel = tk.Label(DownloaderTab, fg="black", text="Url:")
urlentry = tk.Entry(DownloaderTab, fg="black", bg="white", width=50)
startdownloader = tk.Button(DownloaderTab, text="Start\nDownload", width=10, height=3, bg="grey94", fg="black", command=startdownloader)
formatselection = tk.OptionMenu(DownloaderTab, selected, *formats,)
rateselection = tk.OptionMenu(DownloaderTab, rateselected, *rateoptions)

# Converter Tab

converterlabelframe = tk.LabelFrame(ConverterTab, text="Converter", bg="grey94", width=460, height=300)
openfilebutton = tk.Button(ConverterTab, text="select file", bg="grey94", fg="black", width=10, height=2, command=openfile)
converterformatselection = tk.OptionMenu(ConverterTab, converterselected, *formats)
directoryentry = tk.Entry(ConverterTab, fg="black", bg="white", width=46)
directorylabel = tk.Label(ConverterTab, fg="black", bg="grey94", text="Directory:")
startconverter = tk.Button(ConverterTab, text="Start\nConverter", width=10, height=3, bg="grey94", fg="black", command=startconverter)

# Autoclicker Tab

autoclickerlabelframe = tk.LabelFrame(AutoclickerTab, text="Autoclicker", bg="grey94", width=460, height=300)

# Auto Downloader

autodownloaderlabelframe = tk.LabelFrame(AutoDownloaderTab, text="Auto Downloader", bg="grey94", width=460, height=300)

# File Archiver Tab

filearchiverlabelframe = tk.LabelFrame(FileArchiverTab, text="File Archiver", bg="grey94", width=460, height=300)

# Video Player Tab

videoplayerlabelframe = tk.LabelFrame(VideoPlayerTab, text="Video Player", bg="grey94", width=460, height=300)

# Music Player Tab

musicplayerlabelframe = tk.LabelFrame(MusicPlayerTab, text="Music Player", bg="grey94", width=460, height=300)

# Help Tab

helplabelframe = tk.LabelFrame(HelpTab, text="Help", bg="grey94", width=460, height=300)
helplabel = tk.Label(HelpTab, fg="black", bg="grey94", text="I will eventually put some helpful text here :)")

# Credits tab

creditslabelframe = tk.LabelFrame(CreditsTab, text="Credits", bg="grey94", width=460, height=300)
creditslabel = tk.Label(CreditsTab, fg="black", bg="grey94", text="I will eventually put some credits here :)")

tabControl.pack(expand=1, fill="both")
downloaderlabelframe.place(x=5, y=0)
converterlabelframe.place(x=5, y=0)
autoclickerlabelframe.place(x=5, y=0)
helplabelframe.place(x=5, y=0)
creditslabelframe.place(x=5, y=0)
urllabel.place(x=15, y=25)
urlentry.place(x=50, y=25)
startdownloader.place(x=370, y=25)
formatselection.place(x=15, y=55)
rateselection.place(x=100, y=55)
openfilebutton.place(x=15, y=60)
converterformatselection.place(x=15, y=105)
directoryentry.place(x=74, y=25)
directorylabel.place(x=15, y=25)
startconverter.place(x=370, y=25)
helplabel.place(x=15, y=15)
creditslabel.place(x=15, y=15)


mainwindow.mainloop()

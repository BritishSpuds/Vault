import tkinter as tk
import youtube_dl


def start():
    urlget = urlentry.get()
    formatget = str(selected.get())
    print("Selected URL: ", urlget)
    print("Selected Format: ", formatget)
    ydl_opts = {
        'outtmpl': 'c:/tmp/%(title)s.%(ext)s',
        'format': formatget,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([urlget])


mainwindow = tk.Tk()
mainwindow.geometry("475x330")
mainwindow.resizable(0, 0)
mainwindow.title("Jake's Youtube Downloader")
# mainwindow.iconbitmap("icon.ico")   # BROKEN WHEN CONVERTED TO EXE FOR SOME REASON


options = [
    "mp4",
    "webm",
    "mkv",
    "mov",
    "mp3",
    "ogg",
]

selected = tk.StringVar(mainwindow)
selected.set(options[0])

downloaderlabelframe = tk.LabelFrame(mainwindow, text="Downloader", bg="grey94", width=465, height=90)
converterlabelframe = tk.LabelFrame(mainwindow, text="Converter", bg="grey94", width=250, height=230)
wiplabel = tk.Label(mainwindow, text="This Section Is Currently Work In Progress.")
brokenlabel = tk.Label(mainwindow, text="Format Selection Is Currently Broken. (mp4 Only)")
pluglabel = tk.Label(mainwindow, text="I Have A Twitch Channel\n And Dontation Link At\n linktr.ee/britishspuds")
urllabel = tk.Label(mainwindow, fg="black", text="Url:")
urlentry = tk.Entry(mainwindow, fg="black", bg="white", width=50)
startbutton = tk.Button(mainwindow, text="Start", width=10, height=3, bg="white", fg="black", command=start)
formatselection = tk.OptionMenu(mainwindow, selected, *options, )

downloaderlabelframe.place(x=5, y=5)
converterlabelframe.place(x=5, y=95)
wiplabel.place(x=15, y=110)
brokenlabel.place(x=90, y=60)
pluglabel.place(x=290, y=110)
urllabel.place(x=15, y=25)
urlentry.place(x=50, y=25)
startbutton.place(x=375, y=25)
formatselection.place(x=15, y=55)

mainwindow.mainloop()

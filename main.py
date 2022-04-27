import tkinter as tk
import youtube_dl as ydl


def start():
    urlget = str(urlentry.get())
    formatget = str(selected.get())
    rateget = int(rateselected.get())
    print("Selected URL: ", urlget)
    print("Selected Format: ", formatget)
    print("Selected Rate Limit: ", rateget, "Bytes/s")
    ydl_opts = {
        'outtmpl': 'c:/tmp/%(title)s.%(ext)s'--restrict-filenames,
        'format': formatget,
        'ratelimit': rateget,
    }
    with ydl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([urlget])


mainwindow = tk.Tk()
mainwindow.geometry("475x330")
mainwindow.resizable(0, 0)
mainwindow.title("Jake's Youtube Downloader")
# mainwindow.iconbitmap("icon.ico")  # BROKEN WHEN CONVERTED TO EXE FOR SOME REASON

downloadlocationwindow = tk.Tk()
downloadlocationwindow.geometry("120x90")
downloadlocationwindow.resizable(0, 0)
downloadlocationwindow.title("Jake's Youtube Downloader")


options = [
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
ratelimitselection = tk.OptionMenu(mainwindow, rateselected, *rateoptions, )

downloaderlabelframe.place(x=5, y=5)
converterlabelframe.place(x=5, y=95)
wiplabel.place(x=15, y=110)
brokenlabel.place(x=90, y=60)
pluglabel.place(x=290, y=110)
urllabel.place(x=15, y=25)
urlentry.place(x=50, y=25)
startbutton.place(x=375, y=25)
formatselection.place(x=15, y=55)
ratelimitselection.place(x=15, y=105)

mainwindow.mainloop()

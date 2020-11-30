# Imports #
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import filedialog
import random
import threading
import pafy

# Root #
root = Tk()
root.title("JAK YouTube Video/Audio Downloader")
root.geometry('780x500')
root.configure(bg="olivedrab1")
root.resizable(False, False)
root.iconbitmap('youtube.ico')

# Global Variable #
urltext = StringVar()
colors = ['red', 'green', 'yellow', 'pink', 'blue', 'gold']
downloadIndex = 0

# Functions #
def getvideo():
    list_Box.delete(0, END)
    url = urltext.get()
    data = pafy.new(url)
    streams = data.allstreams
    index = 0
    for i in streams:
        du = '{:0.1f}'.format(i.get_filesize()//(1024*1024))
        datas = str(index) + '.'.ljust(3, ' ') + str(i.quality).ljust(10, ' ') + str(i.extension).ljust(5, ' ') + str(i.mediatype) + ' ' + du.rjust(10, ' ') + 'MB'
        list_Box.insert(END, datas)
        index += 1

def VideoURL():
    DownloadingBarTextLabel.configure(text='')
    DownloadingRecievedLabelResult.configure(text='')
    DownloadingSizeLabelResult.configure(text='')
    DownloadingTimeLabelResult.configure(text='')
    get_detail = threading.Thread(target=getvideo)
    get_detail.start()

def SelectCursor(evt):
    global downloadIndex
    list_Box_Data = list_Box.get(list_Box.curselection())
    print(list_Box_Data)
    downloadStream = list_Box_Data[:3]
    downloadIndex = int(''.join(x for x in downloadStream if x.isdigit()))

def DownloadVideoData():
    global downloadIndex
    fgr = filedialog.askdirectory()
    DownloadingBarTextLabel.configure(text='Downloading...')

def DownloadVideo():
    getdata = threading.Thread(target=DownloadVideoData)
    getdata.start()

def ChangeIntroLabelColor():
    ss = random.choice(colors)
    IntroLabel.configure(fg=ss)
    IntroLabel.after(20, ChangeIntroLabelColor)

# Ceating Label, Entry, Listbox, Buttons, ProgressBar #
Scroll_bar = Scrollbar(root)
IntroLabel = Label(root, text="JAK YouTube Video/Audio Downloader", width=36, relief='ridge', bd=4, font=('agency fb', 40, 'italic bold'), fg="red")
ChangeIntroLabelColor()
list_Box = Listbox(root, yscrollcommand=Scroll_bar.set, width=50, height=10, font=('arial', 12, 'italic bold'), relief='groove', bd=2, highlightcolor="blue", highlightbackground="orange", highlightthickness="2")
list_Box.bind('<<ListboxSelect>>', SelectCursor)
DownloadingSizeLabel = Label(root, text="Total Size: ", font=('arial', 15, 'bold'), bg="olivedrab1")
DownloadingRecievedLabel = Label(root, text="Recieved Size: ", font=('arial', 15, 'bold'), bg="olivedrab1")
DownloadingTimeLabel = Label(root, text="Time Left: ", font=('arial', 15, 'bold'), bg="olivedrab1")
DownloadingSizeLabelResult = Label(root, text='', font=('arial', 15, 'bold'), bg="olivedrab1")
DownloadingRecievedLabelResult = Label(root, text='', font=('arial', 15, 'italic bold'), bg="olivedrab1")
DownloadingTimeLabelResult = Label(root, text='', font=('arial', 15, 'italic bold'), bg="olivedrab1")
DownloadingBarTextLabel = Label(root, text='', width=36, fg='red', font=('agency fb', 23, 'bold'), bg="olivedrab1")
DownloadingProgressBarLabel = Label(root, text='', width=36, font=('agency fb', 40, 'bold'), bg="olivedrab1", fg='red', relief='raised')
UrlEntry = Entry(root, textvariable=urltext, font=('arial', 20, 'bold'), width=31)
ClickButton = Button(root, text='Enter URL and Click', font=('arial', 10, 'bold'), bg='green', fg='red', activebackground='blue', width=23, bd=8, command=VideoURL)
DownloadingProgressBar = Progressbar(DownloadingProgressBarLabel, orient=HORIZONTAL, value=0, length=100)
DownloadButton = Button(root, text='Download', font=('arial', 10, 'bold'), bg='red', fg='white', activeforeground='blue', width=23, bd=8, command=DownloadVideo)

# Placing Label, Entry, Listbox, Buttons, ProgressBar #
IntroLabel.place(x=10, y=20)
list_Box.place(x=20, y=230)
Scroll_bar.configure(command=Listbox.yview)
DownloadingSizeLabel.place(x=505 , y=240)
DownloadingRecievedLabel.place(x=505, y=290)
DownloadingTimeLabel.place(x=505, y=340)
DownloadingSizeLabelResult.place(x=655, y=240)
DownloadingRecievedLabelResult.place(x=655, y=290)
DownloadingTimeLabelResult.place(x=655, y=340)
DownloadingBarTextLabel.place(x=369, y=440)
DownloadingProgressBarLabel.place(x=20, y=445)
UrlEntry.place(x=20, y=150)
DownloadingProgressBar.grid(row=0, column=0, ipadx=185, ipady=3)
ClickButton.place(x=530, y=150)
Scroll_bar.place(x=477, y=230, height=193, width=20)
DownloadButton.place(x=510, y=380)

# Loop #
root.mainloop()

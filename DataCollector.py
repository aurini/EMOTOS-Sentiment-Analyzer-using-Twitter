from tkinter import *
import tkinter.messagebox
from tkinter import Tk, FALSE, mainloop
from gingerit.gingerit import GingerIt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk
from tkcalendar import Calendar
import tweepy as tw
import sqlite3
import datetime
from GetTwitterData import get_twitter_Data
from GraphicalRepresentation import GraphicalRepresentation
from RunAnalyzer import RunAnalyzer


class analysis_text():
    start_date = 0
    end_date = 0
    uName = 'abc'
    screen_name = ""

    def center(self, toplevel):

        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))
    def callback(self):
        if tkinter.messagebox.askokcancel("Quit", "Do you really wish to quit?"):
            self.main.destroy()

    def FROM(self):
        def print_sel():
            self.start_date = cal.selection_get()
            print(cal.selection_get())
            self.label_StartDate = Label(text='From ' + str(self.start_date), font=("Helvetica", 15))
            self.label_StartDate.pack()
            top.destroy()

        top = tk.Toplevel()
        cal = Calendar(top,
                       font="Arial 14", selectmode='day',
                       cursor="hand1", year=2020, month=8, day=5)
        cal.pack(fill="both", expand=True)
        ttk.Button(top, text="ok", command=print_sel).pack()

    def TO(self):
        def print_sel():
            self.end_date = cal.selection_get()
            print(cal.selection_get())
            self.label_EndDate = Label(text="To " + str(self.end_date), font=("Helvetica", 15))
            self.label_EndDate.pack()
            top.destroy()

        top = tk.Toplevel()
        cal = Calendar(top,
                       font="Arial 14", selectmode='day',
                       cursor="hand1", year=2020, month=8, day=5)
        cal.pack(fill="both", expand=True)
        ttk.Button(top, text="ok", command=print_sel).pack()

    def editedText(self, event):
        self.typedText.configure(text=self.line.get() + event.char)

    def runByEnter(self, event):
        run_alyzr= RunAnalyzer
        run_alyzr.run_analyzer()

    def getTwitterData(self):
        get_twitter_data = get_twitter_Data()
        get_twitter_data.getTwitterData(self.start_date, self.end_date, self.uName)

    def graphical_representation(self):
        graph_repre = GraphicalRepresentation
        graph_repre.representation()



    def __init__(self):
        # Create main window
        self.main = Tk()
        self.main.title("Sentiment Analysis")
        self.main.geometry("1000x1000")
        self.main.resizable(width=FALSE, height=FALSE)
        self.main.protocol("WM_DELETE_WINDOW", self.callback)
        self.main.focus()
        self.center(self.main)

        # Enter User Name
        self.label_Name = Label(text="Enter User Name", font=("Helvetica", 15))
        self.label_Name.pack()
        # Add a hidden button Enter
        self.line = Entry(self.main, width=70)
        self.uName= self.line.get()
        self.line.pack()

        # Calender Input
        s = ttk.Style(self.main)
        s.theme_use('clam')
        ttk.Button(self.main, text='Date From', command=self.FROM).pack(padx=10, pady=10)
        ttk.Button(self.main, text='Date To', command=self.TO).pack(padx=10, pady=10)

        # get Twitter data
        self.textLabel = Label(text="\nGet Twitter Data:", font=("Helvetica", 15))
        self.textLabel.pack()
        ttk.Button(self.main, text='Collect Data', command=self.getTwitterData).pack(padx=10, pady=10)

        self.typedText = Label(text="", fg="blue", font=("Helvetica", 20))
        self.typedText.pack()

        self.line.bind("<Key>", self.editedText)
        self.line.bind("<Return>", self.runByEnter)

        ttk.Button(self.main, text='Graphical Representation', command=self.graphical_representation).pack(padx=10, pady=10)

        self.analyzeLabel = Label(text="", fg="black", font=("Helvetica", 20))
        self.analyzeLabel.pack()
        self.negativeLabel = Label(text="", fg="red", font=("Helvetica", 20))
        self.negativeLabel.pack()
        self.neutralLabel = Label(text="", font=("Helvetica", 20))
        self.neutralLabel.pack()
        self.positiveLabel = Label(text="", fg="green", font=("Helvetica", 20))
        self.positiveLabel.pack()
        self.compoundLabel = Label(text="", fg="blue", font=("Helvetica", 20))
        self.compoundLabel.pack()


myanalysis = analysis_text()
mainloop()
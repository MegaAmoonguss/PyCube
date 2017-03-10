import os
import time
import math
import js2py
from datetime import datetime
from PIL import ImageTk
from tkinter import Tk, Frame, Menu, Label, Button, filedialog, RIGHT, LEFT, TOP, NO
from tkinter.constants import BOTH
from tkinter.ttk import Treeview, Scrollbar
from pycube.image_gen import genimage
from pycube.session import Session

if not os.path.isfile("./scrambler.py"):
    js2py.translate_file("../scrambler/wca-scramble.js", "scrambler.py")

from pycube.scrambler import scrambler #@UnresolvedImport

class PyCube:
    
    def __init__(self):
        self.root = Tk()
        self.root.title("PyCube")
        
        self.session = Session()
        
        # init UI
        self.initMenu()
        self.leftframe = Frame(self.root)
        self.leftframe.pack(side=LEFT, fill=BOTH, expand=1)
        
        self.rightframe = Frame(self.root)
        self.rightframe.pack(side=RIGHT, fill=BOTH, expand=1)
        
        self.cubesize = 3
        scrambler.parse(self.cubesize, 30, False, False)
        scrambler.scramble()
        self.scramble = Label(self.leftframe, text=scrambler.scramblestring(0))
        self.scramble.pack()

        self.time_label = Label(self.leftframe, text="0.000")
        self.time_label.pack()
        
        self.plus2_button = Button(self.leftframe, text="+2", command=self.plus2)
        self.plus2_button.pack()
        
        self.dnf_button = Button(self.leftframe, text="DNF", command=self.dnf)
        self.dnf_button.pack()
        
        self.delete_button = Button(self.leftframe, text="Delete", command=self.delete)
        self.delete_button.pack()
        
        self.scramble_img = Label(self.leftframe)
        self.scramble_img.pack()
        self.update_image()
        
        self.grid = Treeview(self.rightframe)
        self.grid["columns"] = ("times", "avg5", "avg12", "mean", "sd")
        self.grid.heading("#0", text='Time', anchor='w')
        self.grid.column("#0", stretch=NO, width=0, anchor="w")
        self.grid.heading("times", text="Times")
        self.grid.column('times', anchor='center', width=70)
        self.grid.heading("avg5", text="Avg. of 5")
        self.grid.column('avg5', anchor='center', width=70)
        self.grid.heading("avg12", text="Avg. of 12")
        self.grid.column('avg12', anchor='center', width=70)
        self.grid.heading("mean", text="Session mean")
        self.grid.column('mean', anchor='center', width=80)
        self.grid.heading("sd", text="SD")
        self.grid.column('sd', anchor='center', width=70)
        
        self.gridscroll = Scrollbar()
        self.gridscroll.configure(command=self.grid.yview)
        
        self.grid.configure(yscrollcommand=self.gridscroll.set)
        self.grid.pack(side=TOP)
        
        self.root.bind("<KeyRelease-space>", self.start_inspection)
        self._job = None
        self.running = False
        
        self.root.mainloop()
        
    def initMenu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="New", command=self.session_new)
        fileMenu.add_separator()
        fileMenu.add_command(label="Import", command=self.session_import)
        fileMenu.add_command(label="Export", command=self.session_export)
        menubar.add_cascade(label="File", menu=fileMenu)
        
    def start_timer(self, event=None):
        if not self.running:
            self.root.after_cancel(self._job)
            self._job = None
            self.t0 = float("%.3f" % time.time())
            self.update_timer()
            self.running = True
            self.root.bind("<KeyPress-space>", self.reset_timer)
    
    def reset_timer(self, event=None):
        if self.running:
            self.root.after_cancel(self._job)
            self._job = None
            self.running = False
            self.root.bind("<KeyRelease-space>", self.rebind)
            
            t = self.time_label.cget("text")
            if ":" in str(t):
                mins, secs = t.split(":")
                t = (mins * 60) + secs
            self.session.addtime(t, 0, scrambler.scramblestring(0))
            
            entry = self.session.data[-1][1:]
            self.grid.insert("", "end", values=(entry))
            
            scrambler.parse(self.cubesize, 30, False, False)
            scrambler.scramble()
            scramblestr = scrambler.scramblestring(0)
            self.scramble.configure(text=scramblestr)
            self.update_image()
            
    def rebind(self, event=None):
        self.root.bind("<KeyRelease-space>", self.start_inspection)
        
    def update_timer(self):
        now = float("%.3f" % (time.time() - self.t0))
        if now > 60:
            mins = math.floor(now / 60)
            secs = now - (mins * 60)
            now = f"{mins}:{secs}"
        self.time_label.configure(text=now, fg="black")
        self._job = self.root.after(10, self.update_timer)
    
    def start_inspection(self, event=None):
        self.inspect_time = 5
        self.root.bind("<KeyRelease-space>", self.start_timer)
        self.update_inspection()
    
    def update_inspection(self):
        if self.inspect_time == 0:
            self.time_label.configure(text="DNF", fg="red")
            
            # Really ugly was to add a straight DNF, should fix later
            # NOTE: Known bug when first time is DNF. MUST FIX
            self.session.addtime(0, 2, scrambler.scramblestring(0))
            entry = self.session.data[-1][1:]
            self.grid.insert("", "end", values=(entry))
            self.dnf()
        else:
            self.inspect_time -= 1
            self.time_label.configure(text=self.inspect_time, fg="red")
            self._job = self.root.after(1000, self.update_inspection)
        
    def update_image(self):
        img = ImageTk.PhotoImage(genimage(scrambler.imagestring(0), self.cubesize))
        self.scramble_img.configure(image=img)
        self.scramble_img.image = img
    
    def delete(self, event=None):
        if len(self.session.data) > 0:
            last = self.session.getlastitemid()
            self.grid.delete(last)
            self.session.removetime(last) 
    
    def plus2(self, event=None):
        if len(self.session.data) > 0:
            last = self.session.getlastitemid()
            index = len(self.session.data) - 1
            entry = self.session.data[index]
            
            # Check if time isn't already +2 or DNF9
            if entry[6] != 0:
                return
            
            entry[1] = float("%.3f" % (entry[1] + 2))
            entry[6] = 1
            entry = self.session.calcstats()
            vals = entry[1:] + [scrambler.scramblestring(0)]
            vals[0] = str(vals[0]) + "(+2)"
            self.grid.item(last, values=(vals))
            
    def dnf(self, event=None):
        if len(self.session.data) > 0:
            last = self.session.getlastitemid()
            index = len(self.session.data) - 1
            entry = self.session.data[index]
            
            entry[1] = "DNF"
            entry[6] = 2
            
            entry = self.session.calcstats()
            vals = entry[1:]
            self.grid.item(last, values=(vals))
            
    def session_new(self):
        self.session.clear()
        self.grid.delete(*self.grid.get_children())
    
    def session_import(self):
        f = filedialog.askopenfilename(initialdir="../data/",
                                       title="Import session",
                                       filetypes=(("Text Documents", "*.txt"), ("All Files", "*.*")))
        if f == '':
            return
        with open(f) as file:
            self.session_new()
            self.session = Session(file.read())
            
            for entry in self.session.data:
                self.grid.insert("", "end", values=(entry[1:]))
    
    def session_export(self):
        if not os.path.isdir("../data/"):
            os.makedirs("../data/")
            
        name = str(datetime.now())[:-7].replace('-', '').replace(':', '').replace(' ', '')
        f = filedialog.asksaveasfilename(initialfile=name,
                                         initialdir="../data/",
                                         defaultextension="*.txt",
                                         title="Export session",
                                         filetypes=(("Text Documents","*.txt"), ("All Files","*.*")))
        if f == '':
            return
        with open(f, 'w') as file:
            file.write(str(self.session))

app = PyCube()
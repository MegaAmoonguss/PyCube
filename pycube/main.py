import os
import time
import js2py
from datetime import datetime
from PIL import ImageTk
from tkinter import Tk, Frame, Label, Button, filedialog, RIGHT, LEFT, TOP, NO
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
        self.initUI()
        
        self.root.mainloop()
        
    def initUI(self):
        leftframe = Frame(self.root)
        leftframe.pack(side=LEFT, fill=BOTH, expand=1)
        
        rightframe = Frame(self.root)
        rightframe.pack(side=RIGHT, fill=BOTH, expand=1)
        
        scrambler.scramble()
        self.scramble = Label(leftframe, text=scrambler.scramblestring(0))
        self.scramble.pack()

        self.time_label = Label(leftframe, text="0.000")
        self.time_label.pack()
        
        self.scramble_img = Label(leftframe)
        self.scramble_img.pack()
        self.update_image()
        
        self.save = Button(rightframe, text="Save", command=self.export)
        self.save.pack()
        
        self.grid = Treeview(rightframe)
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
        
        self.root.bind("<KeyRelease-space>", self.start_timer)
        self._job = None
        self.running = False
        
    def start_timer(self, event=None):
        if not self.running:
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
            
            t = float(self.time_label.cget("text"))
            self.session.addtime(t, scrambler.scramblestring(0))
            
            self.grid.insert("", "end", values=(self.session.data[-1]))
            
            scrambler.scramble()
            scramblestr = scrambler.scramblestring(0)
            self.scramble.configure(text=scramblestr)
            self.update_image()
    
    def rebind(self, event=None):
        self.root.bind("<KeyRelease-space>", self.start_timer)
        
    def update_timer(self):
        now = float("%.3f" % (time.time() - self.t0))
        self.time_label.configure(text=now)
        self._job = self.root.after(10, self.update_timer)
        
    def update_image(self):
        img = ImageTk.PhotoImage(genimage(scrambler.imagestring(0)))
        self.scramble_img.configure(image=img)
        self.scramble_img.image = img
    
    def delete_item(self):
        selected_item = self.grid.selection()[0]
        self.grid.delete(selected_item)
    
    def export(self):
        if not os.path.isdir("data"):
            os.makedirs("data")
            
        name = str(datetime.now())[:-7].replace('-', '').replace(':', '').replace(' ', '')
        f = filedialog.asksaveasfilename(initialfile=name,
                                         initialdir="../data/",
                                         defaultextension="*.txt",
                                         title="Save session",
                                         filetypes=(("Text Documents","*.txt"), ("All Files","*.*")))
        if f == '':
            return
        with open(f, 'w') as file:
            file.write(str(self.session))

app = PyCube()
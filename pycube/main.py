import os
import time
import js2py
from datetime import datetime
from PIL import ImageTk
from tkinter import Tk, Menu, Frame, Label, Button, filedialog, RIGHT, LEFT, TOP, NO
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
        self.leftframe = Frame(self.root)
        self.leftframe.pack(side=LEFT, fill=BOTH, expand=1)
        
        self.rightframe = Frame(self.root)
        self.rightframe.pack(side=RIGHT, fill=BOTH, expand=1)
        
        scrambler.scramble()
        self.scramble = Label(self.leftframe, text=scrambler.scramblestring(0))
        self.scramble.pack()

        self.time_label = Label(self.leftframe, text="0.000")
        self.time_label.pack()
        
        self.scramble_img = Label(self.leftframe)
        self.scramble_img.pack()
        self.update_image()
        
        self.save = Button(self.rightframe, text="Save", command=self.export)
        self.save.pack()
        
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
        
        self.root.bind("<KeyRelease-space>", self.start_timer)
        self._job = None
        self.running = False
        
        self.aMenu = Menu(self.root, tearoff=0)
        self.aMenu.add_command(label="Delete", command=self.delete)
        self.aMenu.add_command(label="+2", command=self.plus2)
        self.aMenu.add_command(label="DNF", command=self.dnf)
        self.grid_item = ''
        
        self.grid.bind("<Button-3>", self.popup)
        
        self.root.mainloop()
        
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
            
            self.grid.insert("", "end", values=(self.session.data[-1][1:]))
            
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
    
    def delete(self):
        if self.grid_item:
            self.grid.delete(self.grid_item)
            self.session.removetime(self.grid_item)
    
    def plus2(self):
        if self.grid_item:
            index = self.session.getidindex(self.grid_item)
            
            # Check if time isn't already +2 or DNF
            if self.session.data[index][7] == 1 or self.session.data[index][8] == 1:
                return
            
            self.session.data[index][1] += 2
            self.session.data[index][7] = 1
            vals = self.session.data[index]
            self.grid.item(self.grid_item, values=(vals[1:]))
            
    def dnf(self):
        if self.grid_item:
            index = self.session.getidindex(self.grid_item)
            self.session.data[index][1] = "DNF"
            self.session.data[index][8] = 1
            vals = self.session.data[index]
            self.grid.item(self.grid_item, values=(vals[1:]))
            
    def popup(self, event):
        self.aMenu.post(event.x_root, event.y_root)
        self.grid_item = self.grid.focus()
    
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
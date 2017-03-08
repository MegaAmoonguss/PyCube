import os
import time
import js2py
from datetime import datetime
from PIL import ImageTk
from tkinter import Tk, Frame, Label, Button, filedialog
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
        frame = Frame(self.root)
        frame.pack()
        
        scrambler.scramble()
        self.scramble = Label(frame, text=scrambler.scramblestring(0))
        self.scramble.pack()

        self.time_label = Label(frame, text="0.000")
        self.time_label.pack()
        
        self.scramble_img = Label(frame)
        self.scramble_img.pack()
        self.update_image()
        
        self.save = Button(text="Save", command=self.savetimes)
        self.save.pack()
        
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
            self.session.addtime(float(self.time_label.cget("text")))
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
    
    def savetimes(self):
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
            file.write(self.session.gettimes())

app = PyCube()
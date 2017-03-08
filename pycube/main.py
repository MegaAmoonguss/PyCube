import time
from tkinter import Tk, Frame, Label
import os
import js2py

if not os.path.isfile("scrambler.py"):
    js2py.translate_file("../scrambler/wca-scramble.js", "scrambler.py")

from pycube.scrambler import scrambler

class PyCube:
    
    def __init__(self):
        self.root = Tk()
        
        frame = Frame(self.root)
        frame.pack()

        scrambler.scramble()
        self.scramble = Label(frame, text=scrambler.scramblestring(0))
        self.scramble.pack()

        self.time_label = Label(frame, text="0.000")
        self.time_label.pack()
        
        self.root.bind("<space>", self.timer)
        self._job = None
        
        self.root.mainloop()
        
    def timer(self, event=None):
        if self._job == None:
            self.t0 = float("%.3f" % time.time())
            self.update_timer()
        else:
            self.root.after_cancel(self._job)
            self._job = None
            scrambler.scramble()
            self.scramble.configure(text=scrambler.scramblestring(0))
        
    def update_timer(self):
        now = float("%.3f" % (time.time() - self.t0))
        self.time_label.configure(text=now)
        self._job = self.root.after(10, self.update_timer)

app = PyCube()
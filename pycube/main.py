import time
from tkinter import Tk, Frame, Button, Label
from pycube.scrambler import scramble
    
class PyCube:
    
    def __init__(self):
        self.root = Tk()
        
        frame = Frame(self.root)
        frame.pack()

        self.scramble = Label(frame, text=scramble())
        self.scramble.pack()

        self.time_label = Label(frame, text="0.000")
        self.time_label.pack()

        self.time_button = Button(frame,
                             text="Start",
                             command=self.start_timer)
        self.time_button.pack()
        self.root.mainloop()
        
    def start_timer(self):
        self.t0 = float("%.3f" % time.time())
        self.time_button.configure(text="Stop",
                                   command=self.stop_timer)
        self.update_timer()
        
    def update_timer(self):
        now = float("%.3f" % (time.time() - self.t0))
        self.time_label.configure(text=now)
        self._job = self.root.after(10, self.update_timer)
        
    def stop_timer(self):
        self.time_button.configure(text="Start",
                                   command=self.start_timer)
        self.root.after_cancel(self._job)
        self._job = None
        self.scramble.configure(text=scramble())

app = PyCube()
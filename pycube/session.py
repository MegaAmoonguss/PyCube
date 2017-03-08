import os
import datetime

class Session:
    
    def __init__(self):
        self.times = []
    
    def addtime(self, time):
        self.times.append(time)
    
    def removetime(self, index):
        del self.times[index]
        
    def save(self):
        if not os.path.isdir("data"):
            os.makedirs("data")
        
        name = str(datetime.datetime.now())[:-7].replace('-', '').replace(':', '').replace(' ', '')
        with open(os.path.join("data", name + ".txt"), 'w') as file:
            for t in self.times:
                file.write(str(t) + '\n')
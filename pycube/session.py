class Session:
    
    def __init__(self):
        self.times = []
    
    def addtime(self, time):
        self.times.append(time)
    
    def removetime(self, index):
        del self.times[index]
        
    def gettimes(self):
        return '\n'.join([str(t) for t in self.times])
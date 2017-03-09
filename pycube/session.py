import statistics

class Session:
    
    def __init__(self):
        self.times = []
        self.avg5 = []
        self.avg12 = []
        self.means = []
        self.sds = []
    
    def addtime(self, time):
        self.times.append(time)
        
        # Calculate average of 5
        if len(self.times) >= 5:
            last5 = self.times[-5:]
            last5.remove(min(last5))
            last5.remove(max(last5))
            self.avg5.append(float("%.3f" % (sum(last5) / 3)))
        else:
            self.avg5.append("N/A")
            
        # Calculate average of 12
        if len(self.times) >= 12:
            last12 = self.times[-12:]
            last12.remove(min(last12))
            last12.remove(max(last12))
            self.avg12.append(float("%.3f" % (sum(last12) / 3)))
        else:
            self.avg12.append("N/A")
            
        # Calculate session mean
        self.means.append(float("%.3f" % (sum(self.times) / len(self.times))))
        
        # Calculate standard deviation
        if len(self.times) > 1:
            self.sds.append(float("%.3f" % statistics.stdev(self.times)))
        else:
            self.sds.append("N/A")
    
    def removetime(self, index):
        del self.times[index]
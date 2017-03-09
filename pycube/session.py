import statistics

class Session:
    
    def __init__(self):
        self.data = []
    
    def addtime(self, time, scramblestring):
        entry = [time]
        times = [self.data[i][0] for i in range(len(self.data))] + entry
        
        # Calculate average of 5
        if len(times) >= 5:
            last5 = times[-5:]
            last5.remove(min(last5))
            last5.remove(max(last5))
            entry.append(float("%.3f" % (sum(last5) / 3)))
        else:
            entry.append("N/A")
            
        # Calculate average of 12
        if len(times) >= 12:
            last12 = times[-12:]
            last12.remove(min(last12))
            last12.remove(max(last12))
            entry.append(float("%.3f" % (sum(last12) / 3)))
        else:
            entry.append("N/A")
            
        # Calculate session mean
        entry.append(float("%.3f" % (sum(times) / len(times))))
        
        # Calculate standard deviation
        if len(times) >= 2:
            entry.append(float("%.3f" % statistics.stdev(times)))
        else:
            entry.append("N/A")
        
        entry.append(scramblestring)
        self.data.append(entry)
    
    def removetime(self, index):
        del self.times[index]
        
    def __str__(self):
        s = ""
        for i in range(len(self.times)):
            s += ' '.join(self.data[i]) + '\n'
        return s
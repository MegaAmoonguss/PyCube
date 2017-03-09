import statistics

class Session:
    
    def __init__(self, datastring=None):
        if not datastring:
            self.data = []
            self.num_items = 0
        else:
            self.data = [entry.split()[:8] for entry in datastring.split('\n') if len(entry) > 0]
            self.num_items = len(self.data)
            
            for r in range(len(self.data)):
                for c in range(1, 6):
                    try:
                        self.data[r][c] = float(self.data[r][c])
                    except ValueError:
                        continue
    
    def addtime(self, time, scramblestring):
        self.num_items += 1
        id = 'I'
        if self.num_items < 100:
            id += '0'
            if self.num_items < 10:
                id += '0'
                id += str(self.num_items)
            else:
                id += str(self.num_items)
        else:
            id += str(self.num_items)
        
        entry = [id, time]
        times = [self.data[i][1] for i in range(len(self.data)) if self.data[i][1] != "DNF"] + entry[1:]
        
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
        
        # Append two 0s to signify no +2 and no DNF respectively
        entry.append(0)
        entry.append(0)
        
        entry.append(scramblestring)
        self.data.append(entry)
    
    def removetime(self, id):
        del self.data[self.getidindex(id)]
    
    def getidindex(self, id):
        for i in range(len(self.data)):
            if self.data[i][0] == id:
                return i
    
    def getlastitemid(self):
        return self.data[-1][0]
    
    def clear(self):
        self.data = []
        
    def __str__(self):
        s = ""
        for i in range(len(self.data)):
            s += ' '.join([str(value) for value in self.data[i]]) + '\n'
        return s
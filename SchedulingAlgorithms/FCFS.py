class FCFS(object):
    def __init__(self, bt):
        self._bt = bt
        self._wt = [0]

    def avgWaitTime(self):
        for i in range(1,len(self._bt)):
            self._wt.append(self._bt[i-1] + self._wt[i-1])
        return (sum(self._wt)/ len(self._wt))

    def avgTAT(self):
        tat = [0] * len(self._bt)
        for i in range(1,len(self._bt)):
            tat[i] = self._wt[i] + self._bt[i]
        return sum(tat) / len(tat)

f = FCFS([24,3,7,5])
f.avgWaitTime()
f.avgTAT()



class SJF(object):
    def __init__(self, bt):
        self._bt = sorted(bt)
        self._wt = [0]

    def averageWaitTime(self):
        for i in range(1,len(self._bt)):
            self._wt.append(self._bt[i-1] + self._wt[i-1])
        return sum(self._wt) / len(self._wt)

    def turnAroundTime(self):
        tat = list()
        for i in range(len(self._bt)):
            tat.append(self._bt[i] +  self._wt[i])
        return sum(tat)/ len(tat)

s = SJF([6,8,7,3])
print(s.averageWaitTime())
print(s.turnAroundTime())

from collections import deque
class FCFS2(object):
    def __init__(self, burstTime, arrivalTime):
        self._bt = burstTime
        self._at = arrivalTime
        self._wt = [0] * len(self._bt)

    def waitTime(self):
        totalTime = self._bt[0]
        for i in range(1,len(self._bt)):
            if totalTime < self._at[i]:
                totalTime += (self._at[i] - totalTime)
            self._wt[i] =  totalTime - self._at[i]
            totalTime += self._bt[i]
        return sum(self._wt) / len(self._wt)

    def turnAroundTime(self):
        tat = list()
        for i in range(len(self._bt)):
            tat.append(self._bt[i] + self._wt[i])
        print(sum(tat) / len(tat))

f = FCFS2([5,9,6], [3,3,6])
a = f.waitTime()
print(a)
f.turnAroundTime()



class MinHeap(object):
    def __init__(self, items):
        self.__heap = [0]
        for i in items:
            self.__heap.append(i)
            self.__float_up(len(self.__heap) - 1)
            self.show()

    def push(self, item):
        self.__heap.append(item)
        self.__float_up(len(self.__heap) - 1)

    def peek(self):
        if self.__heap[1]:
            return self.__heap[1]
        return None

    def pop(self):
        if len(self.__heap) > 2:
            self.__swap(1,len(self.__heap)- 1)
            minEle = self.__heap.pop()
            self.__bubble_down(1)
        elif len(self.__heap) == 2:
            minEle = self.__heap.pop()
        else:
            return False
        return minEle

    def __swap(self, i, j):
        self.__heap[i], self.__heap[j] = self.__heap[j], self.__heap[i]

    def __float_up(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.__heap[parent] > self.__heap[index]:
            self.__swap(parent, index)
            self.__float_up(parent)

    def __bubble_down(self, index):
        left = index * 2
        right = left + 1
        minVal = index
        if len(self.__heap) > left and self.__heap[left] < self.__heap[minVal]:
            minVal = left
        if len(self.__heap) > right and self.__heap[right] < self.__heap[minVal]:
            minVal = right
        if index != minVal:
            self.__swap(index, minVal)
            self.__bubble_down(minVal)


    def show(self):
        print(self.__heap)


m = MinHeap([2,6,7,8,1,4])
m.show()
m.push(20)
m.push(12)
m.push(5)
m.show()
m.pop()
print("1st")
m.show()
m.pop()
print("2nd")
m.show()


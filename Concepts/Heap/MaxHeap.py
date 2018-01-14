class MaxHeap(object):
    '''
    Heap has 3 public functions push, pop and peep
    3 private functions float_up, bubble_down, swap
    '''

    def __init__(self, items = []):
        self.__heap = [0]
        for i in items:
            self.__heap.append(i)
            self.__float_up(len(self.__heap) - 1)

    def push(self,item):
        self.__heap.append(item)
        self.__float_up(len(self.__heap) - 1)

    def peek(self):
        if (len(self.__heap) > 1):
            return self.__heap[1]
        else:
            return False

    def pop(self):
        if len(self.__heap) > 2:
            self.__swap(1, len(self.__heap) - 1)
            max = self.__heap.pop()
            self.__bubble_down(1)
        elif len(self.__heap) == 2:
            max = self.__heap.pop()
        else:
            max = False
        return max

    def __swap(self, i, j):
        self.__heap[i], self.__heap[j] = self.__heap[j], self.__heap[i]

    def __float_up(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.__heap[index] > self.__heap[parent]:
            self.__swap(parent, index)
            self.__float_up(parent)

    def __bubble_down(self, index):
        left = 2 * index
        right = left + 1
        largest = index
        if len(self.__heap) > left and self.__heap[largest] < self.__heap[left]:
            largest = left
        if len(self.__heap) > right and self.__heap[largest] < self.__heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubble_down(largest)

    def show(self):
        print(self.__heap)

m = MaxHeap([2,6,7,8,1,4])
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


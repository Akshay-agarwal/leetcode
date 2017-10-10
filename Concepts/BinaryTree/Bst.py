class Node(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def find(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.left:
                self.left.find(data)
            else:
                return False
        else:
            if self.right:
                self.right.find(data)
            else:
                return False

    def preOrder(self):
        if self:
            print(str(self.value))
            if self.left:
                self.left.preOrder()
            if self.right:
                self.right.preOrder()

    def postOrder(self):
        if self:
            if self.left:
                self.left.postOrder()
            if self.right:
                self.right.postOrder()
            print(str(self.value))

    def inOrder(self):
        if self:
            if self.left:
                self.left.preOrder()
            print(str(self.value))
            if self.right:
                self.right.preOrder()


class Bst(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            self.root.find(data)
        else:
            return False

    def preOrder(self):
        print("preOrder")
        self.root.preOrder()

    def postOrder(self):
        print("postOrder")
        self.root.postOrder()

    def inOrder(self):
        print("inOrder")
        self.root.inOrder()

b = Bst()
b.insert(5)
b.insert(20)
b.insert(15)
b.insert(22)
b.insert(2)
c = b.find(5)
print(c)
b.inOrder()
b.postOrder()
b.preOrder()

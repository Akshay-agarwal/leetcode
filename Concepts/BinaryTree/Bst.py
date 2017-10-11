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


    def remove(self, data):
        #root is not present
        if not self.root:
            return False

        #data is root Node
        if self.root.value == data:
            if self.root.left is None and self.root.right is None:
                self.root = None
            elif self.root.left and self.root.right is None:
                self.root = self.root.left
            elif self.root.left is None and self.root.right:
                self.root = self.root.right
            elif self.root.left and self.root.right:
                delNodeParent = self.root
                delNode = self.root.right
                while delNode.left:
                    delNodeParent = delNode
                    delNode = delNode.left
                self.root = delNode.value

            if delNode.right:
                if delNodeParent.value > delNode.value:
                    delNodeParent.left = delNode.right
                elif delNodeParent.value < delNode.value:
                    delNodeParent.right = delNode.right

            else:
                if delNodeParent.value > delNode.value:
                    delNodeParent.left = None
                else:
                    delNodeParent.right = None

        #Find if the value is present
        node = self.root
        parent = None

        while node and node.value != data:
            parent = node
            if node.value > data:
                node = node.left
            elif node.value < data:
                node = node.right

        #Element not found case
        if node is Node or node.value != data:
            return False

        #No Children
        elif node.left is None and node.right is None:
            if data < parent.value:
                parent.left = None
            else:
                parent.right = None
            return True

        #Only Left child
        elif node.left and node.right is None:
            if data < parent.value:
                parent.left = node.left
            else:
                parent.right = node.left
            return True

        #Only Right CHild
        elif node.right and node.left is None:
            if data < parent.value:
                parent.left = node.right
            else:
                parent.right = node.right
            return True

        else:
            delNode = node.right
            delNodeParent = node

            while node.left:
                delNodeParent = delNode
                delNode = node.left

            node.value = delNode.value
            if node.right:
                if delNodeParent.value > delNode.value:
                    delNodeParent.left = delNode.right
                elif delNodeParent.value < delNode.value:
                    delNodeParent.right = delNode.right

            else:
                if delNodeParent.value > delNode.value:
                    delNode.left = None
                else:
                    delNode.right = None

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
b.remove(22)
b.postOrder()
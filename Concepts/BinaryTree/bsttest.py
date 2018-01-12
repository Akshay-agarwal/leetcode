class Node(object):  # Please do not remove or rename any of this code
    """Represents a single node in the Ternary Search Tree"""

    def __init__(self, val):
        self.val = val
        self.left = None
        self.mid = None
        self.right = None

    """I writing another insert function for the node, so that node would do all the heavy lifting"""

    def insert(self, data):
        if self.val == data:
            if self.mid:
                self.mid.insert(data)
            else:
                self.mid = Node(data)
        elif self.val > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)


class Tree(object):  # Please do not remove or rename any of this code
    """The Ternary Search Tree"""

    def __init__(self):
        self.root = None

    # Please complete this method.
    """Inserts val into the tree. There is no need to rebalance the tree."""

    def insert(self, data):
        if self.root:
            self.root.insert(data)
        else:
            self.root = Node(data)

    # Please complete this method.
    """Deletes only one instance of val from the tree.
       If val does not exist in the tree, do nothing.
       There is no need to rebalance the tree."""

    def delete(self, data):
        if self.root is None:
            pass

        # the node to be deleted is in the root Node
        elif self.root.val == data:
            if self.mid:
                self.root = self.mid
            elif self.root.left is None and self.root.right is None:
                self.root = None
            elif self.root.left and self.root.right is None:
                self.root = self.root.left
            elif self.root.left is None and self.root.right:
                self.root = self.root.rightChild
            elif self.root.left and self.root.right:
                deleteNodeParent = self.root
                deleteNode = self.root.right
                while deleteNode.leftChild:
                    deleteNodeParent = deleteNode
                    deleteNode = deleteNode.leftChild

                self.root.value = deleteNode.value
                if deleteNode.mid and deleteNode.right:
                    deleteNodeParent.left = deleteNode.mid
                elif deleteNode.right:
                    deleteNodeParent.left = deleteNode.right
                else:
                    deleteNodeParent.left = None

        parent = None
        node = self.root
        # first find the node that is to be removed
        while node and node.val != data:
            parent = node
            if data < node.val:
                node = node.left
            else:
                node = node.right

        # Case 1: The node to delete does not exist
        if node is None or node.val != data:
            pass

        # Case 2: Node with no children
        elif node.left is None and node.right is None and node.mid is None:
            if data < parent.val:
                parent.left = None
            else:
                parent.right = None

        # Case 3: Node has only left child
        elif node.left and node.right is None and node.mid is None:
            if data < parent.val:
                parent.left = node.left
            else:
                parent.right = node.left

        # Case 4: Node has only right child
        elif node.left is None and node.mid is None and node.right:
            if data < parent.val:
                parent.left = node.right
            else:
                parent.right = node.right

        # Case 5: Node has only middle child
        elif node.left is None and node.mid and node.right is None:
            node = node.mid

        # Case 6: Node has left and middle child
        elif node.left and node.mid and node.right is None:
            node = node.mid

        # Case 7: Node has right and middle child
        elif node.left is None and node.mid and node.right:
            node = node.mid

        # Case 8: Node has left and right child
        deleteNodeParent = node
        deleteNode = node.rightChild
        while deleteNode.leftChild:
            deleteNodeParent = deleteNode
            deleteNode = deleteNode.left

        node.val = deleteNode.val
        if deleteNode.right and deleteNode.mid:
            deleteNodeParent.left = deleteNode.mid

        elif deleteNode.right:
            deleteNodeParent.left = deleteNode.right

        else:
            deleteNodeParent.left = None

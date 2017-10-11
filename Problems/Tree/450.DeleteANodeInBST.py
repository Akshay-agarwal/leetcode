# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        # No Root
        if not root:
            return None

        # Root is Key
        elif root.val == key:
            if root.left is None and root.right is None:
                return None
            elif root.left and root.right is None:
                return root.left
            elif root.left is None and root.right:
                return root.right
            else:
                delNode = root.right
                delNodeParent = root

                while delNode.left:
                    delNodeParent = delNode
                    delNode = delNode.left

                root.val = delNode.val
                if delNode.right:
                    if delNodeParent.val > delNode.val:
                        delNodeParent.left = delNode.right
                    else:
                        delNodeParent.right = delNode.right
                else:
                    if delNodeParent.val > delNode.val:
                        delNodeParent.left = None
                    else:
                        delNodeParent.right = None
                return root

        node = root
        parent = None

        # Find the element
        while node and node.val != key:
            parent = node
            if node.val > key:
                node = node.left
            elif node.val < key:
                node = node.right

        # Not found
        if not node or node.val != key:
            return root

        # No children case
        elif not node.left and not node.right:
            if parent.val > key:
                parent.left = None
            elif parent.val < key:
                parent.right = None
            return root

        # Only left child
        elif node.left and not node.right:
            if parent.val > node.val:
                parent.left = node.left
            else:
                parent.right = node.left
            return root

        # Only right child
        elif not node.left and node.right:
            if parent.val > node.val:
                parent.left = node.right
            else:
                parent.right = node.right
            return root

        # Both Children
        else:
            delNode, delNodeParent = node.right, node
            while delNode.left:
                delNodeParent = delNode
                delNode = delNode.left

            node.val = delNode.val
            if delNode.right:
                if delNodeParent.val > delNode.val:
                    delNodeParent.left = delNode.right
                else:
                    delNodeParent.right = delNode.right
            else:
                if delNodeParent.val > delNode.val:
                    delNodeParent.left = None
                else:
                    delNodeParent.right = None
            return root
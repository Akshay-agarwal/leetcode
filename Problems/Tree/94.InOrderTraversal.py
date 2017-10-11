# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        curr = root
        stack, res = [], []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            if stack:
                node = stack.pop()
                res.append(node.val)
                curr = node.right
        return res
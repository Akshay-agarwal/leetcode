# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q, q2, result = deque(), [], []
        q.append((root,1))
        while q:
            node = q.popleft()
            if node:
                q2.append((node[0].val, node[1]))
            if node[0].left:
                q.append((node[0].left, node[1]+1))
            if node[0].right:
                q.append((node[0].right, node[1]+1))
        for (key, value) in q2:
            if len(result) < value:
                result.append([])
            result[value-1].append(key)
        return result
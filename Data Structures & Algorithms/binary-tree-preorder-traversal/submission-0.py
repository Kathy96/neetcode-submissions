# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        node = root
        while stack or node:
            if node:
                res.append(node.val)
                stack.append(node.right)
                node = node.left
            else:
                node = stack.pop()
            
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
   
        result = 0
        
        def dfs(node, prev_max):
            nonlocal result
            if not node:
                return

            if node.val >= prev_max:
                result += 1
            prev_max = max(node.val, prev_max)
            dfs(node.left, prev_max)
            dfs(node.right, prev_max)
        
        
        dfs(root, root.val)
        return result
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
   
        
        def dfs(node, prev_max):
            if not node:
                return 0

            result = 1 if node.val >= prev_max else 0
            prev_max = max(node.val, prev_max)
            result += dfs(node.left, prev_max)
            result += dfs(node.right, prev_max)

            return result
        
        return dfs(root, root.val)
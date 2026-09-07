# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cache
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def dfs(node, rob):
            if not node:
                return 0

            
            result = node.val if rob else 0

            if rob:
                result += dfs(node.right, False) + dfs(node.left, False)
                
            else:
                result += max([dfs(node.right, False) + dfs(node.left, False), \
                dfs(node.right, True) + dfs(node.left, False), \
                dfs(node.right, False) + dfs(node.left, True), \
                dfs(node.right, True) + dfs(node.left, True)])

            return result
            
        
        return max(dfs(root, True), dfs(root, False))
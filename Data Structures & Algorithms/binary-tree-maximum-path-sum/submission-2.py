# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float("-inf")
        
        def dfs(node):
            nonlocal result

            if not node:
                return float("-inf")
            left_max = dfs(node.left)
            right_max = dfs(node.right)
            max_connect = max(node.val + left_max,
                                node.val + right_max, 
                                node.val)
            max_go_through = max(node.val + left_max,
                                node.val + right_max, 
                                node.val, 
                                node.val + left_max + right_max
                                )
            result = max(result, max_go_through)
            return max_connect
        dfs(root)
        return result

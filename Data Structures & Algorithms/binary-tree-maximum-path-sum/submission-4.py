# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float("-inf")
        
        # DFS return the max sum that you can get by connect with this node
        def dfs(node):
            nonlocal result

            if not node:
                return 0
            
            # Use 0 to ignore negative branch -> they only lower the result
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)

            result = max(result, node.val + left_max + right_max)
            return node.val + max(left_max, right_max)
        dfs(root)
        return result

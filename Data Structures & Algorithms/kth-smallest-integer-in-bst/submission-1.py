# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # DFS -> inorder (left first)

        def dfs(node):
            nonlocal k
            if not node:
                return 
            left_result = dfs(node.left)
            if left_result:
                return left_result
            k -= 1
            if k == 0:
                return node.val
            right_result = dfs(node.right)
            if right_result:
                return right_result

        return dfs(root)
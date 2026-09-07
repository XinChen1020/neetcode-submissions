# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        
        # True -> deleted
        def dfs(node) -> bool:

            # Reaching the end
            if not node:
                return False

            if dfs(node.left):
                node.left = None
            if dfs(node.right):
                node.right = None

            # When reaching the leaf node
            if not node.left and not node.right:
                return node.val == target
            
        if not dfs(root):
            return root
        else:
            return None

            

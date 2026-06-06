# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # BFS
        queue = deque([(root, float("-inf"), float("inf"))])

        while queue:
            node, l_limit, r_limit = queue.popleft()
            if not (l_limit < node.val < r_limit):
                return False
            if node.left:
                queue.append((node.left, l_limit, node.val))
            if node.right:
                queue.append((node.right, node.val, r_limit))
        return True
